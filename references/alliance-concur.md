# Referencia: reglas y formularios de Concur en la Alliance

Fuentes (SharePoint Alliance-Finance): "SAP Concur guideline – TR (Travel Request)" y "SAP Concur Guideline – ER (Expense Report)" (oct. 2023), "SAP CONCUR Guideline – Alliance Workshops" (jul. 2024), Travel Policy PO-08-BOF v05 (ago. 2024) y la nota "Travel essentials in Europe" (nov. 2026), más lo visto llenando reportes reales (nov. 2026).

**La sección 0 manda sobre el resto**: es lo visto en la pantalla real. Las secciones 1–7 vienen de las guías y sirven para reglas y contexto; donde un nombre de campo o de tipo de gasto difiera, usar el de la sección 0. Cómo manejar el navegador está en `navegador-concur.md`.

Contenido: 0) Pantalla real (0.1 General · 0.2 Solicitud · 0.3 Crear el reporte · 0.4 Encabezado · 0.5 Detalle de un gasto · 0.6 Tipos de gasto · 0.7 Alertas · 0.8 CIAT vs. Bioversity · 0.9 Sedes, agencias y contactos) · 1) Tipos de gasto y cuentas · 2) Reglas de la política · 3) Meals and Incidentals · 4) Monedas · 5) Campos por tipo (guía) · 6) Campos de la solicitud (guía) · 7) Alertas y soporte

## 0. Pantalla real (verificado nov-2026 en cuentas de entidad CIAT; lo de Bioversity viene de las guías)

### 0.1 General

- Dirección: `https://eu2.concursolutions.com` (ingreso con SSO de CGIAR y Authenticator).
- El idioma depende del perfil de cada usuario: con inglés británico el reporte se llama **Expense Claim**; con inglés de EE. UU., **Expense Report**. Leer la pantalla antes de buscar un botón por nombre. Fechas en formato MM/DD/YYYY.
- Rutas: solicitudes `/nui/travelrequest`; gastos `/nui/expense` (reportes, "Available Expenses", "Available Receipts"); un reporte `/nui/expense/reports/<id>`; un gasto `/nui/expense/reports/<id>/expenses/<id>`.
- Portada: "Requests" (solicitudes), "Expense Reports", "Available Expenses" y "Approvals" (lo que la persona debe aprobar como supervisora: no tocar).
- Aviso de la empresa en la portada: gastos con tarjeta corporativa tienen máximo **40 días** desde el regreso. La política dice 15 días para legalizar: apuntar a 15.
- Filtros "View": en Manage Expenses → Active, Sent for Payment (90 Days), Last 90 Days, This Year, Last Year, Date Range; en Manage Requests → Active, Not Submitted, Pending Approval, Approved, Cancelled, Closed, All Requests.

### 0.2 Solicitud (Create New Request)

| Campo | Notas |
|---|---|
| Commitment ID | Bloqueado; se llena solo al enviar |
| Travel Type * | International / National |
| Trip Title * | Ayuda: "Where, When and What, e.g. Rome 15-16 august 2024 finance retreat" |
| Start Date *, End Date * | Duration (Days) se calcula solo |
| Trip Purpose * | Alliance Workshop · Donors visit · Donors visit & Other · External Meeting · Field trip · Field Trip & Other · Harvest work · Hosted Meeting · HR Travel (Appointment / Compassionate / Relocation / Separation) · Internal Meeting · Non-alliance workshop · Office Visit · Office Visit & Other · OneCG Meeting · OneCG Meeting & Other · Other · Planning · Planting work · Process review and control · Technical Visits · Visit Partners · Visit partners - Others |
| Non Staff, Personal Travel on this trip | Casillas |
| Name (Non-staff), ID Number / Nationality (Non-staff), Family Members | Solo si aplica |
| Insert CIAT * (1) → Insert ALL * (2) → Insert the AEC * (3) | Lista encadenada: elegir el código en (1) llena (2) y (3). Opciones como "(CIAT-ALL-XXXXXXXXTV2) Travel". Ayuda: filtro en "Either". Trae "Most Recently Used" |
| UNIT | Bloqueado, viene del perfil |
| Accounting Office * | Código de tres letras de la sede que emite el anticipo o procesa el reporte (Nairobi: **NBO**). Reemplaza a "Cash Advance Entity" y "Travel Office" de la guía |
| Comment | 500 caracteres |

"Create Request" guarda un borrador; no envía. En las líneas esperadas, M&I y hotel se calculan con la tarifa DSA del destino (en la solicitud aparece como "Destination City – Room (R) & Per-diem (P) rates in US$", p. ej. "(Elsewhere-ES) Elsewhere").

