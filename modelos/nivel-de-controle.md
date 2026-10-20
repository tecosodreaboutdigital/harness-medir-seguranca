# Nível de controle

Quanto a IA pode fazer sozinha num caso de uso, decidido pelo custo do erro e não pela confiança no fornecedor. Usado no passo [Delegar](../medir/delegar.md) e registrado no [contrato de tarefa](contrato-de-tarefa.md).

Adaptado da tabela de autonomia do [harness-medir](https://github.com/tecosodreaboutdigital/harness-medir) (faixas N0 a N3 e a matriz de risco por faixa) para uma câmera, um evento e uma decisão.

> **N mais alto significa mais controle humano, não mais liberdade para a máquina.** Em N3, a IA continua só apontando; o que cresce é o número de pessoas e de registros entre o alerta e a ação.

---

## A tabela (aplique em ordem)

Leia de cima para baixo. **A primeira linha verdadeira define o nível**, e as linhas seguintes não o reduzem.

| Se... | Nível | Quem decide |
|---|---|---|
| quando o alerta dispara, alguém age no mundo real de um jeito difícil de desfazer (abordar, acionar a polícia, bloquear acesso, parar a operação) | **N3** | A IA aponta; o operador confirma no vídeo e outra pessoa autoriza a ação. Tudo registrado, com quem decidiu e por quê. |
| o sistema lê ou grava em sistema de outra empresa ou do cliente, ou o evento passa de 100 por mês, ou a ação tem efeito fora da central | **N2** | A IA aponta e recomenda; o operador confirma antes de agir. Cada aceite ou recusa fica registrado. |
| a ação é interna, fácil de desfazer e sem integração com terceiros | **N1** | A IA pode agir sozinha (marcar o vídeo, abrir chamado, subir a câmera no mosaico), sempre com registro. |

Depois, a trava, que **passa por cima de qualquer linha acima**:

| Se... | Nível | O que fazer |
|---|---|---|
| não existe jeito de conferir se o alerta estava certo | **Trava** | Ainda não delegue nada. Primeiro crie a verificação (segundo sensor, vídeo gravado, conferência em campo). Quando ela existir, o caso fica no nível que a tabela acima definiu. |

**Sem verificação não existe autonomia responsável.**

Registre sempre o nível e **a linha que o definiu**. Quem revisar o caso depois precisa saber se o nível veio da ação, da integração ou do volume.

---

## As quatro perguntas

O jeito mais rápido de aplicar a tabela, usado no exercício da oficina:

1. Quando o alerta dispara, alguém age no mundo real de forma difícil de desfazer? (abordar, acionar a polícia, bloquear acesso, parar a operação)
2. O sistema precisa ler ou gravar em sistema de outra empresa ou do cliente? (controle de acesso, RH, ERP, lista de alerta)
3. Esse evento acontece mais de 100 vezes por mês?
4. Existe um jeito de conferir se o alerta estava certo? (segundo sensor, vídeo gravado, conferência em campo)

Leitura:

- 1 = sim: **N3**.
- 1 = não, e 2 = sim ou 3 = sim (ou a ação tem efeito fora da central): **N2**.
- Caso contrário: **N1**.
- 4 = não: **Trava**, qualquer que seja o resultado acima.

Pergunta complementar, que não muda o nível mas entra no contrato: a cada mil alertas, quantos falsos você aceita antes de revisar o sistema?

---

## Matriz de ações por reversibilidade

O nível vem da pior ação que o alerta pode disparar. Use esta matriz para classificar as ações do seu caso. A autoridade é definida pela reversibilidade, não pela importância aparente da ação.

| Ação | Reversibilidade | Autoridade necessária | Nível mínimo |
|---|---|---|---|
| Marcar trecho de vídeo, adicionar etiqueta | Reversível | Nenhuma, com registro | N1 |
| Subir a câmera no mosaico, tocar aviso na central | Reversível | Nenhuma, com registro | N1 |
| Abrir chamado interno de manutenção | Reversível | Nenhuma, com registro | N1 |
| Recomendar remanejamento de efetivo | Reversível, mas com efeito fora da central | Operador ou comando aceita ou recusa | N2 |
| Gravar ocorrência em sistema do cliente | Parcialmente reversível | Operador confirma antes | N2 |
| Consultar lista de alerta ou cadastro de outra empresa | Reversível, a exposição não | Operador confirma antes | N2 |
| Despachar equipe de campo | Difícil de desfazer | Operador confirma no vídeo e outra pessoa autoriza | N3 |
| Abordar pessoa, bloquear acesso, acionar a polícia, parar a operação | Difícil ou impossível de desfazer | Operador confirma no vídeo e outra pessoa autoriza | N3 |

Acrescente as linhas do seu caso, mas não retire a última.

---

## Exemplos

| Caso | Nível | Linha que definiu |
|---|---|---|
| Câmera obstruída num condomínio, com chamado de manutenção | N1 | Interna, fácil de desfazer, sem integração |
| Falta de EPI em área de produção da indústria, marcando o vídeo para o supervisor | N1 | Interna, fácil de desfazer, sem integração |
| Fila acima do tempo combinado num grande evento | N2 | Ação com efeito fora da central |
| Volume saindo pela doca fora do horário no varejo, gravando ocorrência no sistema da loja | N2 | Grava em sistema do cliente |
| Placa clonada na portaria de um terminal de granéis, com bloqueio de entrada | N3 | Bloquear acesso é difícil de desfazer |
| Pessoa da lista de alerta por reconhecimento facial | N3 | Abordar pessoa é difícil de desfazer |
| Invasão de perímetro num site remoto onde a câmera não grava e ninguém vai a campo | Trava | Não existe jeito de conferir o alerta |

Placa clonada e rosto humano não podem ter o mesmo nível que uma câmera obstruída, mesmo na mesma central e com o mesmo equipamento.

---

## Erros comuns

- **Declarar o nível do sistema, não do caso.** O nível é sempre de uma câmera, um evento e uma decisão.
- **Ler N3 como "IA mais autônoma".** É o contrário.
- **Esquecer a Trava porque o resultado acima deu N1.** Ação interna e reversível sobre um alerta que ninguém confere continua sendo automação às cegas.
- **Não registrar a linha.** Sem ela, ninguém consegue revisar a decisão quando o volume ou a integração mudarem.
- **Nunca revisar.** Volume que passou de 100 por mês, integração nova ou ação nova mudam o nível. Reaplique a tabela em toda revisão do harness.
