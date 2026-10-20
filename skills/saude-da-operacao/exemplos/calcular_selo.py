#!/usr/bin/env python3
"""Calcula o selo de integridade do dado por câmera e por área. Só biblioteca padrão.

Selos, do pior para o melhor: sem_dado > atrasado > estimado > integro.
Regra central: falha de infraestrutura nunca aparece como "nada aconteceu".
Uma área só mostra "0 eventos" quando todas as câmeras dela estão íntegras.

Uso:
    python calcular_selo.py sinais-exemplo.json
"""
import json
import sys
from datetime import datetime

ORDEM = ["integro", "estimado", "atrasado", "sem_dado"]


def ts(s):
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ")


def selo_da_camera(c, agora, lim):
    if not c.get("ping_ok") or not c.get("gravando") or not c.get("ultimo_quadro_em"):
        return "sem_dado", "sem rede, sem gravação ou sem quadro"
    atraso = (agora - ts(c["ultimo_quadro_em"])).total_seconds()
    if atraso > lim["atraso_max_s"]:
        return "atrasado", "último quadro há %d s" % atraso
    if abs(c.get("deriva_relogio_s", 0)) > lim["deriva_relogio_max_s"]:
        return "atrasado", "relógio fora de sincronia"
    if c.get("fonte") != "medido":
        return "estimado", "valor completado por estimativa"
    return "integro", "imagem, gravação e relógio em dia"


def main(caminho):
    with open(caminho, encoding="utf-8") as f:
        d = json.load(f)
    agora, lim = ts(d["agora"]), d["limites"]
    areas = {}
    print("%-7s %-16s %-9s %s" % ("camera", "area", "selo", "motivo"))
    for c in d["cameras"]:
        selo, motivo = selo_da_camera(c, agora, lim)
        print("%-7s %-16s %-9s %s" % (c["camera_id"], c["area"], selo, motivo))
        a = areas.setdefault(c["area"], {"selo": "integro", "eventos": 0})
        if ORDEM.index(selo) > ORDEM.index(a["selo"]):
            a["selo"] = selo
        a["eventos"] += c.get("eventos_na_janela", 0)
    print()
    for nome, a in areas.items():
        if a["selo"] == "sem_dado":
            painel = "SEM VISÃO: alerta de infraestrutura para o operador"
        elif a["selo"] == "atrasado":
            painel = "%d eventos até o último dado recebido (atrasado)" % a["eventos"]
        elif a["selo"] == "estimado":
            painel = "cerca de %d eventos (estimado)" % a["eventos"]
        else:
            painel = "%d eventos" % a["eventos"]
        print("%-16s %-9s %s" % (nome, a["selo"], painel))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "sinais-exemplo.json")