Error real al enviar con un AEC que no es de viaje: "Unable to proceed: The AEC … Check BUS status, please contact the Finance Team". Se resolvió usando el AEC de viaje (terminado en TV2).

### 0.3 Solicitud aprobada → crear el reporte

La solicitud aprobada muestra arriba a la derecha **"Create Expense Report"** y los menús Request Details (Request Header / Request Timeline / Audit Trail), Print/Share y Attachments. Ese botón crea el reporte enlazado a la TR. Alternativa: Expense → Create Expense Report/Claim → "Create from an Approved Request".

### 0.4 Encabezado del reporte (Report Details → Report Header)

Campos: Commitment ID (bloqueado), Report Name *, Report Date, Trip Purpose *, Report Type, CIA * / ALL * / AEC *, Non Staff Name, ID Number / Nationality, Accounting Office *, Report Number, **Personal Travel on this trip** (None Selected / No / Yes), **Reimbursement Currency *** y Comment (500).

- **Reimbursement Currency** es obligatoria y debe ser válida para el Accounting Office; si falta salen dos errores que bloquean el envío. Para NBO aparecen arriba "(USD) US Dollar" y "(KES) Kenyan Shilling". Preguntar cuál: depende de la cuenta donde reembolsan.
- Con días personales: "Personal Travel on this trip" = Yes y una línea en Comment para el procesador.

### 0.5 Detalle de un gasto

Pestañas Details / Itemizations / Allocations. Campos: Expense Type *, Transaction Date *, Business Purpose, City of Purchase *, Payment Type *, Amount *, Currency *, Exchange Rate *, Amount in USD *, Supplier, Request * (solo si el tipo estaba en la TR), Comment (500), y el visor de recibo (Upload New Receipt / Choose From Available Receipts; con recibo: Remove / Add / Open). Hotel añade Date Range * y Nights.

- **Supplier es obligatorio para usuarios de entidad CIAT** aunque no tenga asterisco (Bioversity no tiene este campo, según la guía): sin él sale "PROVEE - You need to enter the name of the supplier". Usar "(00000000) N/A" cuando el comercio no está registrado. Algunas agencias sí están: "(KENP000599474Q) SATGURU TRAVEL AND TOUR SERVICES LIMITED".
- **Payment Type**: "Out-of-Pocket" (pagado por el viajero: efectivo o tarjeta personal), "Company Paid" (pagado por la Alliance, p. ej. el tiquete de la agencia) y, con tarjeta corporativa, el nombre del banco emisor con ícono de tarjeta. Las compras con tarjeta corporativa llegan solas a "Available Expenses" con proveedor, ciudad y monto; solo falta tipo y recibo. "Card Transactions" (en Manage Expenses) muestra si la persona tiene tarjeta corporativa cargada.
- **City of Purchase** pone la moneda y la tasa del día de la transacción (Paris/Madrid/Granada → EUR; Nairobi → KES). Para el tiquete pagado en USD, cambiar la moneda a USD a mano.
- **Request**: se enlaza solo a la línea aprobada del mismo tipo ("10/25/2026, $585.78 - …"). Tipos sin línea en la TR (Local Transport, Fare National) no muestran el campo y se guardan igual.

### 0.6 Tipos de gasto (lista completa vista en un reporte CIAT, nov-2026)

- **01. Travel**: Hotel / Room Allowance · Hotel / Room Allowance - Manual · Meals and incidentals · Meals and Incidentals - Manual · Travel Expenses - General & miscellaneous · Unsupported Colombia - Meals and Incidentals - Expenses
- **02. Transportation**: Fare Int. (air tkt and other long-distance transport) · Fare National (air tkt and long-distance transport) · Local Transport (short distance, train, taxi, bus, etc.)
- **03. Communication**: Representation - Hospitality Expenses
- **04. Fees**: Visas
- **05. Meetings and Events**: Workshop - (non staff) Meals and Incidentals · Workshops - (non-staff) Accommodation · Workshops - (non-staff) General & Miscellaneous Expenses · Workshops - (non-staff) Ticket Costs
- **06. HR Related Travel**: Travel - Appointment · Travel - Compassionate. · Travel - Relocation · Travel- Repatriation
- **07. Training**: Professional Development (Staff development + travel)
- **08. Accounts Receivable**: A/R Employees for Travel and Office Expenses
- **09. Field Work Activities**: Expenses non-staff - Field operations - wages · General services in official travel · Guides and similar expenses · Representation expenses · Supplies in official travel

Uso práctico (reporte aceptado como borrador sin errores, nov-2026):

