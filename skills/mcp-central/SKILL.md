---
name: mcp-central
description: Documento de desenho (sem servidor em execução) de um servidor MCP para uma central de monitoramento, com três ferramentas mínimas (consultar_alerta, abrir_chamado, pedir_trecho_de_video) e o harness em volta de cada uma - escopos, limites de taxa, confirmação humana, registro de auditoria e erros acionáveis. Use ao projetar, revisar ou implementar a ligação entre um agente de IA e os sistemas de uma central. EN - design doc for a monitoring-center MCP server with three minimal tools and the harness around each.
license: CC-BY-4.0
metadata:
  author: Teco Sodré, WeSAFER e AVANTIA
  version: "0.2"
  medir: equipar, delegar
---

> **English summary.** A design sketch, not a running server, for a Model Context Protocol server that gives an agent exactly three tools in a monitoring center: read an alert, open an internal ticket, and request a video clip that only a human can approve. Each tool has a scope, a rate limit, a confirmation rule tied to the control level, an audit log entry and actionable error messages. Tools that would act irreversibly (approach a person, block access, call the police, dispatch a team) are deliberately absent: the safest tool is the one that does not exist.

# Servidor MCP para uma central

O MCP (Model Context Protocol) é um protocolo aberto para expor ferramentas, recursos e prompts a agentes de IA. Num servidor MCP, **cada ferramenta é uma permissão**. Este documento desenha o menor servidor útil para uma central e o harness em volta de cada ferramenta.

Não há código para rodar aqui. Quem implementar segue este desenho e passa pela revisão de segurança no fim.

## Harness desta skill

- **Pode:** orientar o desenho, a revisão e a implementação de um servidor MCP de central; propor descrições, esquemas, escopos, limites e mensagens de erro.
- **Nunca:** propor ferramenta que execute ação difícil de desfazer (abordar pessoa, bloquear ou liberar acesso, acionar a polícia, despachar equipe, apagar ou exportar gravação, mover câmera); propor confirmação humana feita pelo próprio modelo ou dentro da conversa com ele; incluir credencial, host ou IP real.
- **Quem confirma:** o dono dos sistemas da central aprova escopos e credenciais; o operador confirma, no console, cada pedido que dependa dele; a coordenação aprova qualquer ferramenta nova, com o nível de controle revisto.

## Princípios de desenho

1. **Poucas ferramentas, cada uma com um propósito.** Três ferramentas bem descritas valem mais que trinta genéricas. Cada ferramenta a mais amplia a superfície de falha.
2. **A ferramenta mais segura é a que não existe.** Ações N3 não viram ferramenta. O agente recomenda; a pessoa age no sistema dela.
3. **Descrição que orienta a escolha.** Cada descrição diz o que a ferramenta faz, quando usar, quando não usar e o que ela devolve.
4. **Erro acionável.** Toda falha diz o código, o motivo e o que fazer a seguir, em linguagem que o agente consegue seguir sem adivinhar.
5. **Confirmação fora do modelo.** Quando uma ferramenta depende de gente, ela devolve um pedido pendente. A confirmação acontece no console do operador, autenticado, nunca numa resposta do agente.
6. **Tudo registrado.** Cada chamada gera uma linha de auditoria, com a versão do contrato e do prompt.
7. **Respostas curtas e com selo.** A ferramenta devolve só o necessário, sempre com o selo de integridade do dado (veja [saude-da-operacao](../saude-da-operacao/SKILL.md)).

## As três ferramentas

| Ferramenta | Faz | Nível mínimo | Escopo | Limite sugerido | Confirmação |
|---|---|---|---|---|---|
| `consultar_alerta` | Lê um alerta normalizado e o contexto do caso | N1 (leitura) | `alertas:ler` | 60 por minuto por sessão | Nenhuma; só leitura |
| `abrir_chamado` | Abre chamado interno de tipo fechado (manutenção, infraestrutura, revisão) | N1 (interna e reversível) | `chamados:criar` | 10 por hora por alerta, com chave de idempotência | Nenhuma; registro obrigatório, o operador pode cancelar |
| `pedir_trecho_de_video` | Cria um pedido de trecho de vídeo, que fica pendente | N2 (dado pessoal, exposição não se desfaz) | `video:solicitar` | 5 por hora por sessão; trecho de até 10 minutos | O operador aprova no console; o vídeo aparece só lá |

