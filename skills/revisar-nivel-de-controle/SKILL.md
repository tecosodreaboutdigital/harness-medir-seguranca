---
name: revisar-nivel-de-controle
description: Audita uma operação de CFTV ou monitoramento que já tem analíticos ou IA ligados, caso a caso, contra a tabela de nível de controle e o checklist de dez itens, e devolve uma tabela de lacunas ordenada por gravidade. Use em revisões periódicas, antes de ampliar um piloto ou depois de um incidente. EN - audits an existing analytics deployment against the control level table and the 10-item checklist and outputs prioritized gaps.
license: CC-BY-4.0
metadata:
  author: Teco Sodré, WeSAFER e AVANTIA
  version: "0.2"
  medir: delegar, inspecionar
---

> **English summary.** For each analytics use case already running, rebuilds the one-camera-one-event-one-decision sentence, derives the control level from the table, compares it with the declared level, runs the 10-item pre-launch checklist and returns a gap table sorted by severity (Lock cases running first). It only reads and asks; it never changes configuration, never "approves" the operation and never blames the operator.

# Revisar nível de controle

Uma operação com analíticos ligados há meses costuma ter casos com nível declarado pelo fornecedor, casos sem verificação e casos que mudaram de volume. Esta skill encontra essas lacunas.

## Quando usar

- Revisão periódica do harness (a data marcada no contrato).
- Antes de ampliar um piloto para mais câmeras ou mais sites.
- Depois de um incidente ou de uma queixa de excesso de alertas.

## Harness desta skill

- **Pode:** ler documentação, contratos, listas de regras e relatórios que o usuário fornecer; fazer perguntas; aplicar a tabela e o checklist; apontar lacunas e sugerir a pendência.
- **Nunca:** alterar configuração, desligar ou ligar analítico, acessar sistemas por conta própria, declarar a operação "aprovada", atribuir dono a uma pendência sem o usuário dizer quem é, culpar o operador por defeito de projeto.
- **Quem confirma:** a coordenação da central decide cada pendência, com dono e prazo. A skill só aponta.

## Como fazer

1. **Inventário.** Liste os casos ligados. Para cada um, reconstrua a frase: câmera (ou cena), evento, decisão. Caso que não cabe numa frase é a primeira lacuna.
2. **Nível derivado.** Aplique a tabela em ordem: ação difícil de desfazer dá N3; leitura ou escrita em sistema de terceiro, volume acima de 100 por mês ou efeito fora da central dá N2; o resto, N1. Sem verificação: **Trava**, por cima de tudo.
3. **Compare** com o nível declarado. Declarado com menos controle humano que o derivado (ex.: declarado N1, derivado N3) é lacuna grave.
4. **Checklist.** Passe os dez itens de [checklist antes de ligar](../../modelos/checklist-antes-de-ligar.md) em cada caso. Peça comprovação, não opinião: o registro existe? O teste de câmera derrubada foi feito?
5. **Ordene** as lacunas por gravidade:
   1. Caso em Trava rodando com qualquer ação automática.
   2. Nível declarado com menos controle humano que o derivado.
   3. Falha de infraestrutura que aparece como "nada aconteceu" (item 8).
   4. Itens 1, 2 e 4 (mapa incompleto).
   5. Itens 5, 6, 7 e 9 (sem como provar que funciona).
   6. Item 10 (sem data de revisão).
6. **Devolva** a tabela e o resumo. Não use nota nem porcentagem: o checklist é uma porta, não uma nota.

## Formato de saída

```
Revisão de nível de controle · <operação, em nível de setor> · <data>

| Caso (câmera, evento, decisão) | Declarado | Pela tabela | Linha | Trava? | Itens "não" | Gravidade |
|---|---|---|---|---|---|---|

Lacunas, da mais grave para a menos grave:
1. <caso>: <lacuna>. Pendência sugerida: <o que fazer>. Dono: <a definir pela coordenação>.

Fora do escopo desta revisão: <o que não foi possível conferir e por quê>
```

## Regra inegociável

**A skill aponta; quem decide é a coordenação.** Nenhuma lacuna é fechada pela própria revisão.

Sinais de que você está prestes a quebrar a regra:

- "Esse caso roda há um ano sem problema, pode ficar como está." Sem registro e sem sensor, "sem problema" não é evidência.
- "Nove de dez itens, está 90% pronto." Um "não" é uma lacuna com nome.
- "O operador é que não olha os alertas." Se a interface não deixa discordar, o defeito é de projeto.

## Referências

- [Nível de controle](../../modelos/nivel-de-controle.md) e [checklist antes de ligar](../../modelos/checklist-antes-de-ligar.md)
- [Delegar](../../medir/delegar.md) e [Inspecionar](../../medir/inspecionar.md)
