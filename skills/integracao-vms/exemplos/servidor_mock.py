#!/usr/bin/env python3
"""Adaptador mock, somente leitura, que recebe alertas por webhook assinado.

Só biblioteca padrão do Python 3.8+. Serve para estudar o padrão, nunca para produção.

O que ele demonstra:
- assinatura HMAC-SHA256 sobre "<timestamp>.<corpo>" com segredo lido de variável de ambiente;
- janela de tempo contra replay (padrão 300 s) e recusa de evento_id repetido;
- limite de requisições por cliente e de tamanho do corpo;
- minimização: só campos de uma lista fechada seguem adiante; o resto é descartado;
- log sem dado pessoal (só id, tipo, origem e resultado);
- somente leitura: não existe rota que escreva no sistema de origem; PUT, PATCH e DELETE dão 405.

Uso:
    export MOCK_WEBHOOK_SEGREDO="segredo-de-teste-local"   # nunca um segredo real
    python servidor_mock.py --porta 8088
    # em outro terminal:
    python enviar_alerta_mock.py alerta-webhook.json

Rotas:
    POST /webhook/alertas   recebe um evento assinado (o caminho pode ser trocado com --caminho)
    GET  /alertas           devolve os últimos eventos normalizados, para o assistente ler
    GET  /saude             devolve {"status": "ok"}
"""
import argparse
import collections
import hashlib
import hmac
import json
import os
import sys
import threading
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

JANELA_S = 300
MAX_CORPO = 64 * 1024
LIMITE_POR_MINUTO = 60

# Lista fechada de campos que seguem adiante. Qualquer outro campo é descartado.
CAMPOS_PERMITIDOS = {
    "evento_id", "origem", "tipo", "ocorrido_em", "camera_id", "confianca",
    "regra", "referencia_video", "selo",
    # eventos de controle de acesso (ver ../../integracao-controle-de-acesso)
    "leitor_id", "area", "id_pessoa_pseudonimo", "motivo", "credencial_status",
}

_lock = threading.Lock()
_vistos = collections.OrderedDict()   # evento_id -> instante em que foi visto
_eventos = collections.deque(maxlen=200)
_janelas = collections.defaultdict(collections.deque)  # cliente -> instantes das requisições


def log(msg):
    sys.stdout.write(time.strftime("%Y-%m-%dT%H:%M:%S") + " " + msg + "\n")
    sys.stdout.flush()


def assinatura_valida(segredo, timestamp, corpo, recebida):
    esperado = hmac.new(segredo, timestamp.encode() + b"." + corpo, hashlib.sha256).hexdigest()
    recebida = recebida[7:] if recebida.startswith("sha256=") else recebida
    return hmac.compare_digest(esperado, recebida)


def dentro_do_limite(cliente, agora):
    with _lock:
        fila = _janelas[cliente]
        while fila and agora - fila[0] > 60:
            fila.popleft()
        if len(fila) >= LIMITE_POR_MINUTO:
            return False
        fila.append(agora)
        return True


def ja_visto(evento_id, agora):
    with _lock:
        for chave in list(_vistos):
            if agora - _vistos[chave] > JANELA_S:
                del _vistos[chave]
            else:
                break
        if evento_id in _vistos:
            return True
        _vistos[evento_id] = agora
        return False


