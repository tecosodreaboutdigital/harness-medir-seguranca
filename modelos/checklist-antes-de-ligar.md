# Checklist antes de ligar um analítico novo

Dez itens para conferir antes de ligar um analítico ou um assistente de IA numa câmera real. Passe de novo em toda revisão do harness.

**É uma porta, não uma nota.** Nove "sim" e um "não" não significam 90% pronto: significam uma lacuna com nome, e é exatamente por ela que vai entrar o próximo incidente. Todo "não" vira pendência com dono e prazo.

---

```
Caso: <câmera, evento, decisão>
Conferido por: <nome>   Data: <dd/mm/aaaa>   Versão do contrato: <v>

[ ] 1. O caso de uso está escrito em uma frase: câmera, evento, decisão.
[ ] 2. O nível de controle foi declarado, e a linha da tabela que o definiu está registrada.
[ ] 3. Existe um jeito de conferir o alerta.
[ ] 4. Está definido quem confirma, quem autoriza e em quanto tempo.
[ ] 5. A interface deixa o operador discordar, e a discordância fica registrada.
[ ] 6. A meta de falsos positivos a cada mil alertas foi combinada antes de ligar.
[ ] 7. A carga do operador (alertas por hora) é medida como se mede downtime.
[ ] 8. Falha de câmera, rede ou servidor aparece como falha, nunca como "nada aconteceu".
[ ] 9. Existe registro de cada alerta, decisão e ação, com horário.
[ ] 10. Há data marcada para revisar o harness com o que aconteceu.

Pendências (todo "não"):
- Item <n>: <o que falta>   Dono: <nome>   Prazo: <data>
```

---

## Como comprovar cada item

| # | Comprovação aceitável | Passo MEDIR |
|---|---|---|
| 1 | A frase está no [contrato de tarefa](contrato-de-tarefa.md) | Mapear |
| 2 | Nível e linha no contrato (veja [nível de controle](nivel-de-controle.md)) | Mapear, Delegar |
| 3 | Descrição da verificação (segundo sensor, vídeo gravado, conferência em campo). Se não há, o caso está em **Trava** e não se liga | Delegar |
| 4 | Funções e prazos no contrato, incluindo o que acontece se ninguém responder | Delegar |
| 5 | Botão ou campo de discordância testado, e o registro aparece no relatório | Inspecionar |
| 6 | Número escrito no contrato, com data, antes do primeiro alerta | Mapear, Inspecionar |
| 7 | Sensor de alertas por operador por hora ligado (veja [sensores](sensores.md)) | Inspecionar |
| 8 | Teste feito: derrube uma câmera de teste e veja o alerta de falha chegar | Inspecionar |
| 9 | Um alerta de teste percorreu todo o caminho e aparece no registro com horário, decisão e ação | Inspecionar |
| 10 | Data no contrato e na agenda de quem participa | Reforçar |

## Leitura

- **"Não" no item 3:** o caso está em Trava. Não ligue; crie a verificação primeiro.
- **"Não" nos itens 1, 2 ou 4:** o mapa está incompleto. Volte a [Mapear](../medir/mapear.md) antes de ligar.
- **"Não" nos itens 5 a 9:** pode ligar em observação, sem ação automática nenhuma, até fechar as pendências. Sem esses itens, ninguém consegue provar se está funcionando.
- **"Não" no item 10:** marque a data agora. Leva um minuto.
