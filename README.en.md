# The MEDIR harness for security operations

*Read in [Português](README.md) · [Español](README.es.md). Website: [tecosodreaboutdigital.github.io/harness-medir-seguranca](https://tecosodreaboutdigital.github.io/harness-medir-seguranca/en/), in English, Portuguese and Spanish.*

The MEDIR cycle applied to CCTV and monitoring: one-page templates, control level rules, anonymized cases and agent skills for anyone putting AI inside a security control room without handing the decision to the machine.

This repository started at the Practical AI in Security workshop, presented by Teco Sodré at SegSummit in October 2026, and is built together with the workshop community.

Status: v0.2, first expansion: a website in three languages and seven agent skills. See the [CHANGELOG](CHANGELOG.md) (in Portuguese).

---

## The idea in one line

**Agent = model + harness.** The model is what sees and writes. The harness is everything around it: the context, the rules, who decides, what gets measured and what changes after a mistake. Everyone has the same models. The harness is what makes AI trustworthy in your operation, and nobody sells it off the shelf.

Three rules:

1. **Every alert is a hypothesis, never proof.** The algorithm flags, the protocol decides.
2. **The operator confirms.** Anything hard to undo goes through a person, always.
3. **No verification, no responsible autonomy.** If nobody can check the alert, nothing is delegated.

## The MEDIR cycle

| Step | Question | In CCTV |
|---|---|---|
| **Map** | Which task, at what risk? | One camera, one event, one decision. The control level comes out of here. |
| **Equip** | What does the model need to know and do? | Role, protocol, control level, short answer format, minimal tools. |
| **Delegate** | How much can it do alone? | Autonomy declared per use case, never per vendor. |
| **Inspect** | How do we know it works? | Sensors that produce evidence: false positives per thousand alerts, time to triage, alerts per operator per hour, logged disagreements. |
| **Reinforce** | What changes after a mistake? | Every mistake becomes a permanent change in the environment, with a date and a version. |

In Portuguese the initials (Mapear, Equipar, Delegar, Inspecionar, Reforçar) spell *medir*, "to measure".

## Control level

Apply in order; the first true row sets the level. **A higher N means more human control, not more freedom for the machine.**

| If... | Level | Who decides |
|---|---|---|
| when the alert fires, someone acts in the real world in a way that is hard to undo | **N3** | The AI flags; the operator confirms on video and another person authorizes. |
| the system reads from or writes to a third party's system, or the event happens more than 100 times a month, or the action has effects outside the control room | **N2** | The AI flags and recommends; the operator confirms before acting. |
| the action is internal, easy to undo and has no third-party integration | **N1** | The AI may act alone, always logged. |
| there is no way to check whether the alert was right | **Lock** | Delegate nothing yet. The Lock overrides every row until a verification exists. |

## What is in the repository

- [Website](https://tecosodreaboutdigital.github.io/harness-medir-seguranca/en/) (source in [docs/en/](docs/en/index.html)): the five steps, the [templates](docs/en/modelos.html) and the [skills](docs/en/skills.html) in English. Static HTML and CSS, no JavaScript; only the IBM Plex fonts come from Google Fonts, with a system font fallback.
- [skills/](skills/README.md): seven skills in the open Agent Skills format, each with a harness section (what it may do, what it must never do, who confirms). Instructions in Portuguese, with an English summary at the top of each file.
- [medir/](medir/mapear.md), [modelos/](modelos/contrato-de-tarefa.md) and [casos/](casos/README.md): the steps, templates and cases in Portuguese Markdown.

## Contributing

Cases, mistakes that became rules, sensors, skills, questions and translations are welcome through issues or pull requests. Everything is anonymized: no client, city, public body, vendor, equipment model, price or person. See [CONTRIBUTING.md](CONTRIBUTING.md) (in Portuguese; issues in English or Spanish are fine).

## Authorship and license

MEDIR method and original series: Teco Sodré, in [harness-medir](https://github.com/tecosodreaboutdigital/harness-medir). Adaptation to electronic security: Teco Sodré, WeSAFER and AVANTIA, with community contributions recorded in the repository history.

Content licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). © 2026 Teco Sodré, WeSAFER and AVANTIA. You may use and adapt it, including commercially, with attribution. Full legal text in [LICENSE](LICENSE).
