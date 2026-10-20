#!/usr/bin/env python3
"""Envia um evento de exemplo, assinado, para o servidor_mock.py. Só biblioteca padrão.

Uso:
    export MOCK_WEBHOOK_SEGREDO="segredo-de-teste-local"
    python enviar_alerta_mock.py alerta-webhook.json
    python enviar_alerta_mock.py alerta-webhook.json --repetir      # mostra a recusa de replay (409)
    python enviar_alerta_mock.py alerta-webhook.json --atrasado     # mostra a recusa por janela (401)
    python enviar_alerta_mock.py ../../integracao-controle-de-acesso/exemplos/credencial-revogada.json \
        --url http://localhost:8089/webhook/acesso
"""
import argparse
import hashlib
import hmac
import json
import os
import sys
import time
import urllib.error
import urllib.request
import uuid


def enviar(url, segredo, dado, atrasado=False):
    corpo = json.dumps(dado, ensure_ascii=False).encode("utf-8")
    ts = str(int(time.time()) - (900 if atrasado else 0))
    assinatura = hmac.new(segredo, ts.encode() + b"." + corpo, hashlib.sha256).hexdigest()
    req = urllib.request.Request(url, data=corpo, method="POST", headers={
        "Content-Type": "application/json",
        "X-Timestamp": ts,
        "X-Assinatura": "sha256=" + assinatura,
        "X-Evento-Id": dado["evento_id"],
    })
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.status, r.read().decode()
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("arquivo")
    p.add_argument("--url", default="http://localhost:8088/webhook/alertas")
    p.add_argument("--repetir", action="store_true")
    p.add_argument("--atrasado", action="store_true")
    a = p.parse_args()
    segredo = os.environ.get("MOCK_WEBHOOK_SEGREDO")
    if not segredo:
        sys.exit("Defina MOCK_WEBHOOK_SEGREDO com o mesmo segredo de teste do servidor.")
    with open(a.arquivo, encoding="utf-8") as f:
        dado = json.load(f)
    dado["evento_id"] = "EVT-" + uuid.uuid4().hex[:12]
    dado["ocorrido_em"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    print(*enviar(a.url, segredo.encode(), dado, a.atrasado))
    if a.repetir:
        print(*enviar(a.url, segredo.encode(), dado))


if __name__ == "__main__":
    main()
