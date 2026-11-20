# legalizar-viaje

A Claude skill that prepares **SAP Concur** travel requests (Travel Request) and expense reports (Expense Report / Expense Claim) for any staff member of the **Alliance of Bioversity International and CIAT**, whether in the CIAT or Bioversity entity and at any hub.

*The name is Spanish for "settle a trip's expenses". The skill talks to each person in their own language (English, Spanish, French…) and always writes in English in Concur and in the expense sheet.*

## What it does

- Reads receipts, tickets and boarding passes (PDFs or photos) and builds the expense table.
- Asks the questions only the traveler can answer: personal days, who paid what, cash advance, etc.
- Fills in the report in Concur through the browser: header, lines and attached receipts. Everything stays **as a draft**.
- Generates the supporting expense sheet (Excel + PDF), with totals that match Concur to the cent.
- Ends with a summary that separates what the Alliance paid (Company Paid) from what is reimbursed.

It **never** submits the report, approves anything or types passwords. The person has to step in at four points, and the skill says so up front: logging in, answering questions, uploading files and submitting the report.

## Install

**Claude app (desktop or claude.ai):** download `legalizar-viaje.skill` from [Releases](../../releases) and upload it in the skills settings (Capabilities → Skills).

**Claude Code:**

```bash
git clone https://github.com/byliz-ai/legalizar-viaje.git ~/.claude/skills/legalizar-viaje
```

To update: `git -C ~/.claude/skills/legalizar-viaje pull`.

## Requirements

- Skills enabled in Claude.
- A browser Claude can drive: the Browser pane in the Claude app or the Claude in Chrome extension. Without a browser, the skill still builds the table and the expense sheet, and the person types the data into Concur.
- A Concur session opened by the person (`eu2.concursolutions.com`).
- Python 3 with `openpyxl` (and `reportlab` for the PDF), for the expense sheet.

## First use

The first time, the skill asks for the basics and saves them in `~/.claude/legalizar-viaje/profile.md`: entity, hub, unit, reimbursement currency, corporate card, travel agency and browser. That profile stays **only on each person's computer**; it is not part of this repo.

To start, just tell Claude something like "I need to do the expense report for my trip to Rome" or "help me with Concur".

## Contents

| File | Purpose |
|---|---|
| `SKILL.md` | The skill's instructions: steps, when the person steps in, rules |
| `references/alliance-concur.md` | Alliance travel policy and Concur screens: expense types, CIAT vs Bioversity, hubs, agencies, contacts |
| `references/concur-browser.md` | How to drive Concur forms from the browser |
| `scripts/expense_sheet.py` | Generates the expense sheet (Excel + PDF) |
| `assets/example_sheet.json` | Sample input for the script |
| `assets/profile-template.md` | Template for each person's profile |

## Status

Tested end to end on a real 23-line report (CIAT, personal card, Nov 2026). These parts come from the Finance guides and haven't been tested live yet: the corporate card flow, Bioversity specifics and the delegate option. If something in Concur doesn't match, the skill says so and offers to fix the reference.

This is an unofficial, personal project; it is not maintained or endorsed by the Alliance's Finance team. Alliance policy always takes precedence over what's written here.

## Privacy

Don't commit receipts, expense sheets, profiles or anyone's data to this repo; the `.gitignore` blocks the most common formats. Before using the skill with financial information, check that the Alliance's AI use policy allows it.