| Gasto | Tipo | Pago | Fecha | Soporte |
|---|---|---|---|---|
| Cada comida (urbano, costo real) | Meals and incidentals | Out-of-Pocket | la del recibo | recibo |
| Uber, taxi, traslado al aeropuerto o estación | Local Transport | Out-of-Pocket | la del recibo | recibo o comprobante de la app |
| Tiquete aéreo de la agencia | Fare Int. | Company Paid | emisión del tiquete | correo o factura de la agencia + pases de abordar (unidos en un solo adjunto) |
| Tren o bus entre ciudades pagado por el viajero | Fare National | Out-of-Pocket | compra del billete | billete con precio |

### 0.7 Alertas que se vieron

Errores (bloquean el envío):
- "The Reimbursement Currency you have selected is not valid for this Accounting Office" / "The report header is missing data in this required field(s): Reimbursement Currency".
- "PROVEE - You need to enter the name of the supplier".

Advertencias (no bloquean):
- "You must attach a receipt image to this expense" (solo en gastos que superan el umbral de recibo).
- "Please ensure your cash advance is issued by the processor…" (recordatorio fijo).
- "Please ensure you reconcile the expense type Fare National or Fare International…" (recordatorio fijo; sigue aunque el tiquete esté cargado).
- "The transaction date is older than your company allows. Please provide an explanation…" (tiquetes comprados semanas antes): explicar en el comentario.

### 0.8 CIAT vs. Bioversity (según las guías de 2023; confirmar en pantalla)

Cada empleado está en una entidad legal; se ve en los campos del encabezado.

| Tema | Entidad CIAT | Entidad Bioversity |
|---|---|---|
| Código presupuestal | Lista encadenada CIAT / ALL / AEC, p. ej. "(CIAT-ALL-XXXXXXXXTV2) Travel". AEC de viaje termina en TV | Código A… - B… - C…, p. ej. "A1301-B100695-C100509". Filtro del buscador en "either" |
| Campos extra en cada gasto | Supplier (obligatorio; "(00000000) N/A" si no está registrado) y Receipts Status; en Palmira, itemizaciones | Ninguno extra: Save Expense |
| Moneda por defecto | La de la sede (p. ej. COP en Palmira, KES en Nairobi) | USD |
| Non-staff en la TR | Nombre completo + pasaporte/ID y nacionalidad | Nombre + Supplier ID que da Cuentas por Pagar (Alliance-AccountsPayableRome@cgiar.org) |
| Porción personal (A/R Employees) | Cuenta 35010 | Cuenta 33002 |
| Flujo de aprobación del reporte | Siempre pasa por revisión (clearance) | Puede ir directo al procesador |
| Monedas aceptadas en Agresso | Lista CIAT (§4) | Lista Bioversity (§4) |
| M&I en Palmira | Existe "Unsupported Palmira Per-diem Expenses" | No aplica |

Gasto intra-Alliance (contrato de una entidad, paga la otra): no se puede poner el código de la otra entidad; escribir en Comments del encabezado y de cada gasto "Intra-Alliance, the real expense will be covered by <entidad> <código>".

### 0.9 Sedes, agencias y contactos

Accounting Office: código de tres letras de la sede que procesa el reporte (Nairobi = **NBO**). Si no se sabe, mirarlo en una TR anterior de la persona (Request Header).

Agencias de viajes institucionales según el mapeo de viajes de 2024–2025 (confirmar con la oficina de viajes de la sede; cambian con los contratos):

| Región / sede | Agencia |
|---|---|
| África (Nairobi y otras) | FCM Travel y Satguru Travel ("SATGURU TRAVEL AND TOUR SERVICES LIMITED" está registrada como proveedor en Concur) |
| Américas | Carlson Wagonlit (CWT) |
| Asia | FCM (Malasia), Mayflower (Malasia), Travel Experts (India), Joytours y Green Paradise (Vietnam, Laos, Filipinas) |
| Italia (Roma) | Uvet American Express |
| Montpellier | Havas Voyages |
| Lovaina | Omnia Travel (agencia de KU Leuven) |

Contactos:
- Soporte de Concur (accesos, perfiles, errores): Alliance-ITsupport@cgiar.org.
- Tarjeta corporativa: Alliance-CorporateCreditCard@cgiar.org.
- Oficina de viajes de Europa: alliance-traveleurope@cgiar.org.
- Guías, videos y preguntas frecuentes: SharePoint de Alliance-Finance ("What you need to know about SAP Concur", "Frequently SAP Concur Asked Questions", "Travel Buddy").
- Cada región tiene "Champions" de Concur (usuarios de referencia) que resuelven dudas locales.

