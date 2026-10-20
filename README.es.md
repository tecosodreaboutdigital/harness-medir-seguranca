# Harness MEDIR para seguridad electrónica

*Leer en [Português](README.md) · [English](README.en.md). Sitio: [tecosodreaboutdigital.github.io/harness-medir-seguranca](https://tecosodreaboutdigital.github.io/harness-medir-seguranca/es/), en español, portugués e inglés.*

El ciclo MEDIR aplicado al CCTV y al monitoreo: plantillas de una página, reglas de nivel de control, casos anonimizados y skills para agentes, para quien va a poner IA dentro de una central de seguridad sin entregarle la decisión a la máquina.

Este repositorio nació en el Taller Práctico de IA en Seguridad, presentado por Teco Sodré en SegSummit en octubre de 2026, y se construye junto con la comunidad del taller.

Estado: v0.2, primera expansión: un sitio en tres idiomas y siete skills para agentes. Vea el [CHANGELOG](CHANGELOG.md) (en portugués).

---

## La idea en una línea

**Agente = modelo + harness.** El modelo es lo que ve y escribe. El harness es todo lo que lo rodea: el contexto, las reglas, quién decide, qué se mide y qué cambia después de un error. Todos tienen los mismos modelos. El harness es lo que hace confiable a la IA en su operación, y nadie lo vende listo.

Tres reglas:

1. **Toda alerta es una hipótesis, nunca una prueba.** El algoritmo señala, el protocolo decide.
2. **El operador confirma.** Lo que es difícil de deshacer pasa por una persona, siempre.
3. **Sin verificación no hay autonomía responsable.** Si nadie puede comprobar la alerta, no se delega nada.

## El ciclo MEDIR

| Paso | Pregunta | En CCTV |
|---|---|---|
| **Mapear** | ¿Qué tarea, con qué riesgo? | Una cámara, un evento, una decisión. De aquí sale el nivel de control. |
| **Equipar** | ¿Qué necesita saber y hacer el modelo? | Rol, protocolo, nivel de control, respuesta corta, herramientas mínimas. |
| **Delegar** | ¿Cuánto puede hacer solo? | Autonomía declarada por caso de uso, nunca por proveedor. |
| **Inspeccionar** | ¿Cómo sabemos que funciona? | Sensores que producen evidencia: falsos positivos por cada mil alertas, tiempo hasta el triaje, alertas por operador por hora, desacuerdos registrados. |
| **Reforzar** | ¿Qué cambia después de un error? | Cada error se vuelve un cambio permanente en el entorno, con fecha y versión. |

## Nivel de control

Aplíquelo en orden; la primera fila verdadera define el nivel. **Un N más alto significa más control humano, no más libertad para la máquina.**

| Si... | Nivel | Quién decide |
|---|---|---|
| cuando se dispara la alerta, alguien actúa en el mundo real de una forma difícil de deshacer | **N3** | La IA señala; el operador confirma en el video y otra persona autoriza. |
| el sistema lee o escribe en un sistema de terceros, o el evento ocurre más de 100 veces al mes, o la acción tiene efecto fuera de la central | **N2** | La IA señala y recomienda; el operador confirma antes de actuar. |
| la acción es interna, fácil de deshacer y sin integración con terceros | **N1** | La IA puede actuar sola, siempre con registro. |
| no hay forma de comprobar si la alerta era correcta | **Bloqueo** | Todavía no delegue nada. El Bloqueo pasa por encima de todas las filas hasta que exista una verificación. |

## Qué hay en el repositorio

- [Sitio](https://tecosodreaboutdigital.github.io/harness-medir-seguranca/es/) (fuente en [docs/es/](docs/es/index.html)): los cinco pasos, las [plantillas](docs/es/modelos.html) y las [skills](docs/es/skills.html) en español. HTML y CSS estáticos, sin JavaScript; solo las fuentes IBM Plex vienen de Google Fonts, con una fuente del sistema como respaldo.
- [skills/](skills/README.md): siete skills en el formato abierto Agent Skills, cada una con una sección de harness (qué puede hacer, qué nunca hace, quién confirma). Instrucciones en portugués, con un resumen en inglés al inicio de cada archivo.
- [medir/](medir/mapear.md), [modelos/](modelos/contrato-de-tarefa.md) y [casos/](casos/README.md): los pasos, las plantillas y los casos en Markdown, en portugués.

## Cómo contribuir

Casos, errores que se volvieron reglas, sensores, skills, preguntas y traducciones son bienvenidos por issue o pull request. Todo se anonimiza: ningún cliente, ciudad, organismo público, proveedor, modelo de equipo, precio o persona. Vea [CONTRIBUTING.md](CONTRIBUTING.md) (en portugués; puede abrir issues en español).

## Autoría y licencia

Método MEDIR y serie original: Teco Sodré, en [harness-medir](https://github.com/tecosodreaboutdigital/harness-medir). Adaptación a la seguridad electrónica: Teco Sodré, WeSAFER y AVANTIA, con las contribuciones de la comunidad registradas en el historial del repositorio.

Contenido bajo [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/deed.es). © 2026 Teco Sodré, WeSAFER y AVANTIA. Puede usarlo y adaptarlo, incluso comercialmente, citando la fuente. Texto legal completo en [LICENSE](LICENSE).
