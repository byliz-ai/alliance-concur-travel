# Reference: Concur rules and forms at the Alliance

Sources (SharePoint Alliance-Finance): "SAP Concur guideline – TR (Travel Request)" and "SAP Concur Guideline – ER (Expense Report)" (Oct 2023), "SAP CONCUR Guideline – Alliance Workshops" (Jul 2024), Travel Policy PO-08-BOF v05 (Aug 2024) and the note "Travel essentials in Europe" (Nov 2026), plus what was observed while filling in real reports (Nov 2026).

**Section 0 takes precedence over the rest**: it is what was seen on the actual screen. Sections 1–7 come from the guidelines and are useful for rules and context; where a field or expense type name differs, use the one in section 0. How to operate the browser is covered in `concur-browser.md`.

Contents: 0) Actual screen (0.1 General · 0.2 Request · 0.3 Creating the report · 0.4 Header · 0.5 Expense detail · 0.6 Expense types · 0.7 Alerts · 0.8 CIAT vs. Bioversity · 0.9 Hubs, agencies and contacts) · 1) Expense types and accounts · 2) Policy rules · 3) Meals and Incidentals · 4) Currencies · 5) Fields by type (guideline) · 6) Request fields (guideline) · 7) Alerts and support

## 0. Actual screen (verified Nov 2026 on CIAT-entity accounts; the Bioversity details come from the guidelines)

### 0.1 General

- Address: `https://eu2.concursolutions.com` (sign in with CGIAR SSO and Authenticator).
- The language depends on each user's profile: with British English the report is called **Expense Claim**; with US English, **Expense Report**. Read the screen before looking for a button by name. Dates are in MM/DD/YYYY format.
- Paths: requests `/nui/travelrequest`; expenses `/nui/expense` (reports, "Available Expenses", "Available Receipts"); a report `/nui/expense/reports/<id>`; an expense `/nui/expense/reports/<id>/expenses/<id>`.
- Home page: "Requests", "Expense Reports", "Available Expenses" and "Approvals" (items the person must approve as a supervisor: do not touch).
- Company notice on the home page: corporate card expenses have a limit of **40 days** after return. The policy says 15 days to submit the expense report: aim for 15.
- "View" filters: in Manage Expenses → Active, Sent for Payment (90 Days), Last 90 Days, This Year, Last Year, Date Range; in Manage Requests → Active, Not Submitted, Pending Approval, Approved, Cancelled, Closed, All Requests.

### 0.2 Request (Create New Request)

| Field | Notes |
|---|---|
| Commitment ID | Locked; filled in automatically on submission |
| Travel Type * | International / National |
| Trip Title * | Help text: "Where, When and What, e.g. Rome 15-16 august 2024 finance retreat" |
| Start Date *, End Date * | Duration (Days) is calculated automatically |
| Trip Purpose * | Alliance Workshop · Donors visit · Donors visit & Other · External Meeting · Field trip · Field Trip & Other · Harvest work · Hosted Meeting · HR Travel (Appointment / Compassionate / Relocation / Separation) · Internal Meeting · Non-alliance workshop · Office Visit · Office Visit & Other · OneCG Meeting · OneCG Meeting & Other · Other · Planning · Planting work · Process review and control · Technical Visits · Visit Partners · Visit partners - Others |
| Non Staff, Personal Travel on this trip | Checkboxes |
| Name (Non-staff), ID Number / Nationality (Non-staff), Family Members | Only if applicable |
| Insert CIAT * (1) → Insert ALL * (2) → Insert the AEC * (3) | Cascading list: choosing the code in (1) fills in (2) and (3). Options such as "(CIAT-ALL-XXXXXXXXTV2) Travel". Help text: filter on "Either". Includes "Most Recently Used" |
| UNIT | Locked; comes from the profile |
| Accounting Office * | Three-letter code of the hub that issues the cash advance or processes the report (Nairobi: **NBO**). Replaces "Cash Advance Entity" and "Travel Office" from the guideline |
| Comment | 500 characters |

"Create Request" saves a draft; it does not submit. In the expected expense lines, M&I and hotel are calculated using the destination's DSA rate (in the request it appears as "Destination City – Room (R) & Per-diem (P) rates in US$", e.g. "(Elsewhere-ES) Elsewhere").

