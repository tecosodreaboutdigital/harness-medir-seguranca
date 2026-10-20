# Como contribuir

Este repositório é construído com a comunidade A.I.S. (Agentes de IA = Modelo + Harness para Segurança Eletrônica, Monitoramento e Produtividade) e por quem mais operar CFTV e monitoramento. As próximas versões saem do que acontece nas operações de vocês.

## O que você pode trazer

| Tipo | Onde entra | Formato |
|---|---|---|
| Um caso real, anonimizado | `casos/` | [casos/_modelo.md](casos/_modelo.md) |
| Um erro que virou regra | `medir/reforcar.md` ou o caso correspondente | [abaixo](#erro-que-virou-regra) |
| Um sensor que produziu evidência | `modelos/sensores.md` | [abaixo](#sensor) |
| Uma skill para agentes | `skills/<nome>/SKILL.md` | [abaixo](#uma-skill) |
| Uma tradução ou ajuste de idioma | `docs/en/`, `docs/es/`, `README.en.md`, `README.es.md` | [abaixo](#traduções) |
| Uma pergunta, correção ou melhoria | O arquivo em questão | Issue ou pull request |

## Fluxo

**Por issue (mais simples).** Abra uma issue com um destes prefixos no título: `[caso]`, `[regra]`, `[sensor]`, `[pergunta]` ou `[correção]`. Cole o texto no formato indicado. Um mantenedor revisa a anonimização e transforma em arquivo.

**Por pull request.**

1. Faça um fork e crie uma branch com nome curto (ex.: `caso-varejo-doca`).
2. Faça a alteração. Um assunto por pull request.
3. Na descrição, diga o tipo de contribuição e confirme que passou o checklist de anonimização (e, se for skill de integração, a revisão de segurança).
4. Um mantenedor revisa anonimização, clareza e coerência com a terminologia do repositório. Pode pedir ajustes.
5. Depois de aprovada, a mudança entra no [CHANGELOG](CHANGELOG.md) na próxima versão.

Quem não usa GitHub pode trazer a contribuição para a [comunidade A.I.S. no WhatsApp](https://chat.whatsapp.com/FlXr6KUllRpCkjJz16uZYY); um mantenedor transcreve, já anonimizada, e abre a issue.

## Regras de anonimização

Valem para qualquer contribuição, em qualquer arquivo, inclusive em issues, comentários e mensagens de commit.

1. **Setor genérico, nunca o nome.** Escreva "indústria", "terminal de granéis", "sites remotos de energia", "grandes eventos", "varejo", "condomínio". Nada de cliente, empresa, marca ou grupo econômico.
2. **Sem lugar.** Nenhuma cidade, estado, bairro, endereço, porto, rodovia, aeroporto ou ponto de referência.
3. **Sem órgão, evento ou data identificável.** Nenhum órgão público, força de segurança identificada, festa, festival ou edição de evento.
4. **Sem fornecedor.** Nenhum nome de software, fabricante, integrador ou modelo de câmera e equipamento. Use a categoria: sistema de gravação, controle de acesso, leitura de placa, câmera térmica, reconhecimento facial.
5. **Sem preço.** Nenhum valor de contrato, preço de equipamento ou salário.
6. **Sem pessoa.** Nenhum nome, rosto, placa, crachá, voz ou imagem de pessoa real. Nenhuma imagem de câmera real, planta baixa, mapa ou print de sistema.
7. **Números em faixa quando o exato identifica.** "Dezenas de câmeras" em vez de "137 câmeras", se o número exato puder apontar a operação.
8. **Teste do colega.** Se alguém do seu cliente ou da sua equipe reconheceria a operação lendo o texto, ainda não está anônimo.

Na dúvida, não publique: pergunte na issue antes. Uma contribuição que fere estas regras é recusada ou devolvida para ajuste, mesmo que o restante esteja ótimo. Se algo identificável entrar por engano, avise um mantenedor imediatamente.

## Regras de escrita

- Português do Brasil, formal e direto. No site, inglês e espanhol seguem a seção [Traduções](#traduções).
- **Nunca use travessão.** Use vírgula, dois pontos, parênteses ou ponto final. Hífen é permitido.
- Use a terminologia do repositório: **nível de controle** (N1, N2, N3, **Trava**), **operador confirma**, **alerta é hipótese**, **harness**, **sensor**, **selo de integridade do dado**.
- Exemplos concretos valem mais que princípios. Uma câmera, um evento, uma decisão.
- Fato externo (lei, norma, estudo) leva a fonte, com link verificado. Não invente referência.

## Erro que virou regra

```
Data (mês e ano): <mm/aaaa>
Setor: <genérico>
Caso: <câmera, evento, decisão>
Nível de controle: <N1, N2, N3 ou Trava>
O que deu errado: <uma ou duas frases>
Em que passo estava a lacuna: <Mapear, Equipar, Delegar, Inspecionar ou Reforçar>
Mudança permanente: <regra, limiar, zona mascarada, treino, mudança de nível...>
Versão do harness em que entrou: <v>
Sensor que mostra se funcionou: <qual, e em quanto tempo>
```

## Sensor

```
Nome do sensor: <curto>
O que mede: <uma frase>
Cálculo: <fórmula, com unidade e período>
Fonte dos dados: <de onde vem cada número>
Limite: <a partir de que valor alguém age, e quem>
Sinal de alerta: <o padrão que indica problema>
Armadilha: <como esse número engana>
Onde foi usado: <setor genérico; resultado, se puder compartilhar>
```

## Uma skill

Skills ficam em `skills/<nome>/`, no formato aberto Agent Skills: uma pasta por skill, com um `SKILL.md` que começa com YAML. O nome da pasta é igual ao `name`, em letras minúsculas e hífens.

```
skills/<nome>/
  SKILL.md          obrigatório
  exemplos/         opcional: payloads fictícios, scripts só com biblioteca padrão
```

Estrutura mínima do `SKILL.md`:

```
---
name: <nome-da-pasta>
description: <o que faz e quando usar, em uma ou duas frases; termine com "EN - <resumo>">
license: CC-BY-4.0
metadata:
  author: <seu nome ou apelido>
  version: "<versão>"
  medir: <passo do ciclo>
---

> **English summary.** <três a cinco frases>

# <Título>

## Quando usar
## Harness desta skill
- **Pode:** <o que a skill pode fazer>
- **Nunca:** <o que ela nunca faz, inclusive sob pressão>
- **Quem confirma:** <função que confirma ou autoriza>
## Como fazer
## Formato de saída
## Regra inegociável      (uma regra, e as desculpas mais prováveis para quebrá-la)
## Revisão de segurança   (obrigatória em skill que toca sistemas)
## Referências
```

Regras para aceitar uma skill:

1. **A seção "Harness desta skill" é obrigatória**, com as três linhas: pode, nunca, quem confirma. Skill sem essa seção é devolvida, por melhor que seja o resto.
2. **Nenhuma ação difícil de desfazer sem confirmação humana.** A skill não executa nem recomenda executar abordar pessoa, bloquear ou liberar acesso, acionar a polícia, despachar equipe, apagar ou exportar gravação.
3. **Somente leitura por padrão.** Escrita em sistema de terceiro só com justificativa no texto e com o nível de controle revisto.
4. **Revisão de segurança** em toda skill que toca sistemas: autenticação, menor privilégio, somente leitura por padrão, segredos fora do repositório, log sem dado pessoal, limite de taxa e proteção contra replay em webhooks (HMAC com timestamp).
5. **Exemplos sem nada real.** Hosts `exemplo.local`, segredos de teste lidos de variável de ambiente, nenhum IP, credencial, token, URL de sistema real, rosto, placa ou nome de pessoa. Scripts só com a biblioteca padrão da linguagem, escutando só em `localhost`.
6. **Sem fornecedor.** Protocolos e ferramentas abertas (ONVIF, RTSP, REST, webhooks, Zabbix, MCP) são bem-vindos; nomes comerciais de sistemas de gravação, analíticos ou reconhecimento facial, não.
7. **Teste antes.** Diga no pull request com que alerta fictício você testou a skill e o que mudou com ela em relação a não usá-la.

O mantenedor lê a skill inteira antes de aceitar. Uma skill entra no catálogo de [skills/README.md](skills/README.md) e nas páginas de skills do site nos três idiomas.

## Traduções

O site existe em português, inglês e espanhol neutro da América Latina. Traduzir aqui é reescrever para quem opera uma central naquele idioma, não converter palavra por palavra.

- Mantenha a terminologia: nível de controle / control level / nivel de control; Trava / Lock / Bloqueo; e as três regras (alerta é hipótese, o operador confirma, sem verificação não há autonomia).
- Uma mudança de conteúdo no site entra nos três idiomas no mesmo pull request, ou abre uma issue `[tradução]` para quem puder completar.
- As mesmas regras de anonimização e de escrita valem em qualquer idioma, inclusive a de não usar travessão.

## Licença das contribuições

Contribuições são aceitas sob a [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br), a mesma licença do repositório (veja [LICENSE](LICENSE)). Ao abrir uma issue ou pull request, você declara que tem direito de compartilhar o conteúdo e concorda que ele seja publicado sob essa licença, com crédito no histórico do repositório.
