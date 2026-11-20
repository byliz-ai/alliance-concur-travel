---
name: legalizar-viaje
description: Prepares and fills in SAP Concur travel requests (Travel Request) and expense reports (Expense Report / Expense Claim) for any staff member of the Alliance of Bioversity International and CIAT (CIAT or Bioversity entity, any hub) from receipts, tickets and boarding passes, and builds the supporting expense sheet in Excel and PDF. Use it whenever someone mentions Concur, an expense report or claim, a travel request, a cash advance, per diem, M&I, DSA or trip receipts, or says things like "I need to do the expense report for my trip to…", "help me with Concur", "my report was sent back" or "create my travel request", even if they don't name the skill. ES — legalizar, legalización, reporte de gastos, solicitud de viaje, anticipo, viáticos, "tengo que legalizar el viaje a…", "me devolvieron el reporte". FR — note de frais, demande de voyage.
---

# Travel expense reports in SAP Concur (Alliance Bioversity–CIAT)

The goal is for staff to spend minutes, not hours, in Concur: you read the receipts, classify, calculate, type and attach; the person decides what only they know, does the few steps the browser can't do, and submits. Reports are almost always sent back for the same reasons (empty required field, wrong expense type, date that doesn't match the receipt, missing receipt, undeclared personal days), so the review beforehand is worth as much as the data entry.

**Language:** talk to the person in their language (Spanish, English, French…). What goes into Concur (purposes, comments) and the expense sheet is written in English, which is what the processors read.

There are two modes. Pick one based on the request:

- **Travel Request (TR)**: before the trip. Without an approved TR there is no spending and no travel.
- **Expense report (Expense Report / Expense Claim)**: after the trip. Deadline: **15 calendar days** from the return (with a corporate card the Concur home page mentions 40 days; aim for 15). If it's already late, say so at the start.

Skill files (read them when a step says so):

- `references/alliance-concur.md`: expense types, travel policy rules, CIAT/Bioversity differences, hubs, and what the real Concur screens look like.
- `references/concur-browser.md`: how to drive Concur in the browser without errors, copy lines, attach receipts, and what the browser can't do.
- `scripts/expense_sheet.py` and `assets/example_sheet.json`: generate the supporting expense sheet (Excel + PDF).
- `assets/profile-template.md`: template for each user's profile.

## Non-negotiable rules