Actual error when submitting with a non-travel AEC: "Unable to proceed: The AEC … Check BUS status, please contact the Finance Team". It was resolved by using the travel AEC (ending in TV2).

### 0.3 Approved request → create the report

The approved request shows **"Create Expense Report"** at the top right, along with the menus Request Details (Request Header / Request Timeline / Audit Trail), Print/Share and Attachments. That button creates the report linked to the TR. Alternative: Expense → Create Expense Report/Claim → "Create from an Approved Request".

### 0.4 Report header (Report Details → Report Header)

Fields: Commitment ID (locked), Report Name *, Report Date, Trip Purpose *, Report Type, CIA * / ALL * / AEC *, Non Staff Name, ID Number / Nationality, Accounting Office *, Report Number, **Personal Travel on this trip** (None Selected / No / Yes), **Reimbursement Currency *** and Comment (500).

- **Reimbursement Currency** is required and must be valid for the Accounting Office; if it is missing, two errors appear that block submission. For NBO, "(USD) US Dollar" and "(KES) Kenyan Shilling" appear at the top. Ask which one: it depends on the account the reimbursement is paid into.
- With personal days: "Personal Travel on this trip" = Yes, plus a line in Comment for the expense processor.

### 0.5 Expense detail

Tabs Details / Itemizations / Allocations. Fields: Expense Type *, Transaction Date *, Business Purpose, City of Purchase *, Payment Type *, Amount *, Currency *, Exchange Rate *, Amount in USD *, Supplier, Request * (only if the type was in the TR), Comment (500), and the receipt viewer (Upload New Receipt / Choose From Available Receipts; with a receipt: Remove / Add / Open). Hotel adds Date Range * and Nights.

- **Supplier is required for CIAT-entity users** even though it has no asterisk (Bioversity does not have this field, according to the guideline): without it you get "PROVEE - You need to enter the name of the supplier". Use "(00000000) N/A" when the merchant is not registered. Some agencies are registered: "(KENP000599474Q) SATGURU TRAVEL AND TOUR SERVICES LIMITED".
- **Payment Type**: "Out-of-Pocket" (paid by the traveler: cash or personal card), "Company Paid" (paid by the Alliance, e.g. the agency ticket) and, with a corporate card, the name of the issuing bank with a card icon. Corporate card purchases arrive automatically in "Available Expenses" with supplier, city and amount; only the type and receipt are missing. "Card Transactions" (in Manage Expenses) shows whether the person has a corporate card loaded.
- **City of Purchase** sets the currency and the exchange rate for the transaction date (Paris/Madrid/Granada → EUR; Nairobi → KES). For a ticket paid in USD, change the currency to USD manually.
- **Request**: links automatically to the approved line of the same type ("10/25/2026, $585.78 - …"). Types with no line in the TR (Local Transport, Fare National) do not show the field and save anyway.

### 0.6 Expense types (full list seen in a CIAT report, Nov 2026)

- **01. Travel**: Hotel / Room Allowance · Hotel / Room Allowance - Manual · Meals and incidentals · Meals and Incidentals - Manual · Travel Expenses - General & miscellaneous · Unsupported Colombia - Meals and Incidentals - Expenses
- **02. Transportation**: Fare Int. (air tkt and other long-distance transport) · Fare National (air tkt and long-distance transport) · Local Transport (short distance, train, taxi, bus, etc.)
- **03. Communication**: Representation - Hospitality Expenses
- **04. Fees**: Visas
- **05. Meetings and Events**: Workshop - (non staff) Meals and Incidentals · Workshops - (non-staff) Accommodation · Workshops - (non-staff) General & Miscellaneous Expenses · Workshops - (non-staff) Ticket Costs
- **06. HR Related Travel**: Travel - Appointment · Travel - Compassionate. · Travel - Relocation · Travel- Repatriation
- **07. Training**: Professional Development (Staff development + travel)
- **08. Accounts Receivable**: A/R Employees for Travel and Office Expenses
- **09. Field Work Activities**: Expenses non-staff - Field operations - wages · General services in official travel · Guides and similar expenses · Representation expenses · Supplies in official travel

