# I · Inspecionar

**Como sabemos que está funcionando?**

## Propósito

Medir o comportamento da IA e da central com sensores que produzem evidência, não opinião. "O operador está gostando" é opinião. Uma frase como "falsos positivos caíram de 180 para 60 a cada mil alertas, e a mediana do tempo até a triagem ficou abaixo de 2 minutos" (números ilustrativos) é evidência, porque qualquer pessoa pode conferir no registro.

Quem avalia não é quem executa: a IA não atesta a própria taxa de acerto. A conferência vem do operador, do vídeo gravado, de um segundo sensor ou de quem foi a campo.

## Perguntas

1. Quais sensores estão ligados desde o primeiro dia, e de onde vêm os dados de cada um?
2. A meta de falsos positivos a cada mil alertas foi combinada antes de ligar?
3. A carga do operador (alertas por operador por hora) está sendo medida como se mede downtime?
4. As discordâncias do operador ficam registradas, com motivo?
5. Falha de câmera, rede ou servidor aparece como falha, ou some como "nada aconteceu"?
6. Quem olha esses números, com que frequência, e o que acontece quando um deles passa do limite?

## Saídas

- Os sensores escolhidos, com definição, fonte e limite de cada um (veja [sensores.md](../modelos/sensores.md)).
- O registro de cada alerta, decisão e ação, com horário.
- Uma revisão periódica com data marcada, em que os números são lidos por quem pode mudar o harness.

## Exemplos no CFTV

- **Sites remotos de energia.** Critério de piloto: alarme crítico triado em até 5 minutos. O sensor é o tempo entre o alerta e a primeira decisão registrada do operador, medido em todos os alertas, não numa amostra escolhida.
- **Grandes eventos.** Cada recomendação de remanejamento tem aceite ou recusa registrados. A taxa de recusa, lida com os motivos, mostra onde a recomendação está desalinhada com o comando.
- **Indústria.** Uma câmera caída que some do painel pode parecer "nenhuma invasão hoje". O sensor de disponibilidade por câmera separa silêncio de cegueira.
- **Varejo.** Se os alertas por operador por hora dobraram depois do analítico novo, o ganho de IA virou aumento de volume. O projeto falhou, mesmo com taxa de acerto alta.

## Antipadrões

- **Medir só a taxa de acerto do fornecedor.** O número de laboratório não diz nada sobre a sua cena, a sua iluminação e a sua chuva.
- **Amostrar os bons casos.** Revisar só os alertas que viraram ocorrência esconde os falsos positivos e todo o custo de operador.
- **Tratar ausência de alerta como sucesso.** Sem sensor de falha de infraestrutura, câmera cega e câmera tranquila parecem iguais.
- **Interface que não deixa discordar.** Se o operador não consegue registrar "a IA errou", o sensor de discordância não existe, e o defeito é de projeto, não de operador.
- **Número sem dono.** Indicador que ninguém lê em data marcada é decoração.

## Próximo passo

Com a evidência na mão, transforme cada erro em mudança permanente em [Reforçar](reforcar.md).
