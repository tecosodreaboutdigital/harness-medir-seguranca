# Sensores

Métricas que produzem evidência, não opinião. Usadas no passo [Inspecionar](../medir/inspecionar.md) e escritas no [contrato de tarefa](contrato-de-tarefa.md) antes de ligar.

Três regras valem para todos:

1. **Quem avalia não é quem executa.** A IA não atesta a própria taxa de acerto; a conferência vem do operador, do vídeo, de um segundo sensor ou de campo.
2. **Todos os alertas, não uma amostra escolhida.** Revisar só o que virou ocorrência esconde o custo.
3. **Todo sensor tem limite e dono.** Número sem limite não dispara nada; limite sem dono não muda nada.

---

## 1. Falsos positivos a cada mil alertas

| Campo | Definição |
|---|---|
| O que mede | Quantos alertas, a cada mil, foram conferidos e descartados como falsos |
| Cálculo | (alertas descartados como falsos ÷ alertas conferidos) × 1.000, por câmera e por evento |
| Fonte | Decisão registrada do operador em cada alerta |
| Limite | A meta combinada antes de ligar, escrita no contrato |
| Sinal de alerta | Uma câmera concentrando a maior parte dos falsos; subida depois de mudança de estação, iluminação ou obra |
| Armadilha | Contar alertas não conferidos como verdadeiros. Alerta sem decisão registrada entra como "não conferido", nunca como acerto |

## 2. Tempo até a triagem

| Campo | Definição |
|---|---|
| O que mede | Tempo entre o alerta chegar à central e a primeira decisão registrada do operador |
| Cálculo | Mediana e pior caso (ou o percentil 90) por turno e por nível de controle |
| Fonte | Horário do alerta e horário da decisão no registro |
| Limite | O prazo do contrato. Exemplo de critério de piloto: alarme crítico triado em até 5 minutos |
| Sinal de alerta | Pior caso subindo enquanto a mediana fica estável: alguns alertas estão sendo esquecidos na fila |
| Armadilha | Medir só a média. Um alerta crítico esquecido por meia hora some dentro de uma média boa |

## 3. Alertas por operador por hora

| Campo | Definição |
|---|---|
| O que mede | A carga cognitiva do operador, medida como se mede downtime |
| Cálculo | Alertas recebidos ÷ operadores no turno ÷ horas, por hora do dia |
| Fonte | Registro de alertas e escala do turno |
| Limite | Combinado com a coordenação da central antes de ligar |
| Sinal de alerta | Subida depois de ligar um analítico novo. Se o ganho de IA virou aumento de volume, o projeto falhou |
| Armadilha | Olhar só o total do dia. A carga que importa é a do pico, de madrugada, com um operador sozinho |

## 4. Discordâncias registradas

| Campo | Definição |
|---|---|
| O que mede | Quantas vezes o operador discordou da hipótese ou da recomendação da IA, e por quê |
| Cálculo | Discordâncias ÷ alertas conferidos, com os motivos agrupados (cena, clima, regra, contexto que a IA não tinha) |
| Fonte | Campo de discordância na interface do operador |
| Limite | Não existe valor certo. Zero discordância por semanas é sinal de problema: ou a interface não deixa discordar, ou ninguém está olhando |
| Sinal de alerta | O mesmo motivo se repetindo. Ele aponta a regra ou o limiar que precisa de [reforço](../medir/reforcar.md) |
| Armadilha | Interface que não permite discordar. Esse é defeito de projeto, não de operador |

## 5. Falha de infraestrutura

| Campo | Definição |
|---|---|
| O que mede | Câmeras, rede, gravação e servidores fora do ar, para que falha nunca apareça como "nada aconteceu" |
| Cálculo | Disponibilidade por câmera (tempo com imagem válida ÷ tempo total) e número de alertas de falha por semana |
| Fonte | Monitoramento do sistema de gravação e da rede, com alerta próprio de falha |
| Limite | Toda câmera de caso em N2 ou N3 fora do ar gera alerta para o operador, na hora |
| Sinal de alerta | Área sem nenhum alerta por tempo incomum. Silêncio pode ser cegueira |
| Armadilha | Painel que mostra só eventos detectados. Câmera caída e área tranquila parecem iguais |

---

## Registro mínimo de cada alerta

Sem registro, nenhum sensor acima existe. Cada alerta guarda, no mínimo:

```
data e hora do alerta
câmera e evento
confiança informada pelo modelo
versão do contrato e do prompt em uso
nível de controle do caso
decisão do operador (confirmou, descartou, escalou) e horário
discordância (sim ou não) e motivo
ação tomada, quem autorizou e horário
falha de infraestrutura envolvida (sim ou não)
```

A versão do contrato e do prompt é o campo mais esquecido e um dos mais importantes: sem ela, uma mudança de comportamento depois de uma troca de regra ou de modelo não tem explicação.

---

## Proponha um sensor

Mediu algo que produziu evidência na sua central? Proponha no formato de [CONTRIBUTING.md](../CONTRIBUTING.md#sensor).