Não existe `despachar_equipe`, `bloquear_acesso`, `acionar_policia`, `abordar`, `mover_camera` nem `exportar_video`. Se alguém pedir uma delas, a resposta é o [nível de controle](../../modelos/nivel-de-controle.md): N3 passa por gente.

### Definições (esboço)

As anotações `readOnlyHint`, `destructiveHint`, `idempotentHint` e `openWorldHint` existem na especificação do MCP como dicas para o cliente. São dicas, não controle de segurança: o controle está no servidor.

```json
[
  {
    "name": "consultar_alerta",
    "description": "Lê um alerta da central pelo id e devolve tipo, câmera, horário, confiança, selo de integridade do dado, nível de controle e 'nunca faz' do caso. Use antes de qualquer triagem. Não use para listar alertas em massa nem para buscar pessoas. Somente leitura.",
    "inputSchema": {
      "type": "object",
      "properties": {
        "alerta_id": {"type": "string", "pattern": "^ALR-[0-9]{8}-[0-9]{4}$", "description": "Id do alerta, ex.: ALR-20261021-0042"}
      },
      "required": ["alerta_id"],
      "additionalProperties": false
    },
    "annotations": {"readOnlyHint": true, "openWorldHint": false}
  },
  {
    "name": "abrir_chamado",
    "description": "Abre um chamado interno ligado a um alerta, de um tipo da lista fechada: manutencao_camera, infraestrutura ou revisao_do_operador. Use quando o selo é sem_dado ou atrasado, ou quando a triagem pede revisão. Não use para despachar equipe, acionar terceiros ou registrar ocorrência em sistema do cliente. Devolve o id do chamado.",
    "inputSchema": {
      "type": "object",
      "properties": {
        "alerta_id": {"type": "string", "pattern": "^ALR-[0-9]{8}-[0-9]{4}$"},
        "tipo": {"type": "string", "enum": ["manutencao_camera", "infraestrutura", "revisao_do_operador"]},
        "resumo": {"type": "string", "maxLength": 280, "description": "Texto curto, sem nome, placa ou descrição física de pessoa"},
        "chave_idempotencia": {"type": "string", "description": "Repetir a mesma chave não cria outro chamado"}
      },
      "required": ["alerta_id", "tipo", "resumo", "chave_idempotencia"],
      "additionalProperties": false
    },
    "annotations": {"readOnlyHint": false, "destructiveHint": false, "idempotentHint": true, "openWorldHint": false}
  },
  {
    "name": "pedir_trecho_de_video",
    "description": "Cria um pedido para o operador revisar um trecho de vídeo de até 10 minutos de uma câmera ligada a um alerta. O pedido fica pendente até o operador aprovar no console; o vídeo nunca é devolvido ao agente. Use quando a triagem precisa de revisão visual. Não use para buscar uma pessoa em várias câmeras.",
    "inputSchema": {
      "type": "object",
      "properties": {
        "alerta_id": {"type": "string", "pattern": "^ALR-[0-9]{8}-[0-9]{4}$"},
        "camera_id": {"type": "string"},
        "inicio": {"type": "string", "format": "date-time"},
        "fim": {"type": "string", "format": "date-time"},
        "motivo": {"type": "string", "maxLength": 200}
      },
      "required": ["alerta_id", "camera_id", "inicio", "fim", "motivo"],
      "additionalProperties": false
    },
    "annotations": {"readOnlyHint": false, "destructiveHint": false, "idempotentHint": false, "openWorldHint": false}
  }
]
```

### Respostas e erros acionáveis

