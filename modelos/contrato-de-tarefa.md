# Contrato de tarefa

Uma página para **uma câmera, um evento e uma decisão.** É a saída do passo [Mapear](../medir/mapear.md) e a base de tudo o que vem depois: o prompt, o nível de controle, os sensores e a revisão.

Adaptado de `playbook/task-contract.md` do [harness-medir](https://github.com/tecosodreaboutdigital/harness-medir). Lá, a frase que justifica o modelo é a mesma que vale aqui: nenhum sensor corrige o que ninguém disse antes que queria.

Copie o bloco, apague este preâmbulo e preencha todos os campos. Não deixe campo em branco: escreva "não se aplica" ou "pendente, dono: <nome>" em vez de apagar.

---

```
# Contrato de tarefa: <nome curto do caso>
Versão: <v1>   Data: <dd/mm/aaaa>   Responsável: <nome de uma pessoa, não de um setor>

## Caso de uso em uma frase
Câmera: <qual câmera ou cena>
Evento: <o que a IA deve detectar>
Decisão: <que decisão o alerta alimenta, e quem a toma>

## Entrega
<O que um alerta correto produz para o operador. Concreto o bastante para que
duas pessoas reconheçam a mesma saída como certa.>

## Nunca faz
<Tudo o que está fora do escopo. Ex.: nunca aciona a polícia, nunca bloqueia
acesso, nunca identifica pessoa pelo nome, nunca grava em sistema do cliente.>

## Nível de controle
Nível: <N1, N2, N3 ou Trava>
Linha da tabela que o definiu: <copie a condição de nivel-de-controle.md>
Quem confirma no vídeo: <função>   Prazo: <minutos>
Quem autoriza a ação: <função, se N3>   Prazo: <minutos>
Se ninguém responder no prazo: <o que acontece; nunca "a IA age sozinha">

## Verificação
<Como se confere se o alerta estava certo: segundo sensor, vídeo gravado,
conferência em campo. Se não existe, o nível é Trava.>

## Ferramentas
<Lista fechada do que o modelo pode consultar ou acionar, e como cada uma falha.>

## Conhecimento necessário
<Trecho do protocolo, escala do turno, áreas liberadas. E o que ele NÃO precisa
carregar para fazer o trabalho.>

## Pronto quando
<Condição verificável de um alerta bem tratado. Ex.: alerta com decisão
registrada (aceite ou recusa, com motivo) em até <N> minutos.>

## Metas e sensores
Falsos positivos aceitos a cada mil alertas: <número>
Tempo até a triagem (mediana / pior caso aceito): <min / min>
Alertas por operador por hora (limite): <número>
Outros sensores: <ver sensores.md>

## Revisão
Próxima revisão do harness: <data>   Quem participa: <funções>
```

---

## Exemplo preenchido (fictício)

```
# Contrato de tarefa: fumaça fora da cerca, site remoto
Versão: v1   Data: 21/10/2026   Responsável: coordenador da central

## Caso de uso em uma frase
Câmera: térmica do perímetro norte do site remoto de energia
Evento: fumaça ou foco de calor fora da cerca
Decisão: despachar ou não equipe de campo; quem decide é o operador da central

## Entrega
Alerta com imagem térmica e trecho de vídeo, hipótese mais provável e
alternativas (queimada agrícola, poeira, reflexo), e o que verificar em 60 s.

## Nunca faz
Nunca despacha equipe sozinho. Nunca libera a chave digital do gabinete.
Nunca aciona órgão externo.

## Nível de controle
Nível: N3
Linha da tabela que o definiu: alguém age no mundo real de forma difícil de desfazer
Quem confirma no vídeo: operador da central   Prazo: 5 minutos
Quem autoriza a ação: supervisor de plantão   Prazo: 10 minutos
Se ninguém responder no prazo: escala para o coordenador; a IA não age

## Verificação
Vídeo visível da câmera vizinha e, quando houver, confirmação da equipe em campo.

## Ferramentas
Consultar os últimos 10 minutos de vídeo das duas câmeras do perímetro.
Abrir chamado vinculado ao alerta. Falha de consulta aparece como falha.

## Conhecimento necessário
Procedimento de incêndio do site, escala de plantão. Não precisa de cadastro
de pessoas nem do controle de acesso.

## Pronto quando
Todo alerta crítico tem decisão registrada em até 5 minutos.

## Metas e sensores
Falsos positivos aceitos a cada mil alertas: a combinar no piloto
Tempo até a triagem: mediana 2 min / pior caso 5 min
Alertas por operador por hora (limite): a combinar no piloto
Outros sensores: disponibilidade por câmera; discordâncias com motivo

## Revisão
Próxima revisão do harness: 30 dias após ligar   Quem participa: coordenador, operador, supervisor
```