## 1. Tipos de gasto y cuentas

Viaje de staff (cuentas 97…):

| Tipo (nombre de la guía) | Cuenta | Para qué |
|---|---|---|
| Fare – National | 97002 | Tiquete o pasaje nacional (avión, tren, barco, bus intermunicipal) |
| Fare – International | 97006 | Tiquete internacional |
| Local Transportation (Taxis, trains & Buses) | 97206 | Taxi, metro, bus urbano, tren de cercanías, traslados al aeropuerto |
| Hotel – Room Allowance | 97202 | Alojamiento |
| Meals and Incidentals | 97204 | Comidas e imprevistos (antes "per diem") |
| Unsupported Palmira Per-diem Expenses | 97203 | Solo CIAT |
| Travel Expenses – General & miscellaneous | 97201 | Lo que no cabe en los demás: SIM/eSIM, seguro de viaje, tasas aeroportuarias, exceso de equipaje aprobado |
| Visas | 97220 | Visa, fotos, permisos de entrada |
| Representation – Hospitality Expenses | 97224 | Invitaciones y comidas grupales |
| Professional Development | 91244 | Capacitación (curso + viaje) |
| A/R Employees for Travel and Office Expenses | 33002 (Bioversity) / 35010 (CIAT) | Porción personal del viaje, o costo que paga un tercero |
| Cash Advance Return | — | Saldo no usado del anticipo |

Talleres de la Alliance con participantes no staff (cuentas 94…, propósito "Alliance Workshop"):

| Tipo | Cuenta |
|---|---|
| Workshops – (non-staff) General & Miscellaneous Expenses | 94202 |
| Workshops – (non-staff) Ticket Costs | 94204 |
| Workshops – (non-staff) Accommodation | 94206 |
| Workshops – (non-staff) Meals and incidentals | 94207 |

Los gastos del taller (salón, catering, refrigerios, M&I pagado en sitio a participantes) van en una TR aparte del staff responsable, con cuentas 94…. Cada participante no staff lleva su propia TR y su propio reporte. No staff no puede pedir anticipo. El staff que asiste a un taller usa las cuentas 97… normales.

Viajes de RR. HH. (nombramiento, reubicación, repatriación, compasivo) tienen cuentas propias y código "NON AEC": consultar la guía de TR.

## 2. Reglas de la política que más causan devoluciones

- **Plazo**: reporte dentro de 15 días calendario tras el regreso. Fuera de plazo puede no procesarse. No se da un anticipo nuevo con uno anterior sin legalizar.
- **TR antes de todo**: aprobada antes de salir y de gastar, incluso si el viaje no cuesta nada a la Alliance (TR de costo cero con Fare en 0). Sirve también como autorización de seguridad y para el seguro.
- **Recibos**: obligatorios salvo transacciones de menos de USD 25 (tarjeta corporativa) o USD 15 (otros medios).
- **Tiquetes aéreos**: solo por la agencia institucional; se reportan con e-ticket y pases de abordar, pago "Company Paid". Comprados por fuera no se reembolsan sin excepción aprobada.
- **Hotel**: tope de 120 % de la tarifa ONU, con factura del hotel. En Palmira, alojarse en el campus.
- **Hospitalidad**: recibo + nombres de asistentes, entidad y motivo. El empleado descuenta su porción de su M&I.
- **Porción personal (días personales)**: la Alliance paga solo la parte oficial. Marcar "Personal Travel on this trip", no cargar gastos de esos días y, si el tiquete costó más por los días personales, cargar la diferencia como A/R Employees. Para calcularla hace falta una cotización con regreso en la fecha oficial; si no la hay, avisarlo.
- **Otros reembolsables con recibo**: traslados a terminales, transporte local, visas, tasas aeroportuarias, exceso de equipaje para documentos (con aprobación previa), seguro de viaje, SIM/eSIM.
- **No reembolsable**: millas o recompensas, películas en la habitación, multas, gastos no laborales. Vacunas y profilaxis van al seguro médico (Cigna).
- **Recibo perdido**: formato "Missing Receipt Declaration" (Manage Receipts → Missing Receipt Declaration).
- **Tarjeta corporativa**: quien la tiene no debería pedir anticipo para hotel y comidas ni reembolso de bolsillo.
- **Carro particular**: tarifa ONU por milla (en USD) más peajes y parqueadero.
- **Viajes terrestres múltiples**: se puede una sola TR mensual y una legalización mensual.
- **Tasa de cambio**: la de la fecha de la transacción, que Concur pone sola.
- Solo Europa: tiquetes aéreos en EUR.

## 3. Meals and Incidentals (M&I)