Practical use (report accepted as a draft with no errors, Nov 2026):

| Expense | Type | Payment | Date | Supporting document |
|---|---|---|---|---|
| Each meal (urban, actual cost) | Meals and incidentals | Out-of-Pocket | receipt date | receipt |
| Uber, taxi, transfer to the airport or station | Local Transport | Out-of-Pocket | receipt date | receipt or app confirmation |
| Air ticket from the agency | Fare Int. | Company Paid | ticket issue date | agency email or invoice + boarding passes (merged into a single attachment) |
| Intercity train or bus paid by the traveler | Fare National | Out-of-Pocket | ticket purchase date | ticket showing the price |

### 0.7 Alerts observed

Errors (block submission):
- "The Reimbursement Currency you have selected is not valid for this Accounting Office" / "The report header is missing data in this required field(s): Reimbursement Currency".
- "PROVEE - You need to enter the name of the supplier".

Warnings (do not block):
- "You must attach a receipt image to this expense" (only on expenses above the receipt threshold).
- "Please ensure your cash advance is issued by the processor…" (standing reminder).
- "Please ensure you reconcile the expense type Fare National or Fare International…" (standing reminder; it stays even when the ticket is loaded).
- "The transaction date is older than your company allows. Please provide an explanation…" (tickets bought weeks in advance): explain in the comment.

### 0.8 CIAT vs. Bioversity (according to the 2023 guidelines; confirm on screen)

Each employee belongs to one legal entity; it shows in the header fields.

| Topic | CIAT entity | Bioversity entity |
|---|---|---|
| Budget code | Cascading CIAT / ALL / AEC list, e.g. "(CIAT-ALL-XXXXXXXXTV2) Travel". The travel AEC ends in TV | A… - B… - C… code, e.g. "A1301-B100695-C100509". Search filter on "either" |
| Extra fields on each expense | Supplier (required; "(00000000) N/A" if not registered) and Receipts Status; in Palmira, itemizations | No extra fields: Save Expense |
| Default currency | The hub's currency (e.g. COP in Palmira, KES in Nairobi) | USD |
| Non-staff in the TR | Full name + passport/ID and nationality | Name + Supplier ID provided by Accounts Payable (Alliance-AccountsPayableRome@cgiar.org) |
| Personal portion (A/R Employees) | Account 35010 | Account 33002 |
| Report approval flow | Always goes through review (clearance) | May go directly to the expense processor |
| Currencies accepted in Agresso | CIAT list (§4) | Bioversity list (§4) |
| M&I in Palmira | "Unsupported Palmira Per-diem Expenses" exists | Not applicable |

Intra-Alliance expense (contract held by one entity, paid by the other): the other entity's code cannot be entered; write in the Comments of the header and of each expense "Intra-Alliance, the real expense will be covered by <entity> <code>".

### 0.9 Hubs, agencies and contacts

Accounting Office: three-letter code of the hub that processes the report (Nairobi = **NBO**). If unknown, look it up in one of the person's previous TRs (Request Header).

