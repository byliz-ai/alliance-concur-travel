# Manejo del navegador en Concur

Lo aprendido llenando un reporte real de 23 líneas (nov-2026). Leer antes de tocar Concur.

Contenido: 1) Qué navegador · 2) Reglas de clic y escritura · 3) Formularios de gasto · 4) Copiar líneas parecidas · 5) Adjuntar recibos · 6) Adjuntos del reporte · 7) Lo que el navegador no puede hacer

## 1. Qué navegador

- Revisar primero dónde está la sesión: `mcp__Claude_Browser__tabs_context` (panel Browser de Claude) o `mcp__claude-in-chrome__tabs_context_mcp` (Chrome). Usar el que tenga una pestaña en `eu2.concursolutions.com`.
- Si ninguno está conectado: para Chrome, la persona instala la extensión "Claude in Chrome" e inicia sesión con su cuenta de Claude; si no, seguir sin navegador (ver SKILL.md, "Si no hay navegador disponible").
- Antes de trabajar, abrir el menú de perfil (iniciales arriba a la derecha) y leer **de quién es la cuenta**. Puede ser la de un colega; decirlo en el chat. Cerrar el menú con Escape.
- Concur también permite que alguien sea **delegado** de otra persona (lo configura el dueño de la cuenta en su perfil; hay un video en las preguntas frecuentes de Finance). En ese caso la persona entra con su propia cuenta y actúa en nombre del otro: confirmar en nombre de quién está antes de cargar nada. (El nombre exacto de esa opción en el menú no se ha verificado; anotarlo aquí la primera vez que se vea.)
- Si Concur pide iniciar sesión, lo hace la persona. Nunca escribir credenciales ni aprobar el Authenticator.

## 2. Reglas de clic y escritura

- El tamaño de la ventana cambia entre turnos: tomar captura antes de usar coordenadas. Preferir `find`/`read_page` y refs.
- Coordenadas desde JavaScript: los rect de la página están en píxeles CSS; el marco de la captura es más chico. Factor = `innerWidth / ancho_de_la_captura` (p. ej. 1355/800). Dividir el rect por ese factor.
- Los menús desplegables de Concur no son `<select>`: clic en la flecha → captura → clic en la opción. No usar Enter con el foco incierto: abrió un formulario de solicitud nueva por error.
- Campos que ya traen valor (Concur prellena con lo último usado): **triple clic** para seleccionar y escribir encima. Si solo se hace clic y se escribe, el texto se suma al anterior.
- En los comentarios (textarea), `cmd+a` no selecciona; usar triple clic.
- Después de cada cambio importante, `zoom` sobre el formulario para verificar antes de guardar.
- El botón "Save Expense" guarda la línea en el borrador; no envía el reporte. **"Submit Report" nunca lo toca la skill.**
- Si la persona detiene un paso (botón de detener o Esc), parar, revisar en qué quedó la página y preguntar antes de seguir.

## 3. Formularios de gasto

- **Ciudad (City of Purchase):** clic en el campo, clic en la caja de búsqueda que aparece, escribir la ciudad, esperar 2–3 s, elegir "Ciudad, PAÍS". La ciudad pone sola la moneda y la tasa del día.
- **Proveedor (Supplier):** obligatorio para CIAT. Abrir, escribir "N/A", elegir "(00000000) N/A". Para agencias registradas, buscar por nombre (p. ej. "Satguru" → "(KENP000599474Q) SATGURU TRAVEL AND TOUR SERVICES LIMITED").
- **Fecha y tasa:** al cambiar la fecha la tasa se recarga con retraso. Orden seguro: fecha → Tab → esperar 3 s → monto → Tab. Si se guarda antes, sale "you must provide valid information for: Exchange Rate".
- **Monto en USD que no se actualiza:** si el monto quedó igual al anterior no se recalcula; escribir otro valor y luego el correcto (o 16.5 en vez de 16.50).
- **Payment Type:** por defecto "Out-of-Pocket"; para el tiquete de la agencia cambiar a "Company Paid".
- **Request:** aparece solo en tipos que estaban en la TR (Meals and incidentals, Fare Int.) y se enlaza solo a la línea aprobada. Local Transport y Fare National sin línea en la TR no lo muestran.
- Al guardar con algo faltante sale "This expense has been saved, but it is missing required information…": elegir "Yes" para ver qué falta.

## 4. Copiar líneas parecidas (Duplicate)

Para muchos recibos de la misma ciudad y tipo (comidas):

1. Crear y guardar una línea completa (tipo, ciudad, proveedor N/A).
2. Marcar su casilla en la lista y pulsar **Duplicate** tantas veces como recibos queden. La selección se mantiene; cada copia queda con la misma ciudad y proveedor y fecha +1 día.
3. Abrir cada copia y cambiar fecha, propósito, monto y comentario.
4. La lista se ordena por fecha descendente: al cambiar la fecha la línea sube o baja. Después de guardar, mirar la lista para encontrar la siguiente copia sin editar (mismo monto que la original).