- Tope diario: 80 % de la tarifa ONU del destino (calculador DSA en Power BI). En la práctica: monto de M&I aprobado en la TR ÷ días de la TR. No inventarlo.
- Reparto del día: desayuno 15 %, almuerzo 30 %, cena 40 %, imprevistos 15 %. Las comidas se compensan entre sí, pero el total del día no pasa del tope.
- Comidas provistas (desayuno del hotel, almuerzo del evento, cena invitada): se descuenta su porcentaje.
- **Zona urbana**: costo real con recibos (una línea por recibo); el tope sigue siendo el M&I del día.
- **Zona rural**: se declara por día con los porcentajes, sin recibos.
- **Imprevistos**: hasta 15 % del M&I, sin recibo. Son costo real, no un derecho automático.
- Requiere al menos una noche fuera.
- Viajes de más de 15 días: acordar con el supervisor una alternativa más económica.
- La guía antigua pedía una sola línea de M&I con la hoja "Alliance Meals & Incidentals Claim SAP Concur.xlsx"; en reportes urbanos actuales se carga cada recibo y se adjunta la hoja de gastos por día (ver SKILL.md, paso 8).

Ejemplo de tope: USD 60, hotel con desayuno, almuerzo dado por el evento → reclamable ese día = 60 × (40 % cena + 15 % imprevistos) = USD 33.

## 4. Monedas activadas en Agresso

Si la moneda no está en la lista de la entidad, se registra en su equivalente en USD.

- **Bioversity**: AUD, BIF, CAD, CHF, COP, CRC, CZK, DKK, ETB, EUR, GBP, INR, JPY, KES, MAD, MWK, MYR, NOK, NPR, NZD, PEN, PHP, SEK, THB, UGX, USD, UZS, VND, XAF, XOF, ZAR.
- **CIAT**: AUD, CAD, CDF, CHF, COP, EUR, GBP, HNL, JPY, KES, LAK, MWK, NIO, NOK, PEN, PHP, RWF, TZS, UGX, USD, VND, XOF, ZAR, ZMW, ZWL.

Lista de 2023: si Concur rechaza una moneda, usar USD y avisar.

## 5. Campos por tipo (según la guía de 2023)

- **Transaction Date**: fecha de la factura o recibo. Para tiquetes, la de emisión.
- **City of Purchase**: donde se hizo el gasto; define la moneda.
- **Amount** y **Currency**: valor real del soporte.
- **Hotel**: check-in y check-out según factura (las noches se calculan solas). Valor total de la factura.
- **Fare National / International**: valor del e-ticket o billete. Company Paid si lo compró la agencia; Out-of-Pocket si lo pagó el viajero (p. ej. un tren comprado en línea).
- **A/R Employees**: valor a cargo del viajero.
- **Cash Advance Return**: saldo "Remaining" del anticipo, en la moneda por defecto. Ej.: anticipo 500, gastos de bolsillo 300 → devolución 200.
- Estado del reporte: Report Details → Report Timeline. Se puede hacer **Recall** mientras el procesador no lo haya aprobado.

## 6. Campos de la solicitud (según la guía)

- **Trip Title**: máximo 32 caracteres, "dónde – cuándo – qué". Migra a Agresso.
- **Budget code / AEC**: filtro en "either". CIAT: CIAT/Project = CIAT, ALL/BUS = ALL, AEC de viaje (terminado en TV). Para otro código o entidad, **Allocate** por gasto.
- Gasto intra-Alliance (contrato de una entidad, paga la otra): escribirlo en Comments del encabezado y de cada gasto con el código real.
- **Fare**: cotización de la agencia; país de origen y destino final; itinerario en Comments. Tiquete pagado por un tercero: Fare en 0. Si hay tramo en tren o bus entre ciudades, agregarlo también.
- **Meals & Incidentals / Hotel**: país y ciudad de destino; el sistema calcula con la tarifa DSA. Los días se pueden reducir, no aumentar.
- **Cash Advance**: Request Details → Add Cash Advance; en USD o en la moneda por defecto.
- Para cancelar un viaje usar **Cancel Request**, nunca Close Request; si ya hubo gastos, no se cancela: se legaliza.

## 7. Alertas y soporte

- Alertas **rojas** (Error): bloquean. Amarillas (Warning): no bloquean.
- HRCOUNTR: la TR necesita autorización de seguridad. TGCYPPRV: falta visto bueno de la oficina o agencia de viajes para emitir el tiquete.
- Soporte de Concur: Alliance-ITsupport@cgiar.org. Tarjeta corporativa: Alliance-CorporateCreditCard@cgiar.org.
