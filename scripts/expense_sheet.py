#!/usr/bin/env python3
"""Builds the supporting expense sheet (Excel + PDF) for a Concur expense report.

Format of the template some Alliance processors ask for ("Travel expenses <trip>.xlsx"):
a PERDIEM block (one row per day: Breakfast / Lunch / Dinner / Meals / Room allowance /
Incidentals / Total per diem, in USD), an "Other expenses" block and an "Overall Total".

Each amount is converted with the rate Concur applied and rounded per receipt, just like
Concur, so the total matches the reimbursement in the report to the cent.

Usage:
    python3 expense_sheet.py data.json output.xlsx [output.pdf]

data.json (see assets/example_sheet.json):
{
  "title": "Name - Trip - Travel Request XXXX / Expense Report YYYY",
  "approved_mi_usd": 300.00,                 # optional: M&I approved in the TR
  "days": [
    {"date": "10th March", "location": "Rome", "rate": 1.10,
     "breakfast": [6.50], "lunch": [18.00], "dinner": [25, 3.5],
     "lodging": [], "incidentals": [],
     "dinner_comment": "optional text, stored as a cell comment"}
  ],
  "other": [
    {"description": "Taxi home - airport", "date": "9th March",
     "currency": "KES", "amount": 2000, "rate": 0.0077}
  ],
  "notes": ["..."]
}
Amounts under "days" are in that day's local currency (the one "rate" converts); the result is USD.
"""
import json
import sys

try:
    from openpyxl import Workbook
except ImportError:
    sys.exit("openpyxl is missing. Install it with: python3 -m pip install openpyxl")

from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

ARIAL = "Arial"
BLUE = "0000FF"
USD_FMT = '_(* #,##0.00_);_(* \\(#,##0.00\\);_(* "-"??_);_(@_)'
MEALS = [("B", "breakfast", "Breakfast"), ("C", "lunch", " Lunch"), ("D", "dinner", " Dinner")]


def f(bold=False, color=None, size=10):
    return Font(name=ARIAL, bold=bold, color=color, size=size)


def r2(x):
    # "Half up" rounding like Concur, avoiding Python's banker's rounding.
    return float(f"{x + 1e-9:.2f}") if x >= 0 else -float(f"{-x + 1e-9:.2f}")


def formula(amounts, row):
    if not amounts:
        return None
    return "=" + "+".join(f"ROUND({a}*$J{row},2)" for a in amounts)


def value(amounts, rate):
    return round(sum(r2(a * rate) for a in amounts), 2)


