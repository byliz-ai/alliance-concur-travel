# legalizar-viaje

Skill de Claude para preparar en **SAP Concur** las solicitudes de viaje (Travel Request) y las legalizaciones (Expense Report / Expense Claim) de cualquier persona de la **Alliance of Bioversity International and CIAT**, sea de la entidad CIAT o Bioversity y de cualquier sede.

*EN: Claude skill that prepares Alliance travel requests and expense reports in SAP Concur from receipts, and builds the supporting expense sheet (Excel + PDF).*

## Qué hace

- Lee recibos, tiquetes y pases de abordar (PDF o fotos) y arma la tabla de gastos.
- Hace las preguntas que solo la persona puede responder: días personales, quién pagó qué, anticipo, etc.
- Llena el reporte en Concur desde el navegador: encabezado, líneas y recibos adjuntos. Todo queda **en borrador**.
- Genera la hoja de gastos de soporte (Excel + PDF), con totales que cuadran al centavo con Concur.
- Al final entrega un resumen que separa lo que es Company Paid de lo reembolsable.

**Nunca** envía el reporte (Submit), ni aprueba nada, ni escribe contraseñas. Hay cuatro momentos en que la persona tiene que intervenir, y la skill los avisa desde el inicio: iniciar sesión, responder dudas, subir archivos y enviar el reporte.

## Instalar

**App de Claude (escritorio o claude.ai):** descarga `legalizar-viaje.skill` desde [Releases](../../releases) y súbelo en la configuración de skills (Capabilities → Skills).

**Claude Code:**

```bash
git clone https://github.com/byliz-ai/legalizar-viaje.git ~/.claude/skills/legalizar-viaje
```

Para actualizar: `git -C ~/.claude/skills/legalizar-viaje pull`.

## Qué se necesita

- Las skills activadas en Claude.
- Un navegador que Claude pueda manejar: el panel Browser de la app de Claude o la extensión Claude in Chrome. Sin navegador, la skill igual arma la tabla y la hoja de gastos, y la persona copia los datos a Concur.
- La sesión de Concur abierta por la persona (`eu2.concursolutions.com`).
- Python 3 con `openpyxl` (y `reportlab` para el PDF), para la hoja de gastos.

## Primer uso

La primera vez, la skill pregunta lo básico y lo guarda en `~/.claude/legalizar-viaje/perfil.md`: entidad, sede, unidad, moneda de reembolso, tarjeta corporativa, agencia y navegador. Ese perfil queda **solo en el computador de cada persona**; no va en este repo.

Para empezar basta con decirle a Claude algo como "tengo que legalizar el viaje a Roma" o "ayúdame con Concur".

## Contenido

| Archivo | Para qué |
|---|---|
| `SKILL.md` | Instrucciones de la skill: pasos, momentos en que interviene la persona, reglas |
| `references/alliance-concur.md` | Política y pantallas de Concur en la Alliance: tipos de gasto, CIAT vs Bioversity, sedes, agencias, contactos |
| `references/navegador-concur.md` | Cómo manejar los formularios de Concur desde el navegador |
| `scripts/hoja_gastos.py` | Genera la hoja de gastos (Excel + PDF) |
| `assets/ejemplo_hoja.json` | Ejemplo de datos para el script |
| `assets/perfil-plantilla.md` | Plantilla del perfil de cada persona |

## Estado

Probada de punta a punta en un reporte real de 23 líneas (CIAT, tarjeta personal, nov-2026). Estas partes salen de las guías de Finance y todavía no se han probado en vivo: el flujo con tarjeta corporativa, las particularidades de Bioversity y la opción de delegado. Si algo en Concur no coincide, la skill avisa y propone corregir la referencia.

## Privacidad

No subas a este repo recibos, hojas de gastos, perfiles ni datos de ninguna persona; el `.gitignore` bloquea los formatos más comunes. Antes de usar la skill con información financiera, confirma que la política de uso de IA de la Alliance lo permite.
