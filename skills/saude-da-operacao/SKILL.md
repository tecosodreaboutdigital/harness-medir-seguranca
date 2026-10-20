---
name: saude-da-operacao
description: Liga sinais de saúde da infraestrutura (Zabbix, SNMP, ping, HTTP, estado de gravação, relógio) a um selo de integridade do dado com quatro estados (íntegro, estimado, atrasado, sem dado), para que falha de câmera, rede ou servidor nunca apareça como "nada aconteceu". Use ao montar painéis, sensores ou a triagem de uma central que depende de câmeras e analíticos. EN - maps infrastructure health signals to a data integrity seal so an infrastructure failure never shows as "nothing happened".
license: CC-BY-4.0
metadata:
  author: Teco Sodré, WeSAFER e AVANTIA
  version: "0.2"
  medir: inspecionar
---

> **English summary.** Health signals (Zabbix problems and items, SNMP, ICMP ping, HTTP checks, recording status, clock drift) feed a data integrity seal attached to every number and alert: intact (íntegro), estimated (estimado), late (atrasado) or no data (sem dado). The worst seal wins when aggregating, an area shows "0 events" only when every camera in it is intact, and "no data" in an N2 or N3 case raises an infrastructure alert to the operator immediately. Read-only Zabbix API access, a stdlib example script and a security review checklist are included.

# Saúde da operação

Às 3 da manhã, uma câmera caída e uma área tranquila mostram a mesma coisa: nenhum alerta. Esta skill dá nome à diferença. Todo número e todo alerta carregam um **selo de integridade do dado**.

## Quando usar

- Montar o painel da central ou do comando com contagens e alertas.
- Ligar o sensor de falha de infraestrutura (item 8 do checklist antes de ligar).
- Alimentar a [triagem-de-alerta](../triagem-de-alerta/SKILL.md) com o estado da câmera.

## Harness desta skill

- **Pode:** ler sinais de saúde em somente leitura, calcular o selo, marcar números e áreas, gerar alerta de infraestrutura para o operador, abrir chamado interno de manutenção (N1, com registro).
- **Nunca:** reiniciar equipamento, mudar configuração do monitoramento ou da rede, silenciar ou reconhecer problema no lugar de uma pessoa, mostrar zero onde não há dado, esconder o selo para "limpar" o painel.
- **Quem confirma:** o operador recebe o alerta de infraestrutura e decide o encaminhamento; a manutenção ou a TI confirma a causa e o reparo. Ação corretiva em equipamento é feita por gente.

## Os quatro selos

| Selo | Quando | Como aparece |
|---|---|---|
| **íntegro** | Imagem válida, gravação ativa, dado dentro da janela, relógio sincronizado | O número aparece normalmente, inclusive zero |
| **estimado** | Parte do dado faltou e o valor foi completado por estimativa ou por fonte secundária (ex.: contagem de uma câmera fora estimada pela vizinha) | "cerca de N", com a marca de estimado |
| **atrasado** | O dado chegou, mas fora da janela combinada, ou o relógio do equipamento está fora de sincronia | O último valor, com o horário dele e a marca de atrasado |
| **sem dado** | Sem rede, sem gravação ou sem imagem | "sem visão", nunca zero; alerta de infraestrutura |

Regras:

1. **Falha de infraestrutura nunca aparece como "nada aconteceu".**
2. **O pior selo vence** ao agregar: área com uma câmera `sem dado` é área `sem dado`.
3. **Zero só com selo íntegro.** "0 eventos" exige todas as câmeras da área íntegras.
4. **N2 e N3 alertam na hora.** Câmera de caso em N2 ou N3 com selo `sem dado` gera alerta de infraestrutura imediato para o operador.
5. **O selo viaja com o dado.** Alerta, relatório e painel levam o selo; quem resume não pode tirá-lo.

## De onde vêm os sinais

| Sinal | Ferramenta aberta | Leva a |
|---|---|---|
| Câmera ou gravador responde na rede | ping ICMP (no Zabbix, item `icmpping`) | `sem dado` se falhar |
| Interface de rede, porta do switch, energia | SNMP, por item do Zabbix | `sem dado` ou causa provável |
| Serviço do sistema de gravação no ar | verificação HTTP (item HTTP agent ou cenário web do Zabbix) | `sem dado` se falhar |
| Último quadro e estado de gravação | metadados do sistema de gravação, em leitura (veja [integracao-vms](../integracao-vms/SKILL.md)) | `atrasado` ou `sem dado` |
| Dado parou de chegar | gatilho de ausência de dado, como a função `nodata()` do Zabbix | `atrasado`, depois `sem dado` |
| Relógio | deriva em relação ao NTP | `atrasado` se passar do limite |

**Zabbix em somente leitura.** Use a API JSON-RPC (ex.: `https://zabbix.exemplo.local/api_jsonrpc.php`) com um token de API de um usuário cujo papel só tem leitura e só enxerga os grupos de hosts da central. Métodos de leitura como `problem.get`, `host.get` e `item.get` bastam. Se preferir empurrar, configure um tipo de mídia webhook apontando para o adaptador, com o mesmo cuidado de assinatura e janela da skill de gravação.

## Exemplo

[exemplos/calcular_selo.py](exemplos/calcular_selo.py) lê [exemplos/sinais-exemplo.json](exemplos/sinais-exemplo.json) e mostra o selo por câmera e por área:

```
python exemplos/calcular_selo.py exemplos/sinais-exemplo.json

perimetro-leste  atrasado  1 eventos até o último dado recebido (atrasado)
doca             sem_dado  SEM VISÃO: alerta de infraestrutura para o operador
acesso-norte     estimado  cerca de 4 eventos (estimado)
```

Repare na doca: ela tem zero eventos, e o painel não diz zero. Diz "sem visão".

## Revisão de segurança

- [ ] **Autenticação:** token de API ou assinatura em todo canal; nada anônimo.
- [ ] **Menor privilégio:** o usuário da API só lê, e só os grupos de hosts da central; não reconhece problema, não executa script, não muda configuração.
- [ ] **Somente leitura por padrão:** a skill não reinicia nem reconfigura nada; ação corretiva é chamado para uma pessoa.
- [ ] **Segredos fora do repositório:** token em variável de ambiente ou cofre, com validade e rotação.
- [ ] **Log sem dado pessoal:** sinais de saúde não precisam de imagem nem de pessoa; o log guarda host, item, selo e horário.
- [ ] **Limite de taxa:** consultas à API com intervalo mínimo e espera crescente em erro, para o painel não derrubar o monitoramento.
- [ ] **Proteção contra replay:** se usar webhook, HMAC-SHA256 com timestamp, janela curta e recusa de id repetido.
- [ ] **O monitor também falha:** se a própria fonte de saúde cair, tudo o que depende dela vira `sem dado`, nunca `íntegro`.

## Referências

- [Sensores](../../modelos/sensores.md), em especial "falha de infraestrutura"
- Documentação da API do Zabbix: <https://www.zabbix.com/documentation/current/en/manual/api>