Institutional travel agencies according to the 2024–2025 travel mapping (confirm with the hub's travel office; they change with contracts):

| Region / hub | Agency |
|---|---|
| Africa (Nairobi and others) | FCM Travel and Satguru Travel ("SATGURU TRAVEL AND TOUR SERVICES LIMITED" is registered as a supplier in Concur) |
| Americas | Carlson Wagonlit (CWT) |
| Asia | FCM (Malaysia), Mayflower (Malaysia), Travel Experts (India), Joytours and Green Paradise (Vietnam, Laos, Philippines) |
| Italy (Rome) | Uvet American Express |
| Montpellier | Havas Voyages |
| Leuven | Omnia Travel (KU Leuven's agency) |

Contacts:
- Concur support (access, profiles, errors): Alliance-ITsupport@cgiar.org.
- Corporate card: Alliance-CorporateCreditCard@cgiar.org.
- Europe travel office: alliance-traveleurope@cgiar.org.
- Guidelines, videos and FAQs: Alliance-Finance SharePoint ("What you need to know about SAP Concur", "Frequently SAP Concur Asked Questions", "Travel Buddy").
- Each region has Concur "Champions" (go-to users) who answer local questions.

## 1. Expense types and accounts

Staff travel (97… accounts):

| Type (guideline name) | Account | Used for |
|---|---|---|
| Fare – National | 97002 | Domestic ticket or fare (air, train, boat, intercity bus) |
| Fare – International | 97006 | International ticket |
| Local Transportation (Taxis, trains & Buses) | 97206 | Taxi, metro, city bus, commuter train, airport transfers |
| Hotel – Room Allowance | 97202 | Accommodation |
| Meals and Incidentals | 97204 | Meals and incidentals (formerly "per diem") |
| Unsupported Palmira Per-diem Expenses | 97203 | CIAT only |
| Travel Expenses – General & miscellaneous | 97201 | Anything that does not fit the others: SIM/eSIM, travel insurance, airport fees, approved excess baggage |
| Visas | 97220 | Visa, photos, entry permits |
| Representation – Hospitality Expenses | 97224 | Hosting guests and group meals |
| Professional Development | 91244 | Training (course + travel) |
| A/R Employees for Travel and Office Expenses | 33002 (Bioversity) / 35010 (CIAT) | Personal portion of the trip, or a cost paid by a third party |
| Cash Advance Return | — | Unused balance of the cash advance |

Alliance workshops with non-staff participants (94… accounts, purpose "Alliance Workshop"):

| Type | Account |
|---|---|
| Workshops – (non-staff) General & Miscellaneous Expenses | 94202 |
| Workshops – (non-staff) Ticket Costs | 94204 |
| Workshops – (non-staff) Accommodation | 94206 |
| Workshops – (non-staff) Meals and incidentals | 94207 |

Workshop costs (venue, catering, refreshments, M&I paid on site to participants) go in a separate TR raised by the responsible staff member, using 94… accounts. Each non-staff participant has their own TR and their own expense report. Non-staff cannot request a cash advance. Staff attending a workshop use the regular 97… accounts.

HR travel (appointment, relocation, repatriation, compassionate) has its own accounts and the "NON AEC" code: see the TR guideline.

## 2. Policy rules that most often get reports sent back

- **Deadline**: expense report within 15 calendar days after return. Late reports may not be processed. No new cash advance is issued while an earlier one has not been settled with an expense report.
- **TR before anything else**: approved before departure and before any spending, even if the trip costs the Alliance nothing (zero-cost TR with Fare at 0). It also serves as security authorization and for insurance.
- **Receipts**: required except for transactions under USD 25 (corporate card) or USD 15 (other payment methods).
- **Air tickets**: only through the institutional agency; reported with the e-ticket and boarding passes, payment "Company Paid". Tickets bought elsewhere are not reimbursed without an approved exception.
- **Hotel**: capped at 120 % of the UN rate, with the hotel invoice. In Palmira, stay on campus.
- **Hospitality**: receipt + names of attendees, their entity and the reason. The employee deducts their own portion from their M&I.
- **Personal portion (personal days)**: the Alliance pays only the official part. Tick "Personal Travel on this trip", do not enter expenses for those days and, if the ticket cost more because of the personal days, charge the difference as A/R Employees. Calculating it requires a quote with the return on the official date; if there is none, flag it.
- **Other items reimbursable with a receipt**: transfers to terminals, local transport, visas, airport fees, excess baggage for documents (with prior approval), travel insurance, SIM/eSIM.
- **Not reimbursable**: miles or rewards, in-room movies, fines, non-work expenses. Vaccines and prophylaxis go to the health insurance (Cigna).
- **Lost receipt**: "Missing Receipt Declaration" form (Manage Receipts → Missing Receipt Declaration).
- **Corporate card**: cardholders should not request a cash advance for hotel and meals, nor out-of-pocket reimbursement.
- **Private car**: UN rate per mile (in USD) plus tolls and parking.
- **Multiple overland trips**: a single monthly TR and a single monthly expense report are allowed.
- **Exchange rate**: the rate on the transaction date, which Concur applies automatically.
- Europe only: air tickets in EUR.

## 3. Meals and Incidentals (M&I)

- Daily cap: 80 % of the UN rate for the destination (DSA calculator in Power BI). In practice: M&I amount approved in the TR ÷ days in the TR. Do not make it up.
- Daily split: breakfast 15 %, lunch 30 %, dinner 40 %, incidentals 15 %. Meals can offset each other, but the day's total cannot exceed the cap.
- Meals provided (hotel breakfast, event lunch, hosted dinner): their percentage is deducted.
- **Urban area**: actual cost with receipts (one line per receipt); the cap is still the day's M&I.
- **Rural area**: claimed per day using the percentages, without receipts.
- **Incidentals**: up to 15 % of M&I, no receipt needed. They are actual costs, not an automatic entitlement.
- Requires at least one night away.
- Trips longer than 15 days: agree on a cheaper alternative with the supervisor.
- The old guideline asked for a single M&I line with the sheet "Alliance Meals & Incidentals Claim SAP Concur.xlsx"; in current urban reports each receipt is entered and the day-by-day expense sheet is attached (see SKILL.md, step 8).

Cap example: USD 60, hotel with breakfast, lunch provided by the event → claimable that day = 60 × (40 % dinner + 15 % incidentals) = USD 33.

## 4. Currencies enabled in Agresso

If the currency is not on the entity's list, it is recorded as its USD equivalent.

- **Bioversity**: AUD, BIF, CAD, CHF, COP, CRC, CZK, DKK, ETB, EUR, GBP, INR, JPY, KES, MAD, MWK, MYR, NOK, NPR, NZD, PEN, PHP, SEK, THB, UGX, USD, UZS, VND, XAF, XOF, ZAR.
- **CIAT**: AUD, CAD, CDF, CHF, COP, EUR, GBP, HNL, JPY, KES, LAK, MWK, NIO, NOK, PEN, PHP, RWF, TZS, UGX, USD, VND, XOF, ZAR, ZMW, ZWL.

2023 list: if Concur rejects a currency, use USD and flag it.

## 5. Fields by type (according to the 2023 guideline)

- **Transaction Date**: date of the invoice or receipt. For tickets, the issue date.
- **City of Purchase**: where the expense was incurred; it sets the currency.
- **Amount** and **Currency**: actual amount on the supporting document.
- **Hotel**: check-in and check-out as per the invoice (nights are calculated automatically). Total invoice amount.
- **Fare National / International**: amount on the e-ticket or ticket. Company Paid if the agency bought it; Out-of-Pocket if the traveler paid (e.g. a train ticket bought online).
- **A/R Employees**: amount payable by the traveler.
- **Cash Advance Return**: "Remaining" balance of the cash advance, in the default currency. E.g.: advance 500, out-of-pocket expenses 300 → return 200.
- Report status: Report Details → Report Timeline. The report can be **Recall**ed as long as the processor has not approved it.

## 6. Request fields (according to the guideline)

- **Trip Title**: maximum 32 characters, "where – when – what". Migrates to Agresso.
- **Budget code / AEC**: filter on "either". CIAT: CIAT/Project = CIAT, ALL/BUS = ALL, travel AEC (ending in TV). For another code or entity, use **Allocate** on each expense.
- Intra-Alliance expense (contract held by one entity, paid by the other): note it in the Comments of the header and of each expense, with the real code.
- **Fare**: agency quote; country of origin and final destination; itinerary in Comments. Ticket paid by a third party: Fare at 0. If there is an intercity train or bus leg, add it too.
- **Meals & Incidentals / Hotel**: destination country and city; the system calculates using the DSA rate. Days can be reduced, not increased.
- **Cash Advance**: Request Details → Add Cash Advance; in USD or in the default currency.
- To cancel a trip use **Cancel Request**, never Close Request; if expenses have already been incurred, it cannot be cancelled: submit an expense report instead.

## 7. Alerts and support

- **Red** alerts (Error): block submission. Yellow (Warning): do not block.
- HRCOUNTR: the TR needs security clearance. TGCYPPRV: the travel office's or agency's approval to issue the ticket is missing.
- Concur support: Alliance-ITsupport@cgiar.org. Corporate card: Alliance-CorporateCreditCard@cgiar.org.