def normalizar(dado):
    descartados = sorted(k for k in dado if k not in CAMPOS_PERMITIDOS)
    limpo = {k: v for k, v in dado.items() if k in CAMPOS_PERMITIDOS}
    limpo["recebido_em"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    limpo.setdefault("selo", "integro")
    return limpo, descartados


class Handler(BaseHTTPRequestHandler):
    server_version = "adaptador-mock/0.2"

    def log_message(self, *args):  # silencia o log padrão, que inclui a linha da requisição
        pass

    def _responder(self, codigo, corpo):
        dados = json.dumps(corpo, ensure_ascii=False).encode()
        self.send_response(codigo)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(dados)))
        self.end_headers()
        self.wfile.write(dados)

    def do_GET(self):
        if self.path == "/saude":
            return self._responder(200, {"status": "ok"})
        if self.path == "/alertas":
            with _lock:
                return self._responder(200, {"alertas": list(_eventos)})
        return self._responder(404, {"erro": "ROTA_DESCONHECIDA", "acao": "use GET /alertas ou GET /saude"})

    def do_POST(self):
        agora = time.time()
        cliente = self.client_address[0]
        if self.path != self.server.caminho:
            return self._responder(404, {"erro": "ROTA_DESCONHECIDA", "acao": "envie para " + self.server.caminho})
        if not dentro_do_limite(cliente, agora):
            log("recusado limite_excedido")
            return self._responder(429, {"erro": "LIMITE_EXCEDIDO", "acao": "aguarde 60 s; limite de %d por minuto" % LIMITE_POR_MINUTO})
        try:
            tamanho = int(self.headers.get("Content-Length", "0"))
        except ValueError:
            tamanho = -1
        if tamanho <= 0 or tamanho > MAX_CORPO:
            return self._responder(413, {"erro": "CORPO_INVALIDO", "acao": "corpo entre 1 byte e %d bytes" % MAX_CORPO})
        corpo = self.rfile.read(tamanho)

        ts = self.headers.get("X-Timestamp", "")
        assinatura = self.headers.get("X-Assinatura", "")
        evento_id = self.headers.get("X-Evento-Id", "")
        if not (ts.isdigit() and assinatura and evento_id):
            return self._responder(400, {"erro": "CABECALHOS_AUSENTES", "acao": "envie X-Timestamp (epoch em segundos), X-Assinatura (sha256=<hex>) e X-Evento-Id"})
        if abs(agora - int(ts)) > JANELA_S:
            log("recusado fora_da_janela evento_id=%s" % evento_id)
            return self._responder(401, {"erro": "FORA_DA_JANELA", "acao": "confira o relógio (NTP) do emissor; janela de %d s" % JANELA_S})
        if not assinatura_valida(self.server.segredo, ts, corpo, assinatura):
            log("recusado assinatura_invalida evento_id=%s" % evento_id)
            return self._responder(401, {"erro": "ASSINATURA_INVALIDA", "acao": "assine '<timestamp>.<corpo>' com HMAC-SHA256 e o segredo combinado"})
        if ja_visto(evento_id, agora):
            log("recusado repetido evento_id=%s" % evento_id)
            return self._responder(409, {"erro": "EVENTO_REPETIDO", "acao": "evento já recebido; não reenvie o mesmo evento_id"})
        try:
            dado = json.loads(corpo.decode("utf-8"))
            if not isinstance(dado, dict):
                raise ValueError
        except ValueError:
            return self._responder(400, {"erro": "JSON_INVALIDO", "acao": "envie um objeto JSON em UTF-8"})
        if dado.get("evento_id") != evento_id:
            return self._responder(400, {"erro": "ID_DIVERGENTE", "acao": "X-Evento-Id precisa ser igual a evento_id do corpo"})

        limpo, descartados = normalizar(dado)
        with _lock:
            _eventos.append(limpo)
        extra = (" campos_descartados=" + ",".join(descartados)) if descartados else ""
        log("aceito evento_id=%s tipo=%s origem=%s%s" % (evento_id, limpo.get("tipo"), limpo.get("origem"), extra))
        return self._responder(202, {"status": "recebido", "evento_id": evento_id})

    def _somente_leitura(self):
        return self._responder(405, {"erro": "SOMENTE_LEITURA", "acao": "este adaptador não escreve no sistema de origem"})

    do_PUT = do_PATCH = do_DELETE = _somente_leitura


def main():
    p = argparse.ArgumentParser(description="Adaptador mock, somente leitura, para alertas por webhook.")
    p.add_argument("--porta", type=int, default=8088)
    p.add_argument("--caminho", default="/webhook/alertas")
    a = p.parse_args()
    segredo = os.environ.get("MOCK_WEBHOOK_SEGREDO")
    if not segredo:
        sys.exit("Defina MOCK_WEBHOOK_SEGREDO com um segredo de teste, ex.: export MOCK_WEBHOOK_SEGREDO=segredo-de-teste-local")
    srv = ThreadingHTTPServer(("localhost", a.porta), Handler)  # só escuta na própria máquina
    srv.segredo = segredo.encode()
    srv.caminho = a.caminho
    log("adaptador mock em http://localhost:%d%s (somente leitura)" % (a.porta, a.caminho))
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
