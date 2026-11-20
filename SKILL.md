---
name: legalizar-viaje
description: Prepara y llena en SAP Concur las solicitudes de viaje (Travel Request) y las legalizaciones (Expense Report/Claim) de cualquier empleado de la Alliance of Bioversity International and CIAT (entidad CIAT o Bioversity, cualquier sede) a partir de recibos, tiquetes y pases de abordar, y arma la hoja de gastos de soporte en Excel y PDF. Úsala siempre que alguien mencione Concur, legalizar, reporte de gastos, solicitud de viaje, anticipo, viáticos, per diem, DSA o recibos de un viaje, o diga "tengo que legalizar el viaje a…", "ayúdame con Concur", "me devolvieron el reporte" o "hazme la solicitud de viaje", aunque no nombre la skill. EN — Alliance SAP Concur travel requests and expense reports/claims from receipts; trigger on "expense report", "expense claim", "travel request", "per diem", "Concur", "my report was sent back". FR — note de frais, demande de voyage.
---

# Legalizar viajes en SAP Concur (Alliance Bioversity–CIAT)

El objetivo es que el empleado dedique minutos, no horas, a Concur: tú lees los recibos, clasificas, calculas, digitas y adjuntas; la persona decide lo que solo ella sabe, hace los pocos pasos que el navegador no puede hacer, y envía. Los reportes se devuelven casi siempre por lo mismo (campo obligatorio vacío, tipo de gasto equivocado, fecha que no coincide con el recibo, falta un soporte, días personales sin declarar), así que la revisión previa vale tanto como la digitación.

**Idioma:** conversa en el idioma de la persona (español, inglés, francés…). Lo que se escribe en Concur (propósitos, comentarios) y la hoja de gastos van en inglés, que es lo que leen los procesadores.

Hay dos modos. Decide cuál por lo que pida:

- **Solicitud (Travel Request, TR)**: antes del viaje. Sin TR aprobada no se puede gastar ni viajar.
- **Legalización (Expense Report / Expense Claim)**: después del viaje. Plazo: **15 días calendario** desde el regreso (con tarjeta corporativa la portada de Concur habla de 40 días; apunta a 15). Si ya va tarde, dilo al empezar.

Archivos de la skill (léelos cuando el paso lo indique):

- `references/alliance-concur.md`: tipos de gasto, reglas de la política de viajes, diferencias CIAT/Bioversity, sedes, y lo visto en la pantalla real de Concur.
- `references/navegador-concur.md`: cómo manejar Concur en el navegador sin errores, copiar líneas, adjuntar recibos y qué no puede hacer el navegador.
- `scripts/hoja_gastos.py` y `assets/ejemplo_hoja.json`: generan la hoja de gastos de soporte (Excel + PDF).
- `assets/perfil-plantilla.md`: plantilla del perfil de cada usuario.

## Reglas que no se negocian

- **Nunca enviar (Submit Report) ni aprobar** reportes o solicitudes. Al enviar, el viajero certifica que los gastos son reales; esa firma es suya. Todo queda en borrador.
- **Nunca escribir credenciales** ni aprobar el Authenticator; si Concur pide sesión, la inicia la persona.
- **Nunca inventar un dato.** Un recibo ilegible o un monto que no aparece (p. ej. un aviso de tren sin precio) se marca como pendiente y se pregunta. Un valor inventado en un reporte de gastos es un problema serio para el viajero.
- **Nunca borrar** recibos, archivos ni líneas sin que lo pida. En Concur el ícono de Delete está pegado al de Attach (ver navegador §5).
- No mover ni renombrar los archivos originales: trabajar con copias.
- Trabajar solo en la cuenta que la persona abrió y le corresponde manejar (la suya, o la de alguien que la tiene como delegada en Concur). Si la cuenta abierta es de otra persona, dilo y confirma antes de tocar nada.

## Primer uso: el perfil

