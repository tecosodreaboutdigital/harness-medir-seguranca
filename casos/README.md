# Casos

Casos de uso de IA em segurança eletrônica, contados pelo ciclo MEDIR e **sempre anonimizados em nível de setor.** Um caso aqui não é propaganda nem estudo de mercado: é o registro de como uma operação mapeou, equipou, delegou, inspecionou e reforçou, inclusive o que deu errado.

## Casos de exemplo (v0.1)

Quatro casos curtos, descritos só em nível de setor, a partir da palestra que deu origem ao repositório. Não trazem resultados medidos; servem de modelo de escrita e de ponto de partida para discussão.

| # | Setor | O que mostra |
|---|---|---|
| [01](01-industria-efetivo-por-area.md) | Indústria de bens de consumo | O problema era de processo, não de perímetro; o dado já existia |
| [02](02-terminal-de-graneis-evidencia.md) | Terminal de granéis | A IA não decide a disputa, ela produz a evidência |
| [03](03-sites-remotos-de-energia.md) | Sites remotos de energia | O operador confirma no vídeo antes de despachar |
| [04](04-grandes-eventos.md) | Grandes eventos | A decisão é do comando, e cada aceite ou recusa fica registrado |

O padrão comum aos quatro: **a IA detecta e recomenda; um humano confirma e decide; tudo vira registro.**

## Como enviar um caso

1. Copie [_modelo.md](_modelo.md) para um arquivo novo nesta pasta, com o nome `NN-setor-tema.md` (ex.: `05-varejo-doca.md`).
2. Preencha todos os campos. Campo que você não pode contar por confidencialidade leva "não informado", nunca um dado aproximado que identifique.
3. Passe o **checklist de anonimização** do modelo, item por item.
4. Abra um pull request, ou uma issue com o texto, seguindo [CONTRIBUTING.md](../CONTRIBUTING.md).

Antes de entrar no repositório, todo caso é revisado por um mantenedor só para anonimização e clareza. Na dúvida, o caso volta para ajuste; nada é publicado "para corrigir depois".

## O que torna um caso útil

- **Uma câmera, um evento, uma decisão.** Casos amplos demais ("IA em toda a planta") não ensinam nada.
- **O nível de controle e a linha que o definiu.**
- **Pelo menos um erro e o que mudou depois dele.** Caso sem erro costuma ser caso mal observado.
- **Números com unidade e período**, quando puder compartilhar: falsos positivos a cada mil alertas, tempo até a triagem, alertas por operador por hora. Sem números, diga o que seria medido.
