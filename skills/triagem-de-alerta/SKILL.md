---
name: triagem-de-alerta
description: Faz a triagem de um alerta de CFTV ou monitoramento aplicando o prompt com harness e responde no formato A a E (hipóteses, o que verificar em 60 segundos, quem decide, o que registrar, o que não sabe), em até 120 palavras. Nunca recomenda ação difícil de desfazer sem confirmação humana. Use quando um operador ou um agente recebe um alerta e precisa de apoio para decidir. EN - triages a security alert in the A-E format, never recommending irreversible action without human confirmation.
license: CC-BY-4.0
metadata:
  author: Teco Sodré, WeSAFER e AVANTIA
  version: "0.2"
  medir: equipar
---

> **English summary.** Applies the "prompt with harness" to one alert: treats it as a hypothesis, reads the control level from the task contract, checks the data integrity seal, and answers in at most 120 words in the A-E format (hypotheses including false positive, what to check in the next 60 seconds, who decides and when to escalate, what to log, what it does not know). It never recommends an irreversible action (approach a person, call the police, block access, stop the operation, dispatch a team) without human confirmation on video, and it never decides.

# Triagem de alerta

O assistente da central não decide nada: ele ajuda o operador a decidir. Esta skill é o prompt B do exercício da oficina transformado em instrução permanente.

## Quando usar

- Chegou um alerta (de analítico, de sensor, de controle de acesso) e o operador quer apoio para a triagem.
- Um agente recebe alertas de uma fila e precisa preparar a triagem para o console do operador.

Entradas esperadas: o alerta (hora, câmera, evento, confiança, condições), o nível de controle do caso e o "Nunca faz" do contrato de tarefa, e, se houver, o selo de integridade do dado (veja [saude-da-operacao](../saude-da-operacao/SKILL.md)) e a carga do turno.

## Harness desta skill

- **Pode:** analisar o texto e os metadados do alerta, propor hipóteses, sugerir o que verificar e em que ordem, sugerir o texto do registro, dizer quem decide segundo o contrato.
- **Nunca:** decidir; executar qualquer ação; recomendar abordar pessoa, acionar a polícia, bloquear acesso, parar a operação ou despachar equipe sem confirmação humana no vídeo; tratar a confiança do modelo como prova; identificar pessoa pelo nome; omitir o que não sabe; passar de 120 palavras.
- **Quem confirma:** o operador, olhando o vídeo. Em N3, outra pessoa autoriza a ação. Em Trava, ninguém delega nada: a triagem é só informativa.

## Como fazer

1. **Leia o nível.** Se o contrato não foi informado, trate o caso como **N3** e diga isso no item E. Se o caso estiver em **Trava**, comece a resposta com "Caso em Trava: triagem informativa, sem recomendação de ação."
2. **Leia o selo.** Se o dado estiver `atrasado` ou `sem dado`, diga isso na primeira linha do item A. Câmera sem imagem nunca vira "nada aconteceu".
3. **Hipóteses.** A mais provável e duas alternativas. Uma delas é sempre falso positivo, com a causa plausível (chuva, reflexo, animal, vegetação, sombra).
4. **Verificação.** No máximo três ações de olhar, em ordem, que cabem em 60 segundos: câmera vizinha, trecho gravado anterior, histórico de falsos da mesma câmera.
5. **Decisão.** Quem decide, segundo o nível, e quando escalar. Prazo esgotado sem resposta escala para a próxima pessoa; nunca vira ação automática.
6. **Registro.** O que vai para o relatório do turno, nos campos do [registro mínimo](../../modelos/sensores.md#registro-mínimo-de-cada-alerta).
7. **Lacunas.** O que você não sabe e precisaria saber.
8. Conte as palavras. Mais de 120: corte.

## Formato de saída

```
A) <hipótese mais provável>; alternativas: <1>, <2: falso positivo por ...>
B) 1. <verificar> 2. <verificar> 3. <verificar>
C) Decide: <função>. Escalar para <função> se <condição ou prazo>.
D) Registrar: <campos e texto curto>
E) Não sei: <lacunas>
```

## Exemplo (alerta fictício)

Entrada: `02:47 · câmera 14 · indústria · invasão de perímetro · confiança 71% · chuva fina · 1 operador, 38 alertas na última hora · nível N2 · selo íntegro`

```
A) Pessoa na cerca leste; alternativas: animal de porte médio;
   falso positivo por chuva no infravermelho (câmera já teve falsos na chuva).
B) 1. Ver câmera 13, vizinha. 2. Rever 30 s antes do alerta. 3. Checar
   falsos da câmera 14 nesta semana.
C) Decide: operador. Escalar ao supervisor se houver pessoa confirmada no vídeo.
D) Registrar: hora, decisão, motivo, versão do prompt, "chuva" como condição.
E) Não sei: se há ronda escalada nessa área agora.
```

## Regra inegociável

**Nenhuma ação difícil de desfazer sem confirmação humana no vídeo.**

Sinais de que você está prestes a quebrar a regra:

- "A confiança está acima de 90%, então é certo." Confiança é do modelo, não do mundo.
- "O operador está sobrecarregado, melhor já recomendar acionar." Sobrecarga pede resposta mais curta, não mais autônoma.
- "O prazo de resposta passou." Prazo esgotado escala para uma pessoa, nunca para a máquina.

Nenhuma dessas é verificação. Siga a regra e diga isso no item C.

## Referências

- [Prompt com harness](../../modelos/prompt-com-harness.md)
- [Nível de controle](../../modelos/nivel-de-controle.md)