El perfil guarda lo que no cambia de un viaje a otro (entidad, sede, Accounting Office, moneda de reembolso, tarjeta corporativa, códigos habituales, agencia de viajes, cómo prefiere trabajar). Vive **fuera de la skill**, en `~/.claude/legalizar-viaje/perfil.md` (en Windows, `%USERPROFILE%\.claude\legalizar-viaje\perfil.md`), para que no se comparta al pasar la skill a otros ni se pierda al actualizarla.

- Si existe, léelo al empezar.
- Si no existe, créalo con `assets/perfil-plantilla.md`, llenando lo que veas en Concur (campo UNIT, entidad, Accounting Office, códigos recientes, idioma de la interfaz) y preguntando solo lo que falte. Muéstrale a la persona qué guardaste.
- Si ayudas con la cuenta de un colega, no guardes su perfil ahí salvo que la persona lo pida (puede ir en `~/.claude/legalizar-viaje/perfiles/<nombre>.md`).

## Al empezar: el mensaje de arranque

Antes de tocar Concur, manda **un solo mensaje** que deje a la persona con toda la información, para que no se sorprenda cuando le pidas algo a mitad del trabajo. Debe incluir:

1. **Qué vas a hacer**, en 4–6 pasos cortos.
2. **Qué necesitas**, como lista para revisar (adapta al caso):
   - Concur abierto con sesión iniciada (en el panel Browser de Claude o en Chrome con la extensión de Claude), en la cuenta del viajero.
   - Los recibos del viaje (fotos o PDF) en la carpeta de Descargas o pegados en el chat, incluidos Uber/taxis.
   - El correo o factura de la agencia con el **precio del tiquete**, y los **pases de abordar** de ida y regreso.
   - Billetes de tren o bus con su **precio** (un aviso de viaje sin precio no sirve).
   - Si alguna comida la dio el evento u organizador, y si hubo anticipo.
   - Si el procesador de su sede pide un formato propio de hoja de gastos, el archivo de ejemplo.
3. **Cuándo va a tener que intervenir** (usa esta tabla):

   | Momento | Qué hace la persona | Por qué |
   |---|---|---|
   | Al inicio | Iniciar sesión en Concur si hace falta | Las credenciales son suyas |
   | Tras leer los recibos | Responder preguntas de decisión (días personales, quién pagó qué, tarjeta, moneda de reembolso) | Solo ella lo sabe |
   | Tras cargar las líneas | Subir los soportes a "Available Receipts" (unos clics) | El navegador no puede subir archivos |
   | Tras adjuntar los recibos | Subir el PDF de la hoja de gastos en "Report Attachments" | Mismo motivo |
   | Al final | Revisar y enviar el reporte | La firma es del viajero |

4. **Cuánto toma**: con unos 20 recibos, cargar y adjuntar en Concur lleva del orden de una hora de trabajo en el navegador. Avísale que, si toca el botón de detener o escribe mientras trabajas, el paso en curso se corta; que no pasa nada, solo hay que decirte "sigue".
5. **Primeras preguntas**, solo las indispensables para arrancar (de quién es el viaje, dónde están los archivos). Las de decisión van después de leer los recibos.

Si la persona prefiere ir "uno por uno", plantea las decisiones de a una, con botones, y avanza en cuanto responda cada una.

### Si no hay navegador disponible

Si ni el panel Browser ni Chrome están conectados, igual puedes hacer los pasos 2–5 y 8 (leer, clasificar, preguntar, preparar la carpeta y la hoja de gastos) y entregar una tabla en el orden en que se digita, con cada campo de Concur, para que la persona la cargue a mano. Dilo al empezar.

## Modo legalización

### 1. Ubicar Concur y la cuenta

Sigue `references/navegador-concur.md` §1: encuentra la pestaña de Concur y **lee de quién es la cuenta** en el menú de perfil. Revisa la portada: solicitudes aprobadas sin reporte, reportes en borrador, aprobaciones pendientes (estas no se tocan).

Abre la TR del viaje (Requests → la solicitud) y anota: ID, fechas, propósito, código presupuestal o AEC, Accounting Office y **cada línea aprobada** (tipo y monto). Las líneas que no estén en la TR igual se pueden cargar, pero llevan explicación. Si hay un conector de Outlook disponible, los avisos de Concur (remitente `concursolutions.com`) también sirven para ubicar la TR.

