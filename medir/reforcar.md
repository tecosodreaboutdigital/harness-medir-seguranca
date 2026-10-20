# R · Reforçar

**O que muda depois de um erro?**

## Propósito

Fazer cada erro virar mudança permanente no ambiente: uma regra, um limiar, uma zona mascarada, um treino, uma ferramenta a menos. Com data e versão. É o passo que separa MEDIR de um ciclo genérico de melhoria: você age sobre o ambiente, não sobre a resposta daquela noite.

Um conserto pontual resolve um plantão. Uma mudança no harness melhora todos os próximos.

## Perguntas

1. O que exatamente deu errado? Em qual passo do MEDIR estava a lacuna (mapa, equipamento, delegação, inspeção)?
2. Que mudança permanente evita que o mesmo erro volte? Regra no prompt, limiar, zona mascarada, mudança de nível, treino, procedimento?
3. Quem aprova a mudança e quando ela entra em vigor?
4. Qual sensor vai mostrar se a mudança funcionou, e em quanto tempo?
5. A mudança foi registrada com data, versão e motivo?
6. O erro se repetiu depois de uma mudança anterior? Então a mudança anterior não era a certa.

## Saídas

- Uma entrada de "erro que virou regra", com data, versão, o que mudou e por quê (formato em [CONTRIBUTING.md](../CONTRIBUTING.md#erro-que-virou-regra)).
- O contrato de tarefa e o prompt atualizados, com o número de versão novo.
- A data da próxima revisão do harness.

## Exemplos no CFTV

| Erro | Mudança permanente |
|---|---|
| Grafite em muro gerando alertas de invasão toda noite | Zona mascarada na área do muro, com data e versão; sensor de falsos positivos daquela câmera acompanhado por duas semanas. |
| Número de vagão corroído lido errado, gerando divergência de carga | Conferência cruzada obrigatória com segundo registro antes de abrir ocorrência; leitura com confiança baixa vai para o operador, nunca direto ao sistema do cliente. |
| Placa lida com 87% de confiança tratada como certa | Regra no prompt: abaixo do limiar combinado, a resposta sempre traz a leitura alternativa e pede confirmação no vídeo. |
| Câmera caída interpretada como área vazia num grande evento | Falha de câmera passa a gerar alerta próprio, de infraestrutura, e a área fica marcada como "sem visão" no painel do comando. |
| Operador ignorando alertas de uma câmera com chuva | Limiar sazonal para aquela cena e revisão da carga por operador no período chuvoso; o motivo registrado nas discordâncias embasou a mudança. |

## Antipadrões

- **Conserto que não deixa rastro.** Ajustar a sensibilidade "só esta noite" e não registrar faz o mesmo erro voltar sem ninguém saber por quê.
- **Culpar o operador.** Se o erro passou porque a interface não deixava discordar, a correção é na interface, não no treinamento do operador.
- **Trocar de modelo como resposta padrão.** Um modelo mais forte num harness com lacuna só deixa a falha mais cara.
- **Reforçar sem sensor.** Mudança sem número para acompanhar é aposta.
- **Acumular regras sem revisar.** Regra que não se aplica mais ocupa contexto, confunde o modelo e engorda o harness. Na revisão periódica, retire o que perdeu o motivo.

## Volta ao início

Toda mudança relevante pode alterar o mapa. Na revisão marcada, volte a [Mapear](mapear.md) com o que aconteceu.
