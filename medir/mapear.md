# M · Mapear

**Que tarefa, com que risco?**

## Propósito

Transformar "quero IA nas câmeras" em uma tarefa que cabe numa frase: **uma câmera, um evento, uma decisão.** É no Mapear que se decide o nível de controle, antes de qualquer conversa sobre ferramenta ou fornecedor.

Sem esse recorte, nenhum sensor posterior consegue dizer se a IA acertou, porque ninguém disse antes o que era acertar.

## Perguntas

1. Qual câmera (ou grupo de câmeras com a mesma cena), qual evento e qual decisão o alerta vai alimentar?
2. Quem decide hoje, sem IA, e em quanto tempo?
3. Quanto custa um falso positivo? E um falso negativo? Em pessoas, em tempo de operador, em dinheiro, em reputação.
4. Quantas vezes por mês o evento acontece? E quantos alertas por mês se espera receber?
5. O que nunca pode acontecer, mesmo que a IA esteja certa? (abordar a pessoa errada, bloquear uma saída de emergência, parar uma linha de produção)
6. Quando o alerta dispara, alguém age no mundo real de forma difícil de desfazer?
7. O sistema precisa ler ou gravar em sistema de outra empresa ou do cliente?
8. Existe um jeito de conferir se o alerta estava certo? (segundo sensor, vídeo gravado, conferência em campo)
9. A cada mil alertas, quantos falsos você aceita antes de revisar o sistema?

As perguntas 4, 6, 7 e 8 definem o nível de controle: veja [nivel-de-controle.md](../modelos/nivel-de-controle.md).

## Saídas

- O caso de uso escrito em uma frase.
- O nível de controle e **a linha da tabela que o definiu**.
- A meta de falsos positivos a cada mil alertas, combinada antes de ligar.
- A lista do que nunca pode acontecer.
- O [contrato de tarefa](../modelos/contrato-de-tarefa.md) preenchido, com as lacunas marcadas como pendência.

## Exemplos no CFTV

| Setor | Câmera, evento, decisão |
|---|---|
| Indústria | Câmera da portaria de pedestres; pessoa entrando sem passar pela catraca; o operador decide se aciona a vigilância. |
| Terminal de granéis | Câmera da balança; caminhão pesado sem registro de chegada; o operador decide se abre ocorrência antes da descarga. |
| Sites remotos de energia | Câmera térmica do perímetro; fumaça fora da cerca; o operador decide se despacha equipe. |
| Grandes eventos | Câmeras de um acesso; fila acima do tempo combinado; o comando decide se remaneja efetivo. |
| Varejo | Câmera da doca; volume saindo fora do horário de expedição; o operador decide se chama o supervisor da loja. |
| Condomínio | Câmera da garagem; veículo entrando colado em outro; o operador decide se fala com a portaria. |

## Antipadrões

- **Mapear o produto em vez da tarefa.** "Vamos ligar o analítico de perímetro em todas as câmeras" não é um caso de uso. Cada cena tem custo de erro diferente.
- **Pular o custo do falso positivo.** Se ninguém sabe quanto custa um alarme falso, a meta de falsos positivos vira opinião depois que o sistema já está ligado.
- **Declarar o nível por fornecedor.** "Esse sistema é N1" não existe. O nível é da tarefa: o mesmo equipamento pode estar em N1 numa cena e em N3 em outra.
- **Deixar o "nunca pode acontecer" implícito.** O que não está escrito vai ser descoberto em operação, pelo pior caminho.
- **Mapear sem perguntar ao operador.** Quem passa oito horas na frente do mosaico sabe quantos alertas inúteis já recebe hoje.

## Próximo passo

Com o nível definido, siga para [Equipar](equipar.md).
