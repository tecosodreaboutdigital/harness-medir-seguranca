# D · Delegar

**Quanto ele pode fazer sozinho?**

## Propósito

Declarar, por caso de uso, o que a IA pode fazer sem ninguém, o que ela só recomenda e o que exige confirmação e autorização humanas. A autonomia é calibrada ao custo do erro, nunca à confiança no fornecedor nem à taxa de acerto anunciada.

**N mais alto significa mais controle humano, não mais liberdade para a máquina.** A tabela completa está em [nivel-de-controle.md](../modelos/nivel-de-controle.md).

## Perguntas

1. Qual linha da tabela de nível de controle define este caso? Ela está registrada?
2. Quais ações a IA pode executar sozinha? Todas são internas, fáceis de desfazer e registradas?
3. Quem confirma no vídeo, quem autoriza a ação e em quanto tempo cada um precisa responder?
4. O que acontece se ninguém responder dentro do prazo? (a resposta certa quase nunca é "a IA age sozinha")
5. A interface deixa o operador discordar da IA, e a discordância fica registrada?
6. Existe um jeito de conferir o alerta? Se não existe, o caso está em Trava.

## Saídas

- O nível de controle declarado no [contrato de tarefa](../modelos/contrato-de-tarefa.md), com a linha que o definiu.
- A lista de ações por nível: o que é automático, o que é recomendação, o que exige autorização.
- Os nomes ou funções de quem confirma e de quem autoriza, com prazo e caminho de escalonamento.

## Exemplos no CFTV

| Caso | Nível | Por quê |
|---|---|---|
| Marcar o trecho do vídeo e subir a câmera no mosaico quando há pessoa em área restrita da indústria | N1 | Ação interna, fácil de desfazer, sem integração com terceiros. |
| Câmera com falha ou obstruída em condomínio, abrindo chamado de manutenção | N1 | Interno e reversível. O chamado registra a falha como falha. |
| Fila acima do tempo combinado num grande evento, com recomendação de onde reforçar | N2 | Ação com efeito fora da central. O comando aceita ou recusa, e o registro guarda o motivo. |
| Veículo com placa suspeita na portaria de um terminal de granéis | N2 ou N3 | N2 se o alerta só gera ocorrência; N3 se leva a bloquear a entrada ou abordar o motorista. |
| Fumaça fora da cerca de um site remoto de energia, com despacho de equipe | N3 | Despachar equipe tem custo e risco reais. O operador confirma no vídeo antes de despachar. |
| Pessoa da lista de alerta por reconhecimento facial | N3 | Abordar alguém é difícil de desfazer. A IA aponta; o operador confirma e outra pessoa autoriza. |

Placa clonada e rosto humano não podem ter o mesmo nível: a mesma central pode ter um caso em N1 e outro em N3 rodando lado a lado.

## Antipadrões

- **Autonomia por fornecedor.** "O sistema já vem com ação automática" não decide nada. Quem decide é o contrato da tarefa.
- **Prazo que vira autorização.** "Se o operador não responder em 2 minutos, a IA aciona" transforma ausência de decisão em decisão.
- **Confirmar sem ver.** Confirmação humana significa olhar o vídeo, não clicar em "ok" num pop-up. Pedido de aprovação repetido demais vira clique automático.
- **Subir de nível por pressa.** Começar em N1 uma tarefa que deveria estar em N3 para "ganhar tempo no piloto" é exatamente o risco que o nível existe para evitar.
- **Delegar em Trava.** Se ninguém consegue conferir o alerta, não há o que delegar. Primeiro crie a verificação.

## Próximo passo

Com o nível declarado, defina como saber se está funcionando em [Inspecionar](inspecionar.md).
