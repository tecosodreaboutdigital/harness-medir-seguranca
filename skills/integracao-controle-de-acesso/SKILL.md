---
name: integracao-controle-de-acesso
description: Padrão de webhook somente leitura para receber eventos de controle de acesso e de RH (credencial revogada, desligamento, tentativa com credencial revogada) e levá-los à central como hipótese para o operador conferir, com payloads de exemplo e notas de LGPD para biometria (dado sensível, art. 11), consentimento, retenção e auditoria. Use ao integrar controle de acesso, RH ou cadastro biométrico a um agente de monitoramento. EN - read-only webhook pattern for access-control and HR sync events, with mock payloads and LGPD notes for biometrics.
license: CC-BY-4.0
metadata:
  author: Teco Sodré, WeSAFER e AVANTIA
  version: "0.2"
  medir: equipar
---

> **English summary.** Access-control and HR systems push signed webhook events (credential revoked, employee offboarded, attempt with a revoked credential) to a read-only adapter. The central uses them to inform the operator and to open a removal task for the system owner; the agent never grants, blocks or deletes anything itself. People are referred to by pseudonymous ids only. Includes LGPD notes for biometric data (sensitive personal data, art. 5 II and art. 11), consent and legal basis, retention and deletion (arts. 15 and 16), records of processing (art. 37) and security (art. 46), plus a security review checklist. Not legal advice.

# Integração com controle de acesso e RH

Uma credencial revogada que ainda abre a catraca, ou um rosto que continua cadastrado depois do desligamento, são falhas silenciosas: ninguém percebe até o dia em que importa. Esta skill liga o controle de acesso e o RH à central **para enxergar**, nunca para comandar.

## Quando usar

- Levar à central eventos como credencial revogada, desligamento e tentativa de acesso com credencial revogada.
- Manter cadastros sincronizados (lista de credenciais ativas, cadastro biométrico) sem dar ao agente poder de escrita.
- Revisar uma integração existente sob a ótica da LGPD.

## Harness desta skill

- **Pode:** receber eventos assinados, normalizar, descartar campos fora da lista, apresentar o evento ao operador como hipótese, abrir uma pendência de remoção para o dono do cadastro, registrar.
- **Nunca:** liberar ou bloquear acesso; criar, alterar ou excluir credencial ou cadastro biométrico; consultar o cadastro além do necessário para o evento; levar nome, documento, foto ou template biométrico ao modelo ou ao log; decidir sobre uma pessoa a partir de um único evento.
- **Quem confirma:** o operador confere no vídeo antes de qualquer ação com pessoa (abordar é N3: outra pessoa autoriza). A remoção de credencial ou de cadastro biométrico é feita pelo administrador do sistema, com registro. Base legal, retenção e relatório de impacto são decididos com o encarregado de dados (DPO).

## Fluxo

```
RH ──(desligamento)──▶ adaptador ──▶ pendência para o administrador do controle de acesso:
                                     "revogar credencial e remover cadastro biométrico de p-7f3a9c até <prazo>"
controle de acesso ──(credencial_revogada)──▶ adaptador ──▶ baixa da pendência (com horário)
controle de acesso ──(tentativa_com_credencial_revogada)──▶ adaptador ──▶ alerta ao operador, nível N2 ou N3
```

O agente fecha o ciclo **enxergando**: se o desligamento chegou e a revogação não chegou no prazo, isso vira alerta para a coordenação. Quem revoga é gente.

## Payloads de exemplo

Em [exemplos/](exemplos/), todos fictícios e com pessoa identificada só por `id_pessoa_pseudonimo`:

- [desligamento-rh.json](exemplos/desligamento-rh.json): o RH avisa o fim do vínculo.
- [credencial-revogada.json](exemplos/credencial-revogada.json): o controle de acesso confirma a revogação. Traz de propósito um campo `nome`, que o adaptador descarta.
- [acesso-negado.json](exemplos/acesso-negado.json): tentativa com credencial revogada num leitor, com a câmera associada.