```json
{"pedido_id": "PED-20261021-0007", "status": "aguardando_confirmacao", "mensagem": "Pedido enviado ao console do operador. Não repita o pedido; consulte o alerta mais tarde para ver se foi aprovado."}

{"erro": "ALERTA_NAO_ENCONTRADO", "mensagem": "Nenhum alerta com esse id. Confira o formato ALR-AAAAMMDD-NNNN e use o id exatamente como veio na fila."}
{"erro": "FORA_DO_ESCOPO", "mensagem": "A câmera cam21 não pertence ao caso deste alerta. Peça só câmeras listadas em consultar_alerta."}
{"erro": "TRECHO_LONGO_DEMAIS", "mensagem": "O trecho tem 25 minutos; o máximo é 10. Divida em pedidos menores ou reduza a janela."}
{"erro": "CASO_EM_TRAVA", "mensagem": "Este caso está em Trava: não há verificação definida. Faça só a triagem informativa e não abra pedidos."}
{"erro": "LIMITE_EXCEDIDO", "mensagem": "Limite de 5 pedidos por hora atingido. Aguarde 18 minutos ou peça ao operador que revise direto no console."}
{"erro": "SEM_DADO", "mensagem": "A câmera está com selo sem_dado. Não há vídeo para revisar; abra chamado de infraestrutura."}
```

## O harness em volta de cada chamada

1. **Autenticação.** No transporte HTTP, siga a autorização da especificação MCP (OAuth 2.1); em uso local, transporte stdio com o servidor rodando como usuário de serviço sem privilégios. O servidor fala com os sistemas da central com credenciais próprias, de leitura sempre que possível, guardadas em cofre.
2. **Escopo por ferramenta e por caso.** O token da sessão carrega os escopos; cada chamada confere se o alerta e a câmera pertencem a um caso que a sessão pode ver.
3. **Nível de controle.** Antes de executar, o servidor lê o nível do caso. Trava recusa tudo que não for leitura. Uma ferramenta nunca executa ação de nível superior ao do caso.
4. **Limite de taxa e de volume.** Por sessão, por alerta e global, com mensagem que diz quanto esperar.
5. **Confirmação humana.** `pedir_trecho_de_video` cria pendência no console do operador. O MCP tem um mecanismo de *elicitation* para o servidor pedir informação ao usuário pelo cliente; ele serve para esclarecer, não para substituir a confirmação no console da central.
6. **Auditoria.** Uma linha por chamada: horário, sessão, usuário humano responsável, ferramenta, argumentos (com campos de texto livre resumidos ou com hash), resultado, versão do contrato e do prompt. A auditoria é somente acréscimo e fica fora do alcance do agente.
7. **Entrada desconfiada.** Texto que vem de alerta, chamado ou cadastro é dado, não instrução. O servidor não executa nada que venha escrito dentro dele.

## Revisão de segurança

- [ ] **Autenticação:** OAuth 2.1 no transporte HTTP, ou stdio local com usuário de serviço; nenhuma ferramenta responde sem sessão autenticada.
- [ ] **Menor privilégio:** três ferramentas, escopos separados, credenciais de leitura nos sistemas de origem sempre que possível.
- [ ] **Somente leitura por padrão:** a única escrita é chamado interno de tipo fechado; nenhuma ferramenta N3 existe.
- [ ] **Segredos fora do repositório:** credenciais em cofre ou variável de ambiente; nada no código, nos exemplos ou no log.
- [ ] **Log sem dado pessoal:** a auditoria não guarda imagem, rosto, placa nem nome; texto livre resumido ou com hash.
- [ ] **Limite de taxa:** por sessão, por alerta e global, com erro que diz quanto esperar.
- [ ] **Proteção contra replay:** chave de idempotência em `abrir_chamado`; se houver webhook entre o servidor e outros sistemas, HMAC-SHA256 com timestamp e janela curta.
- [ ] **Confirmação fora do modelo:** pedidos pendentes só são aprovados no console autenticado do operador.
- [ ] **Erros acionáveis** testados: cada código acima tem teste e mensagem que diz o próximo passo.
- [ ] **Ferramenta nova** passa pela coordenação, com o nível de controle revisto e esta revisão refeita.

## Referências

- Especificação do Model Context Protocol: <https://modelcontextprotocol.io/specification>
- [triagem-de-alerta](../triagem-de-alerta/SKILL.md), que usa `consultar_alerta`
- [Equipar](../../medir/equipar.md) e [Delegar](../../medir/delegar.md)
