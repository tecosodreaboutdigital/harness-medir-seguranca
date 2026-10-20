# Prompt com harness

O mesmo alerta em dois prompts: **A**, o modelo puro, e **B**, o modelo com harness. É o exercício do passo [Equipar](../medir/equipar.md) e a forma mais rápida de ver, em cinco minutos, o que o harness muda.

> **Use só alertas fictícios.** Não cole rosto, placa, nome ou imagem de pessoa real em assistente de uso geral. Tratamento de dado pessoal segue a LGPD e a política da sua empresa.

---

## O alerta de exemplo

```
ALERTA 02:47 · câmera 14 · indústria
Evento: Invasão de perímetro
Confiança do modelo: 71%
Chuva fina. Um operador no turno; 38 alertas na última hora.
```

Troque setor, evento e condições pelos do seu caso. Mantenha a hora, a confiança e a carga do operador: são elas que testam se o modelo considera o contexto.

---

## Prompt A · modelo puro

```
Sou operador de uma central de monitoramento de CFTV. Recebi este alerta:

<ALERTA>

O que eu faço?
```

---

## Prompt B · modelo + harness

```
Você é o assistente da central de monitoramento de uma operação do setor "<SETOR>".
Você não decide nada: você ajuda o operador a decidir.

Alerta recebido:
<HORA> · <CÂMERA> · <EVENTO> · confiança do modelo <X>% · <CONDIÇÕES>

Regras desta operação (harness):
1. Todo alerta é uma hipótese, nunca uma prova.
2. Nível de controle deste caso: <N1, N2 ou N3> (<quem decide>).
3. Nunca recomende ação difícil de desfazer (abordar pessoa, acionar a polícia,
   bloquear acesso, parar a operação) sem confirmação humana no vídeo.
4. O operador está cansado e sozinho: seja curto e concreto.

Responda em até 120 palavras, neste formato:
A) Hipótese mais provável e duas alternativas, incluindo falso positivo.
B) O que verificar nos próximos 60 segundos, em ordem.
C) Quem decide e quando escalar.
D) O que registrar no relatório do turno.
E) O que você não sabe e precisaria saber.
```

Para preencher a regra 2, use o texto de "Quem decide" da [tabela de nível de controle](nivel-de-controle.md). Exemplo para N2: "A IA aponta e recomenda; o operador confirma antes de agir. Cada aceite ou recusa fica registrado."

Se o caso estiver em **Trava**, não rode o prompt B como se fosse operação: o exercício serve para mostrar a diferença, mas o caso ainda não tem como ser delegado.

---

## Como rodar o lado a lado

1. Escolha um assistente de IA (qualquer um que você já use no celular ou no computador).
2. Abra uma **conversa nova** e cole o prompt A. Leia a resposta inteira.
3. Abra **outra conversa nova**, no mesmo assistente, e cole o prompt B. Conversa nova evita que a resposta B herde o contexto da A.
4. Compare as duas respostas com as perguntas abaixo, marcando o que mudou.
5. Decida: **qual resposta você entrega ao seu operador às 3 da manhã?**

O que observar:

- [ ] Ficou mais curta e direta?
- [ ] Pediu para verificar antes de agir?
- [ ] Disse quem decide?
- [ ] Admitiu o que não sabe?
- [ ] Lembrou de registrar?
- [ ] Tratou o alerta como hipótese, com falso positivo entre as alternativas?
- [ ] Recomendou alguma ação difícil de desfazer sem confirmação no vídeo? (se sim, o harness falhou e precisa de reforço)

Para um grupo, cada pessoa roda os dois prompts e vota em A, B ou nenhuma das duas, dizendo o que o harness mudou. A discussão sobre o "nenhuma" costuma ser a mais útil.

---

## Como adaptar o prompt B à sua operação

- **Regras vêm do contrato.** Copie o "Nunca faz" e o nível de controle do [contrato de tarefa](contrato-de-tarefa.md) para as regras do prompt. Não invente regra que não está no contrato.
- **Uma regra por erro.** Quando a resposta errar de um jeito novo, acrescente a regra que teria evitado o erro e registre a mudança (veja [Reforçar](../medir/reforcar.md)).
- **Versione.** Dê número de versão ao prompt e registre qual versão estava em uso em cada alerta. Sem isso, uma mudança de comportamento não tem explicação.
- **Teste de novo depois de trocar de modelo.** O mesmo prompt pode render diferente em outro modelo ou em outra versão do mesmo modelo. Rode o lado a lado outra vez.
- **Mantenha o limite de tamanho.** Resposta longa não é lida às 3 da manhã.
