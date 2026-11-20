# alliance-concur-travel

A Claude skill that prepares **SAP Concur** travel requests (Travel Request) and expense reports (Expense Report / Expense Claim) for any staff member of the **Alliance of Bioversity International and CIAT**, whether in the CIAT or Bioversity entity and at any hub.

*The skill talks to each person in their own language (English, Spanish, French…) and always writes in English in Concur and in the expense sheet.*

## What it does

- Reads receipts, tickets and boarding passes (PDFs or photos) and builds the expense table.
- Asks the questions only the traveler can answer: personal days, who paid what, cash advance, etc.
- Fills in the report in Concur through the browser: header, lines and attached receipts. Everything stays **as a draft**.
- Generates the supporting expense sheet (Excel + PDF), with totals that match Concur to the cent.
- Ends with a summary that separates what the Alliance paid (Company Paid) from what is reimbursed.

It **never** submits the report, approves anything or types passwords. The person has to step in at a few points, and the skill says so up front: logging in, answering questions, uploading files, submitting the report and approving what the skill learns.

## Install

**Claude app (desktop or claude.ai):** download `alliance-concur-travel.skill` from [Releases](../../releases) and upload it in the skills settings (Capabilities → Skills).

**Claude Code:**

```bash
git clone https://github.com/byliz-ai/alliance-concur-travel.git ~/.claude/skills/alliance-concur-travel
```

To update: `git -C ~/.claude/skills/alliance-concur-travel pull`. In the Claude app, download the new `.skill` and upload it again. The skill checks for a newer version at the start of each use and tells you.

## Requirements

- Skills enabled in Claude.
- A browser Claude can drive: the Browser pane in the Claude app or the Claude in Chrome extension. Without a browser, the skill still builds the table and the expense sheet, and the person types the data into Concur.
- A Concur session opened by the person (`eu2.concursolutions.com`).
- Python 3 with `openpyxl` (and `reportlab` for the PDF), for the expense sheet.

## First use

The first time, the skill asks for the basics and saves them in `~/.claude/alliance-concur-travel/profile.md`: entity, hub, unit, reimbursement currency, corporate card, travel agency and browser. That profile stays **only on each person's computer**; it is not part of this repo.

In Claude Code or the desktop app's Code tab, the profile file persists between uses. In the Claude chat app each conversation starts from scratch, so the skill hands you the profile as text at the end, to keep in a Claude Project or in Claude's memory.

To start, just tell Claude something like "I need to do the expense report for my trip to Rome" or "help me with Concur".

## How it learns

The skill learns from every use at two levels, and nothing is saved or shared without your OK:

1. **Your profile (private).** At the end, the skill proposes up to three updates to your profile: settings and **lessons**, such as what a processor asked for or why a report was sent back. Next time it checks your report against those lessons before you submit.
2. **The skill itself (shared).** If something is useful for everyone (a Concur screen that changed, a new error, a rule of your hub or entity, a processor's comment), the skill drafts an anonymous **field note**. You decide whether to send it:
   - with a GitHub account: [open a Field note issue](../../issues/new/choose) and paste it (issues here are public);
   - without GitHub: send it to whoever shared the skill with you.

   The maintainer reviews the notes, updates the references and publishes a new release.

Reports that were sent back are the most valuable source: each processor comment is a real rule for that hub.

## Contents

| File | Purpose |
|---|---|
| `SKILL.md` | The skill's instructions: steps, when the person steps in, rules |
| `references/alliance-concur.md` | Alliance travel policy and Concur screens: expense types, CIAT vs Bioversity, hubs, agencies, contacts |
| `references/concur-browser.md` | How to drive Concur forms from the browser |
| `scripts/expense_sheet.py` | Generates the expense sheet (Excel + PDF) |
| `assets/example_sheet.json` | Sample input for the script |
| `assets/profile-template.md` | Template for each person's profile, including lessons |
| `assets/field-note-template.md` | Template for the anonymous field note |
| `references/maintaining.md` | For the maintainer: processing field notes and publishing releases |
| `.github/ISSUE_TEMPLATE/field-note.yml` | The "Field note" issue form |

## Status

Tested end to end on a real 23-line report (CIAT, personal card, Nov 2026). These parts come from the Finance guides and haven't been tested live yet: the corporate card flow, Bioversity specifics and the delegate option. If something in Concur doesn't match, the skill says so, goes with what's on screen and drafts a field note.

This is an unofficial, personal project; it is not maintained or endorsed by the Alliance's Finance team. Alliance policy always takes precedence over what's written here.

## Privacy

Don't commit receipts, expense sheets, profiles or anyone's data to this repo; the `.gitignore` blocks the most common formats. Before using the skill with financial information, check that the Alliance's AI use policy allows it.
