# Como contribuir

Este repositório é construído pela comunidade que participou da Oficina Prática de IA na Segurança e por quem mais operar CFTV e monitoramento. As próximas versões saem do que acontece nas operações de vocês.

## O que você pode trazer

| Tipo | Onde entra | Formato |
|---|---|---|
| Um caso real, anonimizado | `casos/` | [casos/_modelo.md](casos/_modelo.md) |
| Um erro que virou regra | `medir/reforcar.md` ou o caso correspondente | [abaixo](#erro-que-virou-regra) |
| Um sensor que produziu evidência | `modelos/sensores.md` | [abaixo](#sensor) |
| Uma pergunta, correção ou melhoria | O arquivo em questão | Issue ou pull request |

## Fluxo

**Por issue (mais simples).** Abra uma issue com um destes prefixos no título: `[caso]`, `[regra]`, `[sensor]`, `[pergunta]` ou `[correção]`. Cole o texto no formato indicado. Um mantenedor revisa a anonimização e transforma em arquivo.

**Por pull request.**

1. Faça um fork e crie uma branch com nome curto (ex.: `caso-varejo-doca`).
2. Faça a alteração. Um assunto por pull request.
3. Na descrição, diga o tipo de contribuição e confirme que passou o checklist de anonimização.
4. Um mantenedor revisa anonimização, clareza e coerência com a terminologia do repositório. Pode pedir ajustes.
5. Depois de aprovada, a mudança entra no [CHANGELOG](CHANGELOG.md) na próxima versão.

Quem não usa GitHub pode trazer a contribuição para o grupo da comunidade; um mantenedor transcreve, já anonimizada, e abre a issue.

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

- Português do Brasil, formal e direto.
- **Nunca use travessão.** Use vírgula, dois pontos, parênteses ou ponto final. Hífen é permitido.
- Use a terminologia do repositório: **nível de controle** (N1, N2, N3, **Trava**), **operador confirma**, **alerta é hipótese**, **harness**, **sensor**.
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

## Licença das contribuições

Contribuições são aceitas sob a [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.pt-br), a mesma licença do repositório (veja [LICENSE](LICENSE)). Ao abrir uma issue ou pull request, você declara que tem direito de compartilhar o conteúdo e concorda que ele seja publicado sob essa licença, com crédito no histórico do repositório.
