# Driving Concur in the browser

What was learned filling in a real 23-line report (Nov 2026). Read before touching Concur.

Contents: 1) Which browser · 2) Click and typing rules · 3) Expense forms · 4) Copying similar lines · 5) Attaching receipts · 6) Report attachments · 7) What the browser can't do

## 1. Which browser

- First check where the session is: `mcp__Claude_Browser__tabs_context` (Claude's Browser pane) or `mcp__claude-in-chrome__tabs_context_mcp` (Chrome). Use whichever has a tab on `eu2.concursolutions.com`.
- If neither is connected: for Chrome, the person installs the "Claude in Chrome" extension and signs in with their Claude account; otherwise continue without a browser (see SKILL.md, "If no browser is available").
- Before working, open the profile menu (initials, top right) and read **whose account it is**. It may be a colleague's; say so in the chat. Close the menu with Escape.
- Concur also lets someone be a **delegate** for another person (the account owner sets it up in their profile; there's a video in the Finance FAQ). In that case the person logs in with their own account and acts on behalf of the other: confirm on whose behalf they are acting before entering anything. (The exact name of that menu option hasn't been verified; record it here the first time it's seen.)
- If Concur asks for a login, the person does it. Never type credentials or approve Authenticator prompts.

## 2. Click and typing rules

- The window size changes between turns: take a screenshot before using coordinates. Prefer `find`/`read_page` and refs.
- Coordinates from JavaScript: page rects are in CSS pixels; the screenshot frame is smaller. Factor = `innerWidth / screenshot_width` (e.g. 1355/800). Divide the rect by that factor.
- Concur dropdowns aren't `<select>` elements: click the arrow → screenshot → click the option. Don't press Enter when focus is uncertain: it once opened a new request form by mistake.
- Fields that already have a value (Concur pre-fills the last one used): **triple-click** to select and type over it. A single click followed by typing appends the text to the old value.
- In comments (textarea), `cmd+a` doesn't select; use triple-click.
- After every important change, `zoom` on the form to check before saving.
- The "Save Expense" button saves the line in the draft; it doesn't submit the report. **The skill never touches "Submit Report".**
- If the person stops a step (stop button or Esc), stop, check where the page was left and ask before continuing.

## 3. Expense forms

- **City (City of Purchase):** click the field, click the search box that appears, type the city, wait 2–3 s, pick "City, COUNTRY". The city sets the currency and the day's rate on its own.
- **Supplier:** required for CIAT. Open it, type "N/A", pick "(00000000) N/A". For registered agencies, search by name (e.g. "Satguru" → "(KENP000599474Q) SATGURU TRAVEL AND TOUR SERVICES LIMITED").
- **Date and rate:** when the date changes, the rate reloads with a delay. Safe order: date → Tab → wait 3 s → amount → Tab. If you save before that, you get "you must provide valid information for: Exchange Rate".
- **USD amount that doesn't update:** if the amount is the same as before it isn't recalculated; type a different value and then the right one (or 16.5 instead of 16.50).
- **Payment Type:** defaults to "Out-of-Pocket"; for the agency ticket change it to "Company Paid".
- **Request:** only shows up for types that were in the TR (Meals and incidentals, Fare Int.) and links itself to the approved line. Local Transport and Fare National with no line in the TR don't show it.
- When saving with something missing you get "This expense has been saved, but it is missing required information…": choose "Yes" to see what's missing.

## 4. Copying similar lines (Duplicate)

For many receipts of the same city and type (meals):

1. Create and save one complete line (type, city, supplier N/A).
2. Tick its checkbox in the list and press **Duplicate** as many times as there are receipts left. The selection stays; each copy keeps the same city and supplier, with the date +1 day.
3. Open each copy and change the date, purpose, amount and comment.
4. The list is sorted by date, newest first: when the date changes the line moves up or down. After saving, look at the list to find the next unedited copy (same amount as the original).

At the end, check that the number of lines and the total match the table.

## 5. Attaching receipts

The person uploads the files to "Available Receipts" (see section 7). Then, for each expense:

1. Open the expense. Without a receipt, the right panel shows "Choose From Available Receipts".
2. Click it. Cards appear with the file name and **three icons packed closely together: Attach, Delete, View**. Find **Attach** by its aria-label, never blindly by position.
3. After attaching, "Receipt attached" appears with the file name under the viewer.
4. The **">"** arrow next to "n of N" moves to the next expense without going back to the list.
5. Several documents for one expense (ticket + boarding passes): attach the first, then **Add** under the viewer and pick the next one. Concur merges them into a single document (it warns they can't be separated). Check that the page counter goes up.

JavaScript helpers (read and locate only; clicks are made with the mouse tool). Paste once per page load, changing the amount → file prefix map:

```js
window.__map = {"€ 48.00":"06 ", "KES 1,808.00":"01 ", "$898.00":"27 "}; // header amount → file name prefix
const F = innerWidth / 800; // 800 = width of the current screenshot
window.__pt = el => { const r = el.getBoundingClientRect(); return [Math.round((r.x + r.width/2)/F), Math.round((r.y + r.height/2)/F)]; };
window.__info = () => {
  const norm = s => s.replace(/[  ]/g, ' ').trim();
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

Cycle per expense: `__info()` → click `choose` → `__card(want)` → click `attach` → check the file name → ">" arrow. Notes:
- Header amounts contain a non-breaking space (`€ 8.05`); that's why they're normalized.
- If `__info()` returns everything empty, the page hasn't finished loading: wait 3 s and try again.
- Reloading the page (navigate) wipes the helpers; paste them again.
- At the end, in the report list, count the `button[aria-label="Attach Receipt"]` buttons: if it's 0, every line has a receipt.

## 6. Whole-report attachments

Manage Receipts → **Manage Attachments** shows all pages of the report. Its **Add** button opens the computer's file picker (it doesn't let you pick from Available Receipts), so the person uploads the expense sheet PDF. Don't touch "Delete" in that window. To check, reopen the window and see that the page counter went up.

## 7. What the browser can't do (the person's part)

- **Upload files.** Instructions for the person: Expense → Manage Expenses → "Available Receipts" section → **"Upload New Receipt"** → go to the "To upload to Concur" folder → select all (Cmd + A on Mac, Ctrl + A on Windows) → Open. If it doesn't allow multiple files, drag them from Finder or File Explorer onto that section. Opening the folder for them helps: `open "<path>"` (Mac) or `explorer "<path>"` (Windows).
- Alternative from a phone: the SAP Concur app (sign in with the CGIAR email → MS Azure → Authenticator) can photograph receipts and upload them; they show up in "Available Receipts".
- **Log in** and approve Authenticator prompts.
- **Submit the report** (Submit Report) and **approve** other people's reports.