Para testar, use o servidor da skill de gravação em outra rota:

```
export MOCK_WEBHOOK_SEGREDO="segredo-de-teste-local"
python ../integracao-vms/exemplos/servidor_mock.py --porta 8089 --caminho /webhook/acesso
python ../integracao-vms/exemplos/enviar_alerta_mock.py exemplos/credencial-revogada.json --url http://localhost:8089/webhook/acesso
```

O log mostra `campos_descartados=nome`: o nome nunca chega ao assistente. No Git Bash do Windows, defina `MSYS_NO_PATHCONV=1` antes, para que `/webhook/acesso` não seja convertido em caminho de disco.

## Notas de LGPD para biometria

Orientação geral para conversar com o encarregado de dados, não parecer jurídico. Texto da lei: [Lei nº 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm).

- **Biometria é dado pessoal sensível.** O art. 5º, II, inclui o dado biométrico entre os dados sensíveis, e o art. 11 lista as únicas hipóteses em que eles podem ser tratados.
- **Base legal antes de cadastrar.** O art. 11, I, admite o consentimento "de forma específica e destacada, para finalidades específicas". Na relação de trabalho, a liberdade desse consentimento pode ser questionada; por isso avalie com o encarregado outras hipóteses do art. 11, II, como a alínea "g" (prevenção à fraude e segurança do titular em processos de identificação e autenticação em sistemas eletrônicos), e registre a decisão.
- **Finalidade e necessidade.** O cadastro biométrico de controle de acesso serve ao controle de acesso. Usá-lo para outra finalidade (por exemplo, buscar a pessoa em outras câmeras) exige nova análise. Leve ao agente só o mínimo: id pseudônimo, leitor, área, horário.
- **Retenção e eliminação.** O tratamento termina quando a finalidade acaba (art. 15), e os dados devem ser eliminados, salvo as hipóteses de conservação do art. 16. Defina por escrito o prazo de remoção do template após desligamento ou revogação, e meça esse prazo como sensor.
- **Registro e auditoria.** Controlador e operador mantêm registro das operações de tratamento (art. 37). Registre quem removeu, quando e por qual evento, sem guardar o template no registro.
- **Segurança.** O art. 46 exige medidas técnicas e administrativas de proteção. A revisão de segurança abaixo é o mínimo.
- **Relatório de impacto.** A autoridade nacional pode exigir relatório de impacto, inclusive para dados sensíveis (art. 38). Biometria em escala é candidata natural a ter um pronto.

## Revisão de segurança

- [ ] **Autenticação:** webhook assinado com HMAC-SHA256; origens conhecidas; nada anônimo.
- [ ] **Menor privilégio:** o adaptador não tem credencial de escrita no controle de acesso nem no RH; se consultar algo, é leitura do mínimo necessário.
- [ ] **Somente leitura por padrão:** nenhuma rota libera, bloqueia, cria ou exclui; remoção é pendência para uma pessoa.
- [ ] **Segredos fora do repositório:** segredo do webhook em variável de ambiente ou cofre, com rotação.
- [ ] **Log sem dado pessoal:** só id pseudônimo, tipo, leitor, horário e resultado; nunca nome, documento, foto ou template.
- [ ] **Limite de taxa** por origem e limite de tamanho do corpo.
- [ ] **Proteção contra replay:** timestamp assinado, janela curta, recusa de `evento_id` repetido, relógios com NTP.
- [ ] **Pseudonimização:** a tabela que liga `id_pessoa_pseudonimo` à pessoa fica no sistema de origem, fora do alcance do agente.
- [ ] **Prazo de remoção medido:** desligamento sem revogação no prazo vira alerta para a coordenação.
- [ ] **Base legal e retenção registradas** com o encarregado de dados antes de ligar.

## Referências

- [Nível de controle](../../modelos/nivel-de-controle.md): consultar cadastro de outra empresa é N2; abordar pessoa é N3.
- [integracao-vms](../integracao-vms/SKILL.md): o servidor mock e o padrão de assinatura.