def build(data, xlsx_path):
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    border = Border(*(Side(style="thin", color="999999"),) * 4)

    ws["A1"] = data.get("title", "")
    ws["A1"].font = f(True, size=11)

    ws.merge_cells("A2:H2")
    ws["A2"] = "PERDIEM"
    ws["A2"].font = f(True)
    header = ["Date", "Breakfast", " Lunch", " Dinner", "Meals", "Room allowance",
              " Incidentals", "Total per diem", "Location", "Exchange rate to USD (Concur)"]
    for i, h in enumerate(header):
        c = ws.cell(row=3, column=i + 1, value=h)
        c.font = f(True)
        c.border = border
        c.alignment = Alignment(horizontal="center", wrap_text=True)
    for col in "BCDEFGH":
        ws[f"{col}4"] = "USD"
        ws[f"{col}4"].font = f(True)
        ws[f"{col}4"].alignment = Alignment(horizontal="center")

    calc = {"days": [], "per_diem": 0.0, "other": [], "other_total": 0.0}
    row = 5
    for d in data["days"]:
        rate = d["rate"]
        ws[f"A{row}"] = d["date"]
        day = {"date": d["date"], "location": d.get("location", ""), "rate": rate}
        for col, key, _ in MEALS:
            a = d.get(key, [])
            if a:
                ws[f"{col}{row}"] = formula(a, row)
            day[key] = value(a, rate)
            note = d.get(f"{key}_comment")
            if note:
                ws[f"{col}{row}"].comment = Comment(note, "Claude")
        ws[f"E{row}"] = f"=SUM(B{row}:D{row})"
        lodging, incidentals = d.get("lodging", []), d.get("incidentals", [])
        if lodging:
            ws[f"F{row}"] = formula(lodging, row)
        if incidentals:
            ws[f"G{row}"] = formula(incidentals, row)
            if d.get("incidentals_comment"):
                ws[f"G{row}"].comment = Comment(d["incidentals_comment"], "Claude")
        day["lodging"] = value(lodging, rate)
        day["incidentals"] = value(incidentals, rate)
        day["meals"] = round(day["breakfast"] + day["lunch"] + day["dinner"], 2)
        day["total"] = round(day["meals"] + day["lodging"] + day["incidentals"], 2)
        calc["days"].append(day)
        calc["per_diem"] = round(calc["per_diem"] + day["total"], 2)
        ws[f"H{row}"] = f"=SUM(E{row}:G{row})"
        ws[f"I{row}"] = d.get("location", "")
        ws[f"J{row}"] = rate
        ws[f"J{row}"].font = f(color=BLUE)
        ws[f"J{row}"].number_format = "0.0000"
        for col in "BCDEFGH":
            ws[f"{col}{row}"].number_format = "0.00"
        row += 1
    last = row - 1
    pd_sum = row
    ws[f"G{pd_sum}"] = "Sum"
    ws[f"G{pd_sum}"].font = f(True)
    ws[f"H{pd_sum}"] = f"=SUM(H5:H{last})"
    ws[f"H{pd_sum}"].font = f(True)
    ws[f"H{pd_sum}"].number_format = USD_FMT
    if data.get("approved_mi_usd") is not None:
        ws[f"G{pd_sum + 1}"] = "Approved in TR"
        ws[f"H{pd_sum + 1}"] = data["approved_mi_usd"]
        ws[f"H{pd_sum + 1}"].font = f(color=BLUE)
        ws[f"H{pd_sum + 1}"].number_format = USD_FMT
        ws[f"I{pd_sum + 1}"] = "Meals and incidentals approved in the Travel Request (USD)"

    oe = pd_sum + 3
    ws.merge_cells(f"A{oe}:H{oe}")
    ws[f"A{oe}"] = "Other expenses"
    ws[f"A{oe}"].font = f(True)
    for col, h in zip("ABCDGH", ["Description", "Date", "Currency", "Amount", "Exchange rate", "Amount in USD"]):
        c = ws[f"{col}{oe + 1}"]
        c.value = h
        c.font = f(True)
        c.border = border
    row = oe + 2
    first = row
    for o in data.get("other", []):
        ws[f"A{row}"] = o["description"]
        ws[f"B{row}"] = o["date"]
        ws[f"C{row}"] = o["currency"]
        ws[f"D{row}"] = o["amount"]
        ws[f"D{row}"].font = f(color=BLUE)
        ws[f"D{row}"].number_format = USD_FMT
        ws[f"G{row}"] = o["rate"]
        ws[f"G{row}"].font = f(color=BLUE)
        ws[f"G{row}"].number_format = "0.0000000"
        ws[f"H{row}"] = f"=ROUND(D{row}*G{row},2)"
        ws[f"H{row}"].number_format = "0.00"
        usd = r2(o["amount"] * o["rate"])
        calc["other"].append({**o, "usd": usd})
        calc["other_total"] = round(calc["other_total"] + usd, 2)
        row += 1
    o_sum = row + 1
    ws[f"G{o_sum}"] = "Sum"
    ws[f"G{o_sum}"].font = f(True)
    ws[f"H{o_sum}"] = f"=SUM(H{first}:H{max(first, row - 1)})"
    ws[f"H{o_sum}"].font = f(True)
    ws[f"H{o_sum}"].number_format = USD_FMT

    tot = o_sum + 2
    ws[f"A{tot}"] = "Overall Total "
    ws[f"A{tot}"].font = f(True)
    ws[f"H{tot}"] = f"=H{o_sum}+H{pd_sum}"
    ws[f"H{tot}"].font = f(True)
    ws[f"H{tot}"].number_format = USD_FMT
    ws[f"H{tot}"].fill = PatternFill("solid", fgColor="F2F2F2")
    calc["total"] = round(calc["per_diem"] + calc["other_total"], 2)

    n = tot + 2
    ws[f"A{n}"] = "Notes"
    ws[f"A{n}"].font = f(True)
    for i, t in enumerate(data.get("notes", []), start=1):
        ws[f"A{n + i}"] = t
        ws[f"A{n + i}"].font = f()

    for k, v in {"A": 34, "B": 14, "C": 14, "D": 14, "E": 12, "F": 15, "G": 14, "H": 17, "I": 34, "J": 16}.items():
        ws.column_dimensions[k].width = v
    for cells in ws.iter_rows():
        for c in cells:
            if c.font and c.font.name != ARIAL:
                c.font = Font(name=ARIAL, bold=c.font.b, color=c.font.color, size=c.font.sz or 10)
    ws.row_dimensions[3].height = 30
    ws.freeze_panes = "A5"
    wb.save(xlsx_path)
    return calc