### 2. Reunir los soportes

- Busca en Descargas los archivos recientes (macOS/Linux: `ls -lt ~/Downloads | head`; Windows: `Get-ChildItem $HOME\Downloads | Sort-Object LastWriteTime -Descending | Select-Object -First 15`).
- Los nombres de WhatsApp en macOS traen un espacio especial antes de "AM/PM": copia con comodín (`cp ~/Downloads/WhatsApp\ Image\ 2026-11-20\ at\ 11.10.21*`) en vez de escribir el nombre.
- Los PDF e imágenes se leen directo con Read. Con muchas fotos, arma una hoja de contacto (miniaturas con PIL y su nombre de archivo) para leerlas de una vez y saber qué archivo es cada recibo. Para usar PIL no ejecutes Python con `-I` (no encuentra los paquetes del usuario).
- Fíjate en lo que aparezca mientras trabajas: la persona suele ir agregando archivos (pases, tiquetes, billetes).

### 3. Leer y clasificar

De cada soporte saca: fecha y hora, proveedor, ciudad, valor, moneda, **últimos dígitos de la tarjeta** y qué se compró. Luego:

- **Tipo de gasto** según `references/alliance-concur.md` §0.6 y §1: comidas → "Meals and incidentals" (una línea por recibo en zona urbana); Uber/taxi → "Local Transport"; tiquete aéreo → "Fare Int." o "Fare National"; tren o bus entre ciudades → "Fare National"; hotel → "Hotel / Room Allowance"; SIM, seguro, tasas → "Travel Expenses - General & miscellaneous"; visa → "Visas"; comida con invitados → "Representation - Hospitality Expenses".
- **Comida del día** por la hora: antes de las 11 desayuno, 11–17 almuerzo, después de las 17 cena; varios recibos chicos de la noche (tapas, bar) suman a la cena; un café suelto en tránsito puede ir como imprevisto.
- **Días oficiales vs. personales:** compara las fechas de la TR con los **pases de abordar** y con los lugares de los recibos. Si el vuelo de regreso es días después del fin de la TR, o hay recibos en una ciudad que no es la del evento, hay días personales: pregúntalo, no lo asumas.
- **Tope diario de comidas**: monto de M&I aprobado en la TR ÷ días. Señala los días que lo pasan.
- **Zona rural**: si el viaje fue rural, M&I se declara por día con porcentajes, sin recibos (ver referencia §3).

### 4. 🙋 Preguntas de decisión

Haz juntas (o de a una, si la persona lo prefiere) solo las que apliquen y no estén en el perfil:

- ¿Las tarjetas usadas son personales o corporativas? (Si hay corporativa, sus cargos llegan solos a "Available Expenses"; compruébalo en Card Transactions.)
- ¿Quién compró el tiquete aéreo (agencia de la Alliance o el viajero) y dónde está el precio?
- ¿Quién pagó el tren o bus, y cuánto costó?
- ¿Qué comidas dio el evento u organizador? ¿El hotel incluía desayuno?
- ¿Hasta qué día fue oficial el viaje? ¿El día de regreso cuenta como oficial? ¿Qué gastos de ese día fueron personales (p. ej. un desvío)?
- ¿Alguna comida fue compartida con otras personas? (Iría como Hospitality.)
- ¿Hubo anticipo? ¿De cuánto?
- Moneda de reembolso (Reimbursement Currency): Concur solo acepta las válidas para el Accounting Office de la persona; depende de la cuenta donde le reembolsan.

### 5. Preparar la carpeta del viaje

En la carpeta de Descargas crea `Legalizacion <número de reporte> - <viaje>/` y copia los soportes con nombres que empiecen por número de orden, fecha, proveedor y monto (`06 2026-10-26 Hotel X EUR48.00.JPG`). Dentro, una subcarpeta **`Para subir a Concur`** solo con lo que va al reporte (sin gastos personales ni avisos sin precio). Así cada recibo se reconoce en Concur sin abrirlo.

