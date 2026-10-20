# Histórico de versões

As versões seguem o formato `vX.Y`. Cada versão diz o que entrou, o que mudou e de onde veio a mudança.

## v0.2.2 · outubro de 2026 · Tema claro por padrão e botão sol/lua

Pedido de Teco Sodré para o site.

Mudou:

- **Tema claro por padrão** em todas as 24 páginas: fundo quase branco, cartões brancos, texto azul-marinho escuro e âmbar escurecido (#8a5a00) quando o âmbar é texto; fundos âmbar continuam #fab219 com texto escuro. O tema escuro anterior foi mantido igual.
- **Botão sol/lua** na barra superior de toda página (38 px, com `aria-label` e `aria-pressed` em cada idioma, acessível pelo teclado e com foco visível). A escolha é manual e fica guardada no navegador (`localStorage`, chave `hms:tema`, valores `claro` e `escuro`); o site nunca segue o tema do sistema operacional. Um script mínimo no `<head>` aplica a escolha antes da pintura da página, sem piscar. Sem JavaScript, a página fica no tema claro, inteiramente legível, e o botão não aparece.
- Contraste conferido nos dois temas: todos os pares de texto e fundo passam no nível AA da WCAG (menor razão 5,13:1 no claro e 5,30:1 no escuro).

Corrigido:

- Na trilha dos cinco passos, em telas largas, o nome de cada passo aparecia dentro de uma caixa extra.

## v0.2.1 · outubro de 2026 · Comunidade A.I.S., origem explícita e prévias de compartilhamento

Ajustes decididos por Teco Sodré antes da publicação da v0.2.

Entrou:

- **Comunidade A.I.S.** A comunidade do projeto passa a ter nome: "A.I.S. 🚀 Agentes de IA = Modelo + Harness para Segurança Eletrônica, Monitoramento e Produtividade", no WhatsApp, para quem opera, regula, audita ou constrói soluções digitais inteligentes. Seção própria, com o símbolo e o link de convite, nos três README e na página inicial do site em cada idioma; menções antigas à "comunidade da oficina" substituídas.
- **Origem explícita.** "Derivado do harness MEDIR, de Teco Sodré", com link para o repositório e para o site de origem, no topo dos três README, no início da página inicial e no rodapé de todas as páginas do site.
- **Prévia de compartilhamento.** Nova imagem Open Graph `docs/assets/og.jpg` (1200x630, JPEG progressivo, cerca de 85 KB), gerada a partir de `docs/assets/og-fonte.html`, com o símbolo da comunidade. Todas as páginas declaram `og:image` com URL absoluta, tipo, tamanho, texto alternativo e `og:locale` por idioma (pt_BR, en_US, es_ES), e `twitter:card` grande.
- **Ícones.** `favicon.ico` (16, 32 e 48 px) e `apple-touch-icon.png` (180 px), além do `favicon.svg`, declarados em todas as páginas.
- `docs/assets/ais.png`: símbolo da comunidade, otimizado (256 px).

Saiu:

- `docs/assets/og.png`, substituída por `og.jpg`.

Mudou:

- `CONTRIBUTING.md`: a comunidade A.I.S. aparece pelo nome, e quem não usa GitHub tem o link do grupo.

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