def pdf(data, calc, pdf_path):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    def m(x):
        return f"{x:,.2f}" if x else ""

    ss = getSampleStyleSheet()
    small = ss["Normal"]
    small.fontName = "Helvetica"
    small.fontSize = 8
    el = [Paragraph(data.get("title", ""), ss["Heading3"]), Paragraph("PERDIEM", ss["Heading4"])]
    t = [["Date", "Breakfast", "Lunch", "Dinner", "Meals", "Room allowance", "Incidentals",
          "Total per diem", "Location", "Rate to USD (Concur)"], [""] + ["USD"] * 7 + ["", ""]]
    for d in calc["days"]:
        t.append([d["date"], m(d["breakfast"]), m(d["lunch"]), m(d["dinner"]), m(d["meals"]),
                  m(d["lodging"]), m(d["incidentals"]), m(d["total"]), d["location"], f"{d['rate']:.4f}"])
    t.append(["", "", "", "", "", "", "Sum", f"{calc['per_diem']:,.2f}", "", ""])
    if data.get("approved_mi_usd") is not None:
        t.append(["", "", "", "", "", "", "Approved in TR", f"{data['approved_mi_usd']:,.2f}",
                  "M&I approved in the Travel Request (USD)", ""])
    n_sum = 2 + len(calc["days"])
    tb = Table(t, repeatRows=1)
    tb.setStyle(TableStyle([("FONT", (0, 0), (-1, -1), "Helvetica", 7.5), ("FONT", (0, 0), (-1, 1), "Helvetica-Bold", 7.5),
                            ("GRID", (0, 0), (-1, n_sum), 0.3, colors.grey), ("ALIGN", (1, 2), (7, -1), "RIGHT"),
                            ("FONT", (6, n_sum), (7, n_sum), "Helvetica-Bold", 7.5)]))
    el += [tb, Spacer(1, 10), Paragraph("Other expenses", ss["Heading4"])]
    o = [["Description", "Date", "Currency", "Amount", "Exchange rate", "Amount in USD"]]
    for x in calc["other"]:
        o.append([x["description"], x["date"], x["currency"], f"{x['amount']:,.2f}", f"{x['rate']:.7f}", f"{x['usd']:,.2f}"])
    o.append(["", "", "", "", "Sum", f"{calc['other_total']:,.2f}"])
    k = len(o) - 1
    t2 = Table(o)
    t2.setStyle(TableStyle([("FONT", (0, 0), (-1, -1), "Helvetica", 7.5), ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 7.5),
                            ("GRID", (0, 0), (-1, k - 1), 0.3, colors.grey), ("ALIGN", (3, 1), (-1, -1), "RIGHT"),
                            ("FONT", (4, k), (5, k), "Helvetica-Bold", 7.5)]))
    el += [t2, Spacer(1, 8)]
    t3 = Table([["Overall Total (USD, reimbursable to traveler)", f"{calc['total']:,.2f}"]])
    t3.setStyle(TableStyle([("FONT", (0, 0), (-1, -1), "Helvetica-Bold", 9), ("BOX", (0, 0), (-1, -1), 0.5, colors.black)]))
    el += [t3, Spacer(1, 8)]
    if data.get("notes"):
        el.append(Paragraph("<b>Notes</b>", small))
        el += [Paragraph("• " + n, small) for n in data["notes"]]
    SimpleDocTemplate(pdf_path, pagesize=landscape(A4), leftMargin=24, rightMargin=24,
                      topMargin=24, bottomMargin=24).build(el)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as fh:
        data = json.load(fh)
    calc = build(data, sys.argv[2])
    if len(sys.argv) > 3:
        try:
            pdf(data, calc, sys.argv[3])
        except ImportError:
            print("WARNING: reportlab is missing, the PDF was not created. Install it with "
                  "'python3 -m pip install reportlab' or open the Excel file and export it as PDF.",
                  file=sys.stderr)
    print(json.dumps({"per_diem_usd": calc["per_diem"], "other_usd": calc["other_total"],
                      "total_usd": calc["total"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