### 6. Crear el reporte y su encabezado

Desde la TR aprobada: botón **"Create Expense Report"** (arriba a la derecha). En el encabezado (Report Details → Report Header):

- **Reimbursement Currency**: la que respondió la persona. Sin ella Concur no deja enviar.
- **Personal Travel on this trip**: "Yes" si hubo días personales.
- **Comment**: una línea para el procesador, p. ej. "Official travel 25-30 Oct 2026 (30 Oct = return day). Personal days 31 Oct - 6 Nov at traveler's own cost; not claimed."

### 7. Cargar las líneas

Sigue `references/navegador-concur.md` §3–4 (orden seguro de campos, proveedor, Duplicate para comidas) y las diferencias por entidad de `references/alliance-concur.md` §0.8. Criterios:

- **Con tarjeta corporativa**: los cargos ya están en "Available Expenses". Agrégalos al reporte desde ahí (Add Expense → Select from Available Expenses), ponles el tipo y adjunta el recibo; no los crees a mano (quedarían duplicados). Quien tiene tarjeta corporativa no debería reclamar gastos de bolsillo salvo excepciones.
- **Gastos de bolsillo** (efectivo o tarjeta personal): Out-of-Pocket, comentario con el proveedor real y los últimos dígitos de la tarjeta. Usuarios de entidad CIAT: proveedor "(00000000) N/A" si el comercio no está registrado.
- **Tiquete de la agencia**: "Fare Int." (o "Fare National" si es dentro del país), **Company Paid**, proveedor = la agencia (buscarla por nombre), fecha = emisión del tiquete, monto del correo o factura de la agencia, comentario con número de e-ticket, vuelos y si el regreso incluye días personales.
- **Tren o bus pagado por el viajero**: "Fare National", Out-of-Pocket, fecha = compra, monto del billete.
- Fechas de compra de semanas antes del viaje generan la advertencia "transaction date is older than your company allows": agrega en el comentario "Transaction date is the purchase date (dd Mmm), bought in advance of travel on dd Mmm."
- **Anticipo**: los gastos de bolsillo se descuentan del anticipo; si sobra, línea "Cash Advance Return" por el saldo (referencia §5).
- **Días personales**: sus gastos no se cargan. Si el tiquete costó más por esos días, la diferencia va como "A/R Employees for Travel and Office Expenses" (hace falta una cotización con regreso en la fecha oficial para calcularla; si no la hay, avísalo).

Al terminar, compara el número de líneas y el total con tu tabla.

### 8. Hoja de gastos de soporte (Excel + PDF)

Algunos procesadores piden una hoja con el per diem por día y los demás gastos. Si la persona tiene un modelo de su sede, léelo y respeta su formato. Si no, usa el script:

1. Arma un JSON como `assets/ejemplo_hoja.json`: por día, los montos de cada recibo en moneda local y **la tasa que aplicó Concur ese día** (está en cada línea); en "otros", Uber, taxis, tren; en "notas", días personales y el tiquete Company Paid (va como nota, no en el total).
2. Ejecuta `python3 <ruta de la skill>/scripts/hoja_gastos.py datos.json "<carpeta>/Travel expenses <viaje>.xlsx" "<carpeta>/Para subir a Concur/<n> Travel expenses <viaje>.pdf"`. Necesita `openpyxl`; para el PDF, `reportlab` (si falta, el script lo dice y la persona puede exportar el Excel a PDF desde Excel).
3. El total que imprime debe ser **igual** a lo que Concur le reembolsa al viajero (total del reporte menos lo Company Paid). Si difiere en centavos, revisa las tasas.
4. Concur solo acepta imágenes y PDF como soporte: el PDF es el que se sube.

### 9. 🙋 La persona sube los soportes

Dale las instrucciones de `references/navegador-concur.md` §7, ábrele la carpeta (macOS: `open "<carpeta>/Para subir a Concur"`; Windows: `explorer "<carpeta>\Para subir a Concur"`) y deja Concur en Expense → Manage Expenses, bajado hasta "Available Receipts". Cuando diga que ya están, verifica que aparezcan todos por nombre.

