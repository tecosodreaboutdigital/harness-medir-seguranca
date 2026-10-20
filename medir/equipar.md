# E · Equipar

**O que o modelo precisa saber e poder fazer?**

## Propósito

Dar ao modelo o contexto e as ferramentas mínimas para ajudar o operador a decidir, e nada além disso. Equipar é escrever o harness: papel, protocolo, nível de controle, formato da resposta e o que o modelo não sabe.

A regra de dimensionamento vale aqui mais do que em qualquer outro passo: **o harness precisa ser menor que a superfície de falha que ele controla.** Cada ferramenta a mais é um jeito a mais de errar.

## Perguntas

1. Qual é o papel do modelo nesta central? (ele ajuda o operador a decidir; ele não decide)
2. Que trecho do protocolo da central se aplica a este evento?
3. Qual é o nível de controle e quem decide em cada etapa?
4. Em que formato o operador precisa da resposta, considerando que ele está cansado, sozinho e com outros alertas na fila?
5. Que ferramentas o modelo precisa de fato? Consultar o sistema de gravação? Abrir chamado? Alguma outra?
6. O que o modelo não sabe e precisa dizer que não sabe? (condição da câmera, quem está escalado, se a área estava liberada)
7. Onde ficam as decisões depois que a conversa acaba?

## Saídas

- O prompt com harness desta tarefa, versionado (veja [prompt-com-harness.md](../modelos/prompt-com-harness.md)).
- A lista fechada de ferramentas, cada uma com o que faz e como falha.
- O formato da resposta, com limite de tamanho.
- O lugar onde cada alerta, decisão e ação fica registrado (veja o [registro mínimo](../modelos/sensores.md#registro-mínimo-de-cada-alerta)).

## Exemplos no CFTV

- **Formato curto e fixo.** Hipótese mais provável e duas alternativas, incluindo falso positivo; o que verificar nos próximos 60 segundos; quem decide e quando escalar; o que registrar; o que não sabe. No máximo 120 palavras.
- **Ferramenta mínima em sites remotos de energia.** O modelo pode consultar o vídeo gravado dos últimos minutos e abrir um chamado vinculado ao alerta. Não pode liberar a chave digital do gabinete.
- **Ferramenta mínima em condomínio.** O modelo pode subir a câmera no mosaico e sugerir o texto da comunicação com a portaria. Quem fala com a portaria é o operador.
- **Contexto de turno.** Informar ao modelo quantos alertas o operador recebeu na última hora muda a resposta: com 38 alertas na fila, a recomendação precisa ser mais curta e mais seletiva.

## Antipadrões

- **Prompt sem papel.** "O que eu faço?" devolve uma resposta genérica, longa e segura de si. Compare no exercício A contra B.
- **Ferramenta demais.** Dar ao modelo acesso a controle de acesso, lista de alerta e cadastro de pessoas "porque pode ser útil" amplia a superfície de falha sem necessidade e sobe o nível de controle.
- **Harness que só existe na cabeça de alguém.** Regra que não está escrita no prompt, no protocolo ou na configuração não é regra.
- **Esquecer o que o modelo não sabe.** Um modelo que nunca diz "não sei" vai inventar com a mesma confiança com que acerta.
- **Usar dado real em assistente público.** Para testar prompts, use alertas fictícios. Rosto, placa e nome de pessoa real não vão para assistentes de uso geral; tratamento de dado pessoal segue a LGPD e a política da sua empresa.

## Próximo passo

Com o harness escrito, decida o quanto ele pode fazer sozinho em [Delegar](delegar.md).
