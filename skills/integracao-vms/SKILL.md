---
name: integracao-vms
description: Guia e modelo para levar o fluxo de alertas de um sistema de gravação (VMS) até o assistente da central por eventos ONVIF, REST ou webhook genérico, em somente leitura por padrão, com payload de exemplo, servidor mock em Python (só biblioteca padrão) e revisão de segurança. Use ao planejar, revisar ou testar a integração entre gravação ou analítico e um agente de triagem. EN - read-only guide to integrate a VMS alert stream via ONVIF events or REST/webhook, with mock payload and stdlib mock server.
license: CC-BY-4.0
metadata:
  author: Teco Sodré, WeSAFER e AVANTIA
  version: "0.2"
  medir: equipar
---

> **English summary.** A read-only integration pattern: VMS events (ONVIF event service with PullPoint subscription, a generic REST endpoint polled with a read-only token, or a signed webhook) are received by a small adapter that verifies HMAC + timestamp, rejects replays, keeps only an allowlist of fields, logs without personal data and normalizes each event for the triage skill. There is no path back to the VMS. Includes a fictitious ONVIF message, a webhook payload, a Python stdlib mock server and sender, and a security review checklist.

# Integração com sistema de gravação

O assistente só ajuda o operador se o alerta chegar até ele com contexto e sem atraso. Esta skill desenha esse caminho de um jeito que **lê e nunca comanda**.

## Quando usar

- Planejar como os alertas do sistema de gravação ou do analítico chegam a um agente de triagem.
- Revisar uma integração existente antes de ligar o assistente.
- Testar localmente o padrão com os arquivos de [exemplos/](exemplos/).

## Harness desta skill

- **Pode:** receber eventos, conferir assinatura e horário, normalizar, descartar campos fora da lista, guardar o evento para leitura do assistente, consultar metadados em leitura (lista de câmeras, estado de gravação).
- **Nunca:** mover câmera (PTZ), apagar ou exportar gravação, mudar regras do analítico, armar ou desarmar zonas, abrir portão, gravar qualquer coisa no sistema de gravação; guardar credenciais no repositório; enviar imagem ou rosto para serviço externo sem base legal e aprovação registradas; passar link de vídeo ao modelo.
- **Quem confirma:** o dono do sistema de gravação (normalmente a TI ou a engenharia da central) aprova a credencial e o escopo. O operador confirma qualquer ação que nasça de um alerta. Escrever no sistema de gravação é decisão à parte, registrada, e sobe o nível de controle do caso.

## Arquitetura

```
sistema de gravação ──(ONVIF PullPoint | REST com token de leitura | webhook assinado)──▶
  adaptador (somente leitura) ──▶ fila de alertas normalizados ──▶ triagem-de-alerta ──▶ console do operador
                                                                                    (sem caminho de volta)
```

O vídeo não passa pelo modelo. O alerta leva só uma `referencia_video` opaca; quem abre o trecho é o operador, no console. Se um agente precisar pedir um trecho, use o desenho de [mcp-central](../mcp-central/SKILL.md), em que o pedido depende de confirmação humana.

## Três jeitos de receber o alerta

| Jeito | Quando | Cuidados |
|---|---|---|
| **Eventos ONVIF** (serviço de eventos, assinatura PullPoint com `CreatePullPointSubscription` e `PullMessages`) | A câmera ou o gravador expõe eventos ONVIF; analíticos costumam vir em tópicos de `tns1:RuleEngine/...` | Usuário ONVIF com o menor nível que permita ler eventos; renovar a assinatura antes de expirar; tratar "sem mensagens" diferente de "assinatura caiu" |
| **REST, por consulta** | O sistema oferece uma API de eventos | Token só de leitura, com escopo restrito às câmeras do caso; paginação; espera crescente entre tentativas; registrar o último evento lido para não perder nem repetir |
| **Webhook** | O sistema empurra eventos para uma URL | HTTPS; assinatura HMAC-SHA256 com timestamp; janela contra replay; recusa de id repetido; limite de taxa; só aceitar de origens conhecidas |