### 10. Adjuntar los recibos

Sigue `references/navegador-concur.md` §5, gasto por gasto, verificando el nombre del archivo adjuntado. Para el tiquete, adjunta el correo o factura de la agencia y suma los pases de abordar.

### 11. 🙋 La persona sube el PDF de la hoja al reporte

Manage Receipts → Manage Attachments → **Add** abre el selector de archivos del computador: lo hace ella (`references/navegador-concur.md` §6). Luego verifica que el contador de páginas subió.

### 12. Revisión final y resumen

- Abre "View Alerts": debe haber **0 errores**. Explica cada advertencia que quede (las del anticipo y "reconcile Fare" son recordatorios fijos que no desaparecen).
- Confirma que ninguna línea queda sin recibo.
- Entrega el resumen en una tabla que separe lo que paga la empresa de lo que se reembolsa. Esta distinción confunde: explícala con palabras simples ("el tiquete lo pagó la Alliance a la agencia; no se te devuelve, solo se registra").

  | | Moneda de reembolso |
  |---|---|
  | Pagado por la Alliance (Company Paid / tarjeta corporativa) | … |
  | Lo que se le reembolsa al viajero (Out-of-Pocket, menos anticipo) | … |
  | **Total del reporte** | … |

- Lista lo que el procesador podría preguntar: días sobre el tope, comidas grandes que podrían ser compartidas, costo extra del tiquete por días personales, plazo vencido.
- Si aprendiste algo del perfil (moneda, agencia, códigos), actualiza el perfil.

### 13. 🙋 La persona envía

Dile exactamente dónde está el botón ("Submit Report", arriba a la derecha) y que al enviar el viajero certifica los gastos. Tú no lo envías.

## Modo solicitud

1. Datos mínimos: destino, fechas, propósito, código presupuestal o AEC, si necesita anticipo, y la cotización del tiquete de la agencia de su sede.
2. Arma el encabezado y los gastos esperados según `references/alliance-concur.md` §0.2 y §6. Estima hotel y M&I con las tarifas DSA (pide el valor del calculador de Power BI o deja que Concur lo calcule; no lo inventes). Si habrá días personales, marca "Personal Travel on this trip" desde ya.
3. Muestra el borrador: título (máximo 32 caracteres: dónde – cuándo – qué), propósito, fechas y gastos esperados.
4. Si lo pide, llénalo en Concur y déjalo sin enviar (Create Request guarda un borrador). Recuérdale adjuntar itinerario y cotización. Si hay tramos en tren o bus entre ciudades, inclúyelos como gasto esperado: así no quedan fuera de la TR al legalizar.

## Cuando le devuelven un reporte

Busca el aviso de Concur (correo de `AutoNotification@concursolutions.com`, si hay conector de Outlook, o el Report Timeline en Concur) con el comentario del procesador, identifica qué línea falló y por qué, propón la corrección concreta y, si quiere, corrígela en Concur sin reenviar.

## Mantener la skill al día

Si un campo, menú o mensaje no coincide con las referencias, detente, cuéntale qué viste y corrige la referencia que corresponda (o anótalo para quien mantiene la skill). Las guías de Finance son de 2023 y la pantalla cambia; cada sede y entidad tiene variantes.

Si la carpeta de la skill es un repo de git, después de corregir haz commit con un mensaje que diga qué cambió (sin datos de personas) y pregunta antes de hacer push. Para empaquetar un `.skill` desde el repo, excluye `.git`, `README.md` y `.gitignore` (p. ej. `git archive --prefix=legalizar-viaje/ HEAD -- SKILL.md references scripts assets`).

## Privacidad

- Los recibos tienen datos personales y financieros. Trabaja con archivos locales; no los subas a servicios externos ni los pegues en búsquedas web.
- Los perfiles viven fuera de la skill; no los copies dentro de ella. Si actualizas las referencias, anota solo lo general (formularios, mensajes, códigos de oficina, agencias), nunca datos de una persona.