- **Never submit (Submit Report) or approve** reports or requests. By submitting, the traveler certifies that the expenses are real; that signature is theirs. Everything stays as a draft.
- **Never type credentials** or approve Authenticator prompts; if Concur asks for a login, the person does it.
- **Never invent data.** An unreadable receipt or a missing amount (e.g. a train notice without a price) is marked as pending and asked about. An invented value in an expense report is a serious problem for the traveler.
- **Never delete** receipts, files or lines unless asked. In Concur the Delete icon sits right next to Attach (see browser §5).
- Don't move or rename the original files: work on copies.
- Work only in the account the person opened and is entitled to manage (their own, or someone else's who has made them a delegate in Concur). If the open account belongs to someone else, say so and confirm before touching anything.

## First use: the profile

The profile keeps what doesn't change from trip to trip (entity, hub, Accounting Office, reimbursement currency, corporate card, usual codes, travel agency, how the person likes to work). It lives **outside the skill**, in `~/.claude/legalizar-viaje/profile.md` (on Windows, `%USERPROFILE%\.claude\legalizar-viaje\profile.md`), so it isn't shared when the skill is passed on and isn't lost when the skill is updated.

- If it exists, read it at the start.
- If it doesn't, create it from `assets/profile-template.md`, filling in what you see in Concur (UNIT field, entity, Accounting Office, recent codes, interface language) and asking only for what's missing. Show the person what you saved.
- If you're helping with a colleague's account, don't save their profile there unless the person asks (it can go in `~/.claude/legalizar-viaje/profiles/<name>.md`).

## Getting started: the opening message

Before touching Concur, send **one single message** that gives the person all the information, so they aren't surprised when you ask for something halfway through. It must include:

1. **What you'll do**, in 4–6 short steps.
2. **What you need**, as a checklist (adapt it to the case):
   - Concur open and logged in (in Claude's Browser pane or in Chrome with the Claude extension), in the traveler's account.
   - The trip receipts (photos or PDFs) in the Downloads folder or pasted into the chat, including Uber/taxis.
   - The agency email or invoice with the **ticket price**, and the outbound and return **boarding passes**.
   - Train or bus tickets with their **price** (a travel notice without a price doesn't work).
   - Whether the event or organizer provided any meals, and whether there was a cash advance.
   - If the processor at their hub asks for its own expense sheet format, the sample file.
3. **When they'll need to step in** (use this table):

   | When | What the person does | Why |
   |---|---|---|
   | At the start | Log in to Concur if needed | The credentials are theirs |
   | After the receipts are read | Answer decision questions (personal days, who paid what, card, reimbursement currency) | Only they know |
   | After the lines are entered | Upload the receipts to "Available Receipts" (a few clicks) | The browser can't upload files |
   | After the receipts are attached | Upload the expense sheet PDF to "Report Attachments" | Same reason |
   | At the end | Review and submit the report | The signature is the traveler's |

4. **How long it takes**: with about 20 receipts, entering and attaching in Concur takes roughly an hour of browser work. Tell them that if they press the stop button or type while you're working, the current step is cut short; that's fine, they just need to tell you "continue".
5. **First questions**, only those essential to get going (whose trip it is, where the files are). Decision questions come after reading the receipts.

If the person prefers to go "one by one", ask the decisions one at a time, with buttons, and move on as soon as they answer each one.

### If no browser is available

If neither the Browser pane nor Chrome is connected, you can still do steps 2–5 and 8 (read, classify, ask, prepare the folder and the expense sheet) and deliver a table in data-entry order, with every Concur field, so the person can enter it by hand. Say so at the start.

## Expense report mode

### 1. Find Concur and the account

Follow `references/concur-browser.md` §1: find the Concur tab and **read whose account it is** in the profile menu. Check the home page: approved requests without a report, draft reports, pending approvals (don't touch those).

Open the trip's TR (Requests → the request) and note: ID, dates, purpose, budget code or AEC, Accounting Office and **each approved line** (type and amount). Lines that aren't in the TR can still be entered, but they need an explanation. If an Outlook connector is available, Concur notifications (sender `concursolutions.com`) also help find the TR.

### 2. Gather the receipts

- Look for recent files in Downloads (macOS/Linux: `ls -lt ~/Downloads | head`; Windows: `Get-ChildItem $HOME\Downloads | Sort-Object LastWriteTime -Descending | Select-Object -First 15`).
- WhatsApp file names on macOS have a special space before "AM/PM": copy with a wildcard (`cp ~/Downloads/WhatsApp\ Image\ 2026-11-20\ at\ 11.10.21*`) instead of typing the name.
- PDFs and images can be read directly with Read. With many photos, build a contact sheet (thumbnails with PIL and their file names) to read them all at once and know which file is which receipt. To use PIL, don't run Python with `-I` (it won't find the user's packages).
- Watch for new files while you work: people often keep adding files (boarding passes, tickets).

### 3. Read and classify

From each receipt get: date and time, vendor, city, amount, currency, **last digits of the card** and what was bought. Then:

- **Expense type** per `references/alliance-concur.md` §0.6 and §1: meals → "Meals and incidentals" (one line per receipt in urban areas); Uber/taxi → "Local Transport"; air ticket → "Fare Int." or "Fare National"; intercity train or bus → "Fare National"; hotel → "Hotel / Room Allowance"; SIM, insurance, fees → "Travel Expenses - General & miscellaneous"; visa → "Visas"; meal with guests → "Representation - Hospitality Expenses".
- **Meal of the day** by time: before 11:00 breakfast, 11:00–17:00 lunch, after 17:00 dinner; several small evening receipts (tapas, bar) add up to dinner; a single coffee in transit can go as incidentals.
- **Official vs. personal days:** compare the TR dates with the **boarding passes** and with where the receipts are from. If the return flight is days after the TR ends, or there are receipts in a city that isn't the event's, there are personal days: ask, don't assume.
- **Daily meal cap**: M&I amount approved in the TR ÷ days. Flag the days that exceed it.
- **Rural area**: if the trip was rural, M&I is claimed per day with percentages, without receipts (see reference §3).

### 4. 🙋 Decision questions

Ask them together (or one at a time, if the person prefers) — only those that apply and aren't in the profile:

- Are the cards used personal or corporate? (With a corporate card, the charges show up on their own in "Available Expenses"; check Card Transactions.)
- Who bought the air ticket (the Alliance's agency or the traveler) and where is the price?
- Who paid for the train or bus, and how much was it?
- Which meals did the event or organizer provide? Did the hotel include breakfast?
- Until which day was the trip official? Does the return day count as official? Which expenses that day were personal (e.g. a detour)?
- Was any meal shared with other people? (It would go as Hospitality.)
- Was there a cash advance? How much?
- Reimbursement Currency: Concur only accepts the ones valid for the person's Accounting Office; it depends on the account they are reimbursed to.

### 5. Prepare the trip folder

In the Downloads folder create `Expense report <report number> - <trip>/` and copy the receipts with names that start with sequence number, date, vendor and amount (`06 2026-10-26 Hotel X EUR48.00.JPG`). Inside, a subfolder **`To upload to Concur`** with only what goes into the report (no personal expenses, no notices without a price). That way every receipt can be recognized in Concur without opening it.

### 6. Create the report and its header

From the approved TR: **"Create Expense Report"** button (top right). In the header (Report Details → Report Header):

- **Reimbursement Currency**: the one the person gave you. Without it Concur won't let them submit.
- **Personal Travel on this trip**: "Yes" if there were personal days.
- **Comment**: one line for the processor, e.g. "Official travel 25-30 Oct 2026 (30 Oct = return day). Personal days 31 Oct - 6 Nov at traveler's own cost; not claimed."

### 7. Enter the lines

Follow `references/concur-browser.md` §3–4 (safe field order, supplier, Duplicate for meals) and the entity differences in `references/alliance-concur.md` §0.8. Criteria:

- **With a corporate card**: the charges are already in "Available Expenses". Add them to the report from there (Add Expense → Select from Available Expenses), set the type and attach the receipt; don't create them by hand (they'd be duplicated). Corporate card holders shouldn't claim out-of-pocket expenses except in special cases.
- **Out-of-pocket expenses** (cash or personal card): Out-of-Pocket, comment with the actual vendor and the last digits of the card. CIAT-entity users: supplier "(00000000) N/A" if the merchant isn't registered.
- **Agency ticket**: "Fare Int." (or "Fare National" if domestic), **Company Paid**, supplier = the agency (search by name), date = ticket issue date, amount from the agency email or invoice, comment with the e-ticket number, flights and whether the return includes personal days.
- **Train or bus paid by the traveler**: "Fare National", Out-of-Pocket, date = purchase date, amount from the ticket.
- Purchase dates weeks before the trip trigger the warning "transaction date is older than your company allows": add to the comment "Transaction date is the purchase date (dd Mmm), bought in advance of travel on dd Mmm."
- **Cash advance**: out-of-pocket expenses are offset against the advance; if there's money left over, add a "Cash Advance Return" line for the balance (reference §5).
- **Personal days**: their expenses aren't entered. If the ticket cost more because of those days, the difference goes as "A/R Employees for Travel and Office Expenses" (you need a quote with the return on the official date to calculate it; if there isn't one, say so).

When you finish, compare the number of lines and the total with your table.

### 8. Supporting expense sheet (Excel + PDF)

Some processors ask for a sheet with the per diem by day and the other expenses. If the person has a template from their hub, read it and follow its format. If not, use the script:

1. Build a JSON like `assets/example_sheet.json`: per day, the amounts of each receipt in local currency and **the rate Concur applied that day** (it's on each line); under "other", Uber, taxis, train; under "notes", personal days and the Company Paid ticket (it goes as a note, not in the total).
2. Run `python3 <skill path>/scripts/expense_sheet.py data.json "<folder>/Travel expenses <trip>.xlsx" "<folder>/To upload to Concur/<n> Travel expenses <trip>.pdf"`. It needs `openpyxl`; for the PDF, `reportlab` (if it's missing, the script says so and the person can export the Excel file to PDF from Excel).
3. The total it prints must be **equal** to what Concur reimburses the traveler (report total minus Company Paid). If it's off by cents, check the rates.
4. Concur only accepts images and PDFs as receipts: the PDF is what gets uploaded.

### 9. 🙋 The person uploads the receipts

Give them the instructions in `references/concur-browser.md` §7, open the folder for them (macOS: `open "<folder>/To upload to Concur"`; Windows: `explorer "<folder>\To upload to Concur"`) and leave Concur on Expense → Manage Expenses, scrolled down to "Available Receipts". When they say they're done, check that all of them show up by name.

### 10. Attach the receipts

Follow `references/concur-browser.md` §5, expense by expense, checking the name of the attached file. For the ticket, attach the agency email or invoice and add the boarding passes.

### 11. 🙋 The person uploads the sheet PDF to the report

Manage Receipts → Manage Attachments → **Add** opens the computer's file picker: the person does it (`references/concur-browser.md` §6). Then check that the page count went up.

### 12. Final review and summary

- Open "View Alerts": there must be **0 errors**. Explain every warning left (the cash advance one and "reconcile Fare" are fixed reminders that don't go away).
- Confirm that no line is left without a receipt.
- Deliver the summary in a table that separates what the company pays from what is reimbursed. This distinction is confusing: explain it in plain words ("the Alliance paid the agency for the ticket; you don't get it back, it's only recorded").

  | | Reimbursement currency |
  |---|---|
  | Paid by the Alliance (Company Paid / corporate card) | … |
  | Reimbursed to the traveler (Out-of-Pocket, minus advance) | … |
  | **Report total** | … |

- List what the processor might ask about: days over the cap, large meals that might have been shared, extra ticket cost due to personal days, missed deadline.
- If you learned something for the profile (currency, agency, codes), update the profile.

### 13. 🙋 The person submits

Tell them exactly where the button is ("Submit Report", top right) and that by submitting the traveler certifies the expenses. You don't submit it.

## Travel request mode

1. Minimum data: destination, dates, purpose, budget code or AEC, whether they need a cash advance, and the ticket quote from their hub's agency.
2. Build the header and the expected expenses per `references/alliance-concur.md` §0.2 and §6. Estimate hotel and M&I with DSA rates (ask for the value from the Power BI calculator or let Concur calculate it; don't make it up). If there will be personal days, tick "Personal Travel on this trip" right away.
3. Show the draft: title (max 32 characters: where – when – what), purpose, dates and expected expenses.
4. If asked, fill it in Concur and leave it unsubmitted (Create Request saves a draft). Remind them to attach the itinerary and the quote. If there are intercity train or bus legs, include them as expected expenses so they aren't missing from the TR at expense report time.

## When a report is sent back

Find the Concur notification (email from `AutoNotification@concursolutions.com`, if there's an Outlook connector, or the Report Timeline in Concur) with the processor's comment, identify which line failed and why, propose the specific fix and, if they want, fix it in Concur without resubmitting.

## Keeping the skill up to date

If a field, menu or message doesn't match the references, stop, tell the person what you saw and fix the relevant reference (or note it for whoever maintains the skill). The Finance guides are from 2023 and the screens change; each hub and entity has its own variations.

If the skill folder is a git repo, after a fix commit with a message that says what changed (no personal data) and ask before pushing. To package a `.skill` from the repo, leave out `.git`, `README.md` and `.gitignore` (e.g. `git archive --prefix=legalizar-viaje/ HEAD -- SKILL.md references scripts assets`).

## Privacy

- Receipts contain personal and financial data. Work with local files; don't upload them to external services or paste them into web searches.
- Profiles live outside the skill; don't copy them into it. If you update the references, record only general things (forms, messages, office codes, agencies), never an individual's data.
