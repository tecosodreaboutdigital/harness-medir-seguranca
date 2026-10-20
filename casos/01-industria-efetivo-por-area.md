# Caso 01 · Indústria de bens de consumo: efetivo por área

Caso de exemplo da v0.1, descrito em nível de setor. Não traz resultados medidos.

Setor: indústria de bens de consumo
Porte, sem identificar: várias plantas

## Situação antes

A operação tinha câmeras, catracas, leitura de placa e reconhecimento facial havia anos, mas ninguém respondia rápido a uma pergunta simples: quantas pessoas estão na produção agora? O problema não era de perímetro, era de processo.

## Mapear

Câmera: catracas e acessos das áreas de produção, com o cadastro de pessoas
Evento: entrada e saída por área
Decisão: numa evacuação, a brigada precisa do efetivo por área e da lista nominal; no dia a dia, quem aprova acesso é a prevenção de perdas
O que nunca pode acontecer: a lista de evacuação mostrar uma área vazia quando há gente lá dentro

## Equipar

A IA cruza o que já existe (catraca, leitura de placa, cadastro) e entrega efetivo por área e lista nominal para a brigada. Não aprova nem bloqueia acesso.

## Delegar

Nível de controle: N2
Linha da tabela que o definiu: o sistema lê dados de controle de acesso e cadastro
Quem confirma e quem autoriza: a brigada usa a lista; a aprovação de acesso continua com a prevenção de perdas

## Inspecionar

O que seria medido: divergência entre o efetivo calculado e a contagem física em simulados de evacuação; catracas ou leitores fora do ar sinalizados como falha, nunca como área vazia.

## Reforçar

Ponto de atenção para a primeira revisão: toda divergência encontrada em simulado vira regra (por exemplo, como tratar a pessoa que entrou sem passar pela catraca) e entra no contrato com data e versão.

## A lição

**Boa parte do ganho não exigiu equipamento novo: o dado já existia.** O harness foi o que transformou dados soltos numa resposta que a brigada pode usar.
