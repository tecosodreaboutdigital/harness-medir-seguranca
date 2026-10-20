# Histórico de versões

As versões seguem o formato `vX.Y`. Cada versão diz o que entrou, o que mudou e de onde veio a mudança.

## v0.2 · outubro de 2026 · Primeira expansão da comunidade

Primeira expansão depois do lançamento: o conteúdo ganha um site em três idiomas e passa a poder ser carregado por agentes de IA, sempre com o harness escrito junto. Por Teco Sodré, WeSAFER e AVANTIA.

Entrou:

- `docs/`: site para o GitHub Pages (servido de `main/docs`), em português (`docs/`), inglês (`docs/en/`) e espanhol (`docs/es/`). Página inicial, uma página por passo do ciclo, uma de modelos e uma de skills por idioma. Texto reescrito no tom da central de monitoramento, não traduzido ao pé da letra. HTML e CSS estáticos, sem JavaScript, legível no celular a partir de 360 px; só as fontes IBM Plex vêm do Google Fonts, com fonte do sistema como reserva. Favicon em SVG e imagem de compartilhamento (Open Graph).
- Terminologia fixa nos três idiomas: nível de controle / control level / nivel de control; Trava / Lock / Bloqueo.
- `skills/`: sete skills no formato aberto Agent Skills, cada uma com a seção de harness obrigatória (pode, nunca, quem confirma) e resumo em inglês no topo:
  - `mapear-camera`: entrevista e contrato de tarefa com nível de controle e a linha da tabela que o definiu;
  - `triagem-de-alerta`: o prompt com harness, no formato A a E, sem recomendar ação difícil de desfazer sem confirmação humana;
  - `revisar-nivel-de-controle`: auditoria de uma operação já ligada, com lacunas por gravidade;
  - `integracao-vms`: alertas do sistema de gravação por eventos ONVIF, REST ou webhook, somente leitura, com payload, mensagem ONVIF fictícia e servidor mock em Python (só biblioteca padrão) com HMAC, janela contra replay, limite de taxa e minimização;
  - `integracao-controle-de-acesso`: webhook somente leitura de controle de acesso e RH, com payloads e notas de LGPD para biometria (dado sensível, art. 11, retenção, registro, segurança);
  - `saude-da-operacao`: sinais de Zabbix, SNMP, ping e HTTP alimentando o selo de integridade do dado (íntegro, estimado, atrasado, sem dado), com script de exemplo;
  - `mcp-central`: desenho de servidor MCP com três ferramentas mínimas e o harness em volta de cada uma.
- Revisão de segurança em toda skill de integração: autenticação, menor privilégio, somente leitura por padrão, segredos fora do repositório, log sem dado pessoal, limite de taxa e proteção contra replay com HMAC e timestamp.
- `README.en.md` e `README.es.md`; `README.md` com links para o site, as skills e os outros idiomas.

Mudou:

- `CONTRIBUTING.md`: nova seção "Uma skill", com a seção de harness obrigatória e a revisão de segurança para integrações; regras para traduções.

## v0.1 · 21/10/2026 · Lançamento na SegSummit

Versão inicial, lançada na Oficina Prática de IA na Segurança (SegSummit, 21 de outubro de 2026), por Teco Sodré, WeSAFER e AVANTIA. Conteúdo semente: o kit de apoio da oficina, adaptado do [harness-medir](https://github.com/tecosodreaboutdigital/harness-medir).

Entrou:

- `README.md`: o que é o projeto, derivação do harness-medir, ciclo MEDIR no CFTV, nível de controle em resumo, como começar em 15 minutos.
- `medir/`: um arquivo por passo do ciclo (Mapear, Equipar, Delegar, Inspecionar, Reforçar), com propósito, perguntas, saídas, exemplos e antipadrões.
- `modelos/contrato-de-tarefa.md`: contrato de uma página para uma câmera, um evento e uma decisão, com exemplo preenchido.
- `modelos/nivel-de-controle.md`: N1, N2, N3 e Trava aplicados em ordem, as quatro perguntas e a matriz de ações por reversibilidade.
- `modelos/prompt-com-harness.md`: prompt A (modelo puro) e prompt B (modelo + harness), e como rodar o lado a lado.
- `modelos/checklist-antes-de-ligar.md`: os dez itens antes de ligar um analítico novo, com como comprovar cada um.
- `modelos/sensores.md`: cinco sensores e o registro mínimo de cada alerta.
- `casos/`: modelo de caso com checklist de anonimização e quatro casos de exemplo em nível de setor.
- `CONTRIBUTING.md`: fluxo por issue ou pull request, regras de anonimização e de escrita.
- `LICENSE`: CC BY 4.0.

As próximas versões saem das contribuições da comunidade.
