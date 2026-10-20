# Skills

> **English summary.** Seven agent skills in the open [Agent Skills](https://agentskills.io) format (one folder per skill, each with a `SKILL.md` that has YAML frontmatter `name` and `description`). They apply the MEDIR harness to security operations: map a camera, triage an alert, audit control levels, integrate a VMS, access control and infrastructure health in read-only mode, and design an MCP server for a monitoring center. Instructions are in Portuguese, with a short English summary at the top of each file. Every skill has a mandatory harness section: what it may do, what it must never do, and who confirms.

Skills no formato aberto Agent Skills: uma pasta por skill, com um `SKILL.md` que começa com `name` e `description` em YAML. Qualquer agente que leia esse formato pode carregá-las. As instruções estão em português, com um resumo curto em inglês no topo de cada arquivo.

Uma skill não é um atalho para dar mais poder ao agente. É o harness escrito de um jeito que o agente consegue seguir: o que ele pode fazer, o que nunca faz e quem confirma.

## Catálogo

| Skill | Passo MEDIR | O que entrega |
|---|---|---|
| [mapear-camera](mapear-camera/SKILL.md) | Mapear | Entrevista sobre uma câmera, um evento e uma decisão; devolve o contrato de tarefa preenchido e o nível de controle com a linha da tabela que o definiu |
| [triagem-de-alerta](triagem-de-alerta/SKILL.md) | Equipar | Aplica o prompt com harness a um alerta e responde no formato de 1 a 6, começando pelo quadro visual de 3 passos, sem nunca recomendar ação difícil de desfazer sem confirmação humana |
| [revisar-nivel-de-controle](revisar-nivel-de-controle/SKILL.md) | Delegar | Audita uma operação com analíticos já ligados contra a tabela e o checklist, e lista as lacunas |
| [integracao-vms](integracao-vms/SKILL.md) | Equipar | Guia para receber alertas de um sistema de gravação por eventos ONVIF, REST ou webhook, em somente leitura, com payload e servidor mock |
| [integracao-controle-de-acesso](integracao-controle-de-acesso/SKILL.md) | Equipar | Webhook somente leitura para eventos de controle de acesso e RH (credencial revogada, desligamento), com notas de LGPD para biometria |
| [saude-da-operacao](saude-da-operacao/SKILL.md) | Inspecionar | Sinais de saúde (Zabbix, SNMP, ping, HTTP) alimentando o selo de integridade do dado: íntegro, estimado, atrasado, sem dado |
| [mcp-central](mcp-central/SKILL.md) | Equipar, Delegar | Documento de desenho de um servidor MCP para uma central, com três ferramentas mínimas e o harness em volta de cada uma |

## Como instalar

Copie a pasta da skill para o diretório de skills do seu agente. Exemplos comuns:

- Claude Code: `.claude/skills/<nome>/` no projeto, ou `~/.claude/skills/<nome>/` para todos os projetos.
- Outros agentes compatíveis com Agent Skills: consulte a documentação do agente para o caminho de skills.

Leia o `SKILL.md` inteiro antes de instalar. Uma skill que você não leu é uma instrução que você não conhece rodando dentro do seu agente.

## Regras comuns a todas as skills

1. **Alerta é hipótese.** Nenhuma skill trata confiança de modelo como prova.
2. **O operador confirma.** Nenhuma skill executa, ou recomenda executar, ação difícil de desfazer sem confirmação humana no vídeo; em N3, outra pessoa autoriza.
3. **Trava passa por cima de tudo.** Sem jeito de conferir o alerta, nada é delegado.
4. **Somente leitura por padrão.** Integrações leem; escrever em sistema de terceiro exige decisão explícita, registrada, e sobe o nível de controle.
5. **Sem dado real em exemplo.** Hosts `exemplo.local`, segredos de teste lidos de variável de ambiente, nenhum IP, credencial, rosto, placa ou nome de pessoa real.
6. **Sem fornecedor.** Protocolos e ferramentas abertas (ONVIF, RTSP, REST, webhooks, Zabbix, MCP) sim; nomes comerciais de sistemas de gravação, analíticos ou reconhecimento facial, não.

Para contribuir com uma skill nova, veja a seção "Uma skill" do [CONTRIBUTING.md](../CONTRIBUTING.md#uma-skill).