Qualquer que seja o jeito, o adaptador converte para o mesmo formato normalizado:

| Campo normalizado | ONVIF (exemplo) | Observação |
|---|---|---|
| `camera_id` | `SimpleItem VideoSourceConfigurationToken` | identificador técnico, nunca o nome do local |
| `tipo` | tópico, ex.: `tns1:RuleEngine/FieldDetector/ObjectsInside` | traduzido para um tipo do contrato, ex.: `invasao_de_perimetro` |
| `regra` | `SimpleItem Rule` | |
| `ocorrido_em` | atributo `UtcTime` | sempre UTC; o relógio do emissor precisa de NTP |
| `confianca` | quando o analítico informa | ausente é ausente, nunca 100% |
| `referencia_video` | gerada pelo adaptador | opaca; o vídeo fica no console |
| `selo` | vem de [saude-da-operacao](../saude-da-operacao/SKILL.md) | `integro`, `estimado`, `atrasado` ou `sem_dado` |

## Testar localmente

Os arquivos de [exemplos/](exemplos/) usam só a biblioteca padrão do Python e escutam apenas em `localhost`:

```
cd exemplos
export MOCK_WEBHOOK_SEGREDO="segredo-de-teste-local"     # Windows PowerShell: $env:MOCK_WEBHOOK_SEGREDO="..."
python servidor_mock.py --porta 8088
# em outro terminal, com a mesma variável:
python enviar_alerta_mock.py alerta-webhook.json             # 202, e o campo extra é descartado
python enviar_alerta_mock.py alerta-webhook.json --repetir   # 202 e depois 409 (replay)
python enviar_alerta_mock.py alerta-webhook.json --atrasado  # 401 (fora da janela)
curl http://localhost:8088/alertas                           # o que o assistente lê
```

[evento-onvif.xml](exemplos/evento-onvif.xml) mostra uma resposta `PullMessages` fictícia, e [alerta-webhook.json](exemplos/alerta-webhook.json) é o mesmo evento já no formato de webhook.

## Revisão de segurança

Marque cada item antes de ligar em operação. Um "não" é pendência com dono.

- [ ] **Autenticação:** todo canal autentica (usuário ONVIF próprio, token de API ou assinatura HMAC); nada aceita requisição anônima.
- [ ] **Menor privilégio:** a credencial lê só eventos e metadados das câmeras do caso; não tem permissão de PTZ, exportação, exclusão ou configuração.
- [ ] **Somente leitura por padrão:** não existe rota, função ou ferramenta que escreva no sistema de gravação; qualquer exceção está registrada no contrato, com nível revisto.
- [ ] **Segredos fora do repositório:** segredos e tokens vêm de variável de ambiente ou cofre de segredos; nenhum segredo em código, exemplo, issue ou log; rotação definida.
- [ ] **Log sem dado pessoal:** o log guarda id, tipo, origem, horário e resultado; nunca imagem, rosto, placa, nome ou corpo completo do evento.
- [ ] **Limite de taxa e tamanho:** o adaptador limita requisições por origem e o tamanho do corpo, e responde com erro claro.
- [ ] **Proteção contra replay:** webhook assinado com HMAC-SHA256 sobre timestamp e corpo, janela curta (ex.: 300 s), recusa de `evento_id` repetido, relógios com NTP.
- [ ] **Transporte:** HTTPS ou rede isolada entre o emissor e o adaptador; o adaptador não fica exposto à internet.
- [ ] **Minimização:** só campos de uma lista fechada seguem para o assistente.
- [ ] **Falha visível:** assinatura ONVIF expirada, API fora do ar ou webhook silencioso geram alerta de infraestrutura, nunca "nenhum evento".

## Referências

- ONVIF, especificações e perfis (eventos, Profile S, Profile M para metadados de analíticos): <https://www.onvif.org/profiles/>
- [Equipar](../../medir/equipar.md) e [sensores](../../modelos/sensores.md)
