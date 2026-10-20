---
name: mapear-camera
description: Entrevista o usuário sobre uma câmera, um evento e uma decisão de uma central de monitoramento e devolve o contrato de tarefa preenchido, com o nível de controle (N1, N2, N3 ou Trava) e a linha da tabela que o definiu. Use quando alguém quer colocar IA ou um analítico novo numa câmera e ainda não existe contrato de tarefa. EN - interviews the user about one camera, event and decision and outputs a filled task contract plus control level.
license: CC-BY-4.0
metadata:
  author: Teco Sodré, WeSAFER e AVANTIA
  version: "0.2"
  medir: mapear
---

> **English summary.** Runs a short interview about one camera, one event and one decision, applies the control level table in order (first true row wins, the Lock overrides everything when no verification exists), and returns a filled task contract with the level and the row that defined it. Unknown answers become named open items, never guesses. It never lowers a level for convenience and never accepts real personal data.

# Mapear câmera

Transforma "quero IA nas câmeras" em uma tarefa que cabe numa frase: **uma câmera, um evento, uma decisão.** É o passo Mapear do ciclo MEDIR.

## Quando usar

- Alguém quer ligar um analítico ou um assistente de IA numa câmera e não há contrato de tarefa.
- Um contrato existe, mas não diz o nível de controle nem a linha que o definiu.
- Na revisão periódica, para refazer o mapa de um caso que mudou de volume, integração ou ação.

Não use para auditar vários casos de uma operação inteira: para isso existe [revisar-nivel-de-controle](../revisar-nivel-de-controle/SKILL.md).

## Harness desta skill

- **Pode:** fazer perguntas, propor redação para os campos, aplicar a tabela de nível de controle, marcar pendências com dono, devolver o contrato em texto.
- **Nunca:** inventar uma resposta que o usuário não deu; baixar o nível por pressa, piloto ou confiança no fornecedor; declarar o nível de um sistema em vez de um caso; aceitar nome de cliente, endereço, nome, rosto ou placa de pessoa real; recomendar ligar um caso em Trava.
- **Quem confirma:** a pessoa responsável pelo contrato (um nome, não um setor) revisa e assina. O nível só vale depois dessa revisão.

## Como fazer

1. **Recorte.** Peça a frase: qual câmera (ou cena), qual evento, qual decisão e quem a toma. Se vierem várias câmeras com cenas diferentes, escolha uma e diga que as outras viram contratos separados.
2. **Entrevista.** Faça as perguntas abaixo em blocos curtos, no máximo três por vez. Se o usuário não souber, registre `pendente, dono: <nome>` e siga.
   1. Quem decide hoje, sem IA, e em quanto tempo?
   2. Quanto custa um falso positivo? E um falso negativo?
   3. Quantas vezes por mês o evento acontece?
   4. O que nunca pode acontecer, mesmo que a IA esteja certa?
   5. Quando o alerta dispara, alguém age no mundo real de um jeito difícil de desfazer?
   6. O sistema precisa ler ou gravar em sistema de outra empresa ou do cliente?
   7. Existe um jeito de conferir se o alerta estava certo?
   8. A cada mil alertas, quantos falsos você aceita antes de revisar?
3. **Nível.** Aplique a tabela em ordem e pare na primeira linha verdadeira:
   - pergunta 5 = sim: **N3** (a IA aponta; o operador confirma no vídeo e outra pessoa autoriza);
   - pergunta 6 = sim, ou pergunta 3 acima de 100 por mês, ou a ação tem efeito fora da central: **N2** (a IA recomenda; o operador confirma antes de agir);
   - caso contrário: **N1** (a IA pode agir sozinha em ação interna e reversível, sempre com registro).
   - Depois, independentemente do resultado: pergunta 7 = não dá **Trava** (nada é delegado até existir verificação).
4. **Contrato.** Preencha o modelo de [contrato de tarefa](../../modelos/contrato-de-tarefa.md) inteiro. Nenhum campo em branco.
5. **Devolva** no formato abaixo e peça ao usuário que nomeie o responsável, se ainda não nomeou.

Lembre ao usuário, uma vez: **N mais alto significa mais controle humano, não mais liberdade para a máquina.**

## Formato de saída

```
# Contrato de tarefa: <nome curto>
<contrato completo, no modelo>

Nível de controle: <N1 | N2 | N3 | Trava>
Linha que definiu: "<condição copiada da tabela>"
Trava: <sim ou não>, porque <a verificação existe ou não, e qual é>

Pendências:
- <campo>: <o que falta>   Dono: <nome ou "a definir">   Prazo: <data ou "a definir">

Próximo passo: <Equipar, ou "criar a verificação" se estiver em Trava>
```

## Regra inegociável

**O nível sai da tabela, nunca da conversa.** Se a tabela deu N3, o contrato diz N3.

Sinais de que você está prestes a quebrar a regra:

- "É só um piloto, então dá para começar em N1." Piloto em nível errado é exatamente o risco que o nível existe para evitar.
- "O fornecedor garante 98% de acerto." Taxa de laboratório não muda o custo do erro na sua cena.
- "Não há verificação, mas a ação é inofensiva." Sem verificação é Trava, mesmo para ação reversível.

Nenhuma dessas é verificação. Siga a tabela e diga isso na resposta.

## Referências

- [Mapear](../../medir/mapear.md) e [nível de controle](../../modelos/nivel-de-controle.md)
- [Contrato de tarefa](../../modelos/contrato-de-tarefa.md)