Contar al final que el número de líneas y el total coincidan con la tabla.

## 5. Adjuntar recibos

La persona sube los archivos a "Available Receipts" (ver sección 7). Después, en cada gasto:

1. Abrir el gasto. Sin recibo, el panel derecho muestra "Choose From Available Receipts".
2. Clic ahí. Aparecen tarjetas con el nombre del archivo y **tres íconos muy juntos: Attach, Delete, View**. Ubicar el de **Attach** por su aria-label, nunca por posición a ciegas.
3. Tras adjuntar aparece "Receipt attached" y el nombre del archivo bajo el visor.
4. La flecha **">"** junto a "n of N" pasa al siguiente gasto sin volver a la lista.
5. Varios soportes para un gasto (tiquete + pases de abordar): adjuntar el primero, luego **Add** bajo el visor y elegir el siguiente. Concur los une en un solo documento (avisa que no se pueden separar). Verificar que el contador de páginas suba.

Apoyo en JavaScript (solo lectura y ubicación; los clics se hacen con la herramienta de mouse). Pegar una vez por página cargada, cambiando el mapa monto → prefijo del archivo:

```js
window.__map = {"€ 48.00":"06 ", "KES 1,808.00":"01 ", "$898.00":"27 "}; // monto del encabezado → prefijo del archivo
const F = innerWidth / 800; // 800 = ancho de la captura actual
window.__pt = el => { const r = el.getBoundingClientRect(); return [Math.round((r.x + r.width/2)/F), Math.round((r.y + r.height/2)/F)]; };
window.__info = () => {
  const norm = s => s.replace(/[  ]/g, ' ').trim();
  const h = [...document.querySelectorAll('h2')].map(x => norm(x.innerText)).find(t => /(KES [\d,.]+|€ ?[\d,.]+|\$[\d,.]+)$/.test(t)) || '';
  let amt = (h.match(/(KES [\d,.]+|€ ?[\d,.]+|\$[\d,.]+)$/) || [])[1] || null;
  if (amt && amt.startsWith('€') && !amt.startsWith('€ ')) amt = '€ ' + amt.slice(1);
  const ch = [...document.querySelectorAll('button')].find(b => /Choose From Available Receipts/.test(b.innerText));
  return { pos: (norm(document.body.innerText).match(/(\d+) of \d+/) || [])[1], title: h.slice(0, 70), amt, want: window.__map[amt] || null, choose: ch ? window.__pt(ch) : null };
};
window.__card = prefix => {
  const leaf = [...document.querySelectorAll('*')].filter(e => e.childElementCount === 0 && (e.textContent || '').trim().startsWith(prefix));
  if (!leaf.length) return null;
  let c = leaf[0]; for (let i = 0; i < 8 && c; i++) { if (c.querySelectorAll('button').length >= 3) break; c = c.parentElement; }
  c.scrollIntoView({ block: 'center' });
  const b = [...c.querySelectorAll('button')].find(x => ['Attach', 'Add'].includes(x.getAttribute('aria-label')));
  return { name: leaf[0].textContent.trim(), attach: b ? window.__pt(b) : null };
};
```

Ciclo por gasto: `__info()` → clic en `choose` → `__card(want)` → clic en `attach` → verificar el nombre del archivo → flecha ">". Notas:
- Los montos del encabezado traen espacio duro (`€ 8.05`); por eso se normaliza.
- Si `__info()` devuelve todo vacío, la página no terminó de cargar: esperar 3 s y repetir.
- Al recargar la página (navigate) los apoyos se pierden; pegarlos de nuevo.
- Al final, en la lista del reporte, contar los botones `button[aria-label="Attach Receipt"]`: si da 0, todas las líneas tienen recibo.

## 6. Adjuntos del reporte completo

Manage Receipts → **Manage Attachments** muestra todas las páginas del reporte. Su botón **Add** abre el selector de archivos del computador (no deja elegir de Available Receipts), así que el PDF de la hoja de gastos lo sube la persona. No tocar "Delete" en esa ventana. Para verificar, reabrir la ventana y ver que el contador de páginas subió.

## 7. Lo que el navegador no puede hacer (le toca a la persona)

- **Subir archivos.** Instrucciones para la persona: Expense → Manage Expenses → sección "Available Receipts" → **"Upload New Receipt"** → ir a la carpeta "Para subir a Concur" → seleccionar todo (Cmd + A en Mac, Ctrl + A en Windows) → Abrir. Si no deja elegir varios, arrastrarlos desde Finder o el Explorador de archivos a esa sección. Ayuda abrirle la carpeta: `open "<ruta>"` (Mac) o `explorer "<ruta>"` (Windows).
- Alternativa desde el celular: la app de SAP Concur (ingreso con el correo CGIAR → MS Azure → Authenticator) permite fotografiar recibos y subirlos; aparecen en "Available Receipts".
- **Iniciar sesión** y aprobar el Authenticator.
- **Enviar el reporte** (Submit Report) y **aprobar** reportes de otros.
