#!/usr/bin/env python3
"""Genera la hoja de gastos de soporte (Excel + PDF) para una legalización en Concur.

Formato del modelo que piden algunos procesadores de la Alliance ("Travel expenses <viaje>.xlsx"):
bloque PERDIEM (una fila por día: Breakfast / Lunch / Dinner / Meals / Room allowance /
Incidentals / Total per diem, en USD), bloque "Other expenses" y "Overall Total".

Cada monto se convierte con la tasa que aplicó Concur y se redondea por recibo, igual que
Concur, para que el total cuadre al centavo con lo que se reembolsa en el reporte.

Uso:
    python3 hoja_gastos.py datos.json salida.xlsx [salida.pdf]

datos.json (ver assets/ejemplo_hoja.json):
{
  "titulo": "Nombre - Viaje - Travel Request XXXX / Expense Report YYYY",
  "aprobado_mi_usd": 300.00,                # opcional: M&I aprobado en la TR
  "dias": [
    {"fecha": "10th March", "ubicacion": "Rome", "tasa": 1.10,
     "desayuno": [6.50], "almuerzo": [18.00], "cena": [25, 3.5],
     "alojamiento": [], "imprevistos": [],
     "comentario_cena": "texto opcional que queda como comentario de la celda"}
  ],
  "otros": [
    {"descripcion": "Taxi home - airport", "fecha": "9th March",
     "moneda": "KES", "monto": 2000, "tasa": 0.0077}
  ],
  "notas": ["..."]
}
Los montos de "dias" van en la moneda local de ese día (la de "tasa"); el resultado es USD.
"""
import json
import sys

try:
    from openpyxl import Workbook
except ImportError:
    sys.exit("Falta openpyxl. Instálalo con: python3 -m pip install openpyxl")

from openpyxl.comments import Comment
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side

ARIAL = "Arial"
AZUL = "0000FF"
USD_FMT = '_(* #,##0.00_);_(* \\(#,##0.00\\);_(* "-"??_);_(@_)'
CATS = [("B", "desayuno", "Breakfast"), ("C", "almuerzo", " Lunch"), ("D", "cena", " Dinner")]


def f(bold=False, color=None, size=10):
    return Font(name=ARIAL, bold=bold, color=color, size=size)


def r2(x):
    # Redondeo "half up" como Concur, evitando el redondeo bancario de Python.
    return float(f"{x + 1e-9:.2f}") if x >= 0 else -float(f"{-x + 1e-9:.2f}")


def formula(montos, fila):
    if not montos:
        return None
    return "=" + "+".join(f"ROUND({m}*$J{fila},2)" for m in montos)


def valor(montos, tasa):
    return round(sum(r2(m * tasa) for m in montos), 2)


def construir(datos, ruta_xlsx):
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"
    borde = Border(*(Side(style="thin", color="999999"),) * 4)

    ws["A1"] = datos.get("titulo", "")
    ws["A1"].font = f(True, size=11)

    ws.merge_cells("A2:H2")
    ws["A2"] = "PERDIEM"
    ws["A2"].font = f(True)
    cab = ["Date", "Breakfast", " Lunch", " Dinner", "Meals", "Room allowance",
           " Incidentals", "Total per diem", "Location", "Exchange rate to USD (Concur)"]
    for i, h in enumerate(cab):
        c = ws.cell(row=3, column=i + 1, value=h)
        c.font = f(True)
        c.border = borde
        c.alignment = Alignment(horizontal="center", wrap_text=True)
    for col in "BCDEFGH":
        ws[f"{col}4"] = "USD"
        ws[f"{col}4"].font = f(True)
        ws[f"{col}4"].alignment = Alignment(horizontal="center")

    calc = {"dias": [], "per_diem": 0.0, "otros": [], "otros_total": 0.0}
    fila = 5
    for d in datos["dias"]:
        tasa = d["tasa"]
        ws[f"A{fila}"] = d["fecha"]
        fila_calc = {"fecha": d["fecha"], "ubicacion": d.get("ubicacion", ""), "tasa": tasa}
        for col, clave, _ in CATS:
            m = d.get(clave, [])
            if m:
                ws[f"{col}{fila}"] = formula(m, fila)
            fila_calc[clave] = valor(m, tasa)
            com = d.get(f"comentario_{clave}")
            if com:
                ws[f"{col}{fila}"].comment = Comment(com, "Claude")
        ws[f"E{fila}"] = f"=SUM(B{fila}:D{fila})"
        aloj, imp = d.get("alojamiento", []), d.get("imprevistos", [])
        if aloj:
            ws[f"F{fila}"] = formula(aloj, fila)
        if imp:
            ws[f"G{fila}"] = formula(imp, fila)
            if d.get("comentario_imprevistos"):
                ws[f"G{fila}"].comment = Comment(d["comentario_imprevistos"], "Claude")
        fila_calc["alojamiento"] = valor(aloj, tasa)
        fila_calc["imprevistos"] = valor(imp, tasa)
        fila_calc["comidas"] = round(fila_calc["desayuno"] + fila_calc["almuerzo"] + fila_calc["cena"], 2)
        fila_calc["total"] = round(fila_calc["comidas"] + fila_calc["alojamiento"] + fila_calc["imprevistos"], 2)
        calc["dias"].append(fila_calc)
        calc["per_diem"] = round(calc["per_diem"] + fila_calc["total"], 2)
        ws[f"H{fila}"] = f"=SUM(E{fila}:G{fila})"
        ws[f"I{fila}"] = d.get("ubicacion", "")
        ws[f"J{fila}"] = tasa
        ws[f"J{fila}"].font = f(color=AZUL)
        ws[f"J{fila}"].number_format = "0.0000"
        for col in "BCDEFGH":
            ws[f"{col}{fila}"].number_format = "0.00"
        fila += 1
    ult = fila - 1
    s_pd = fila
    ws[f"G{s_pd}"] = "Sum"
    ws[f"G{s_pd}"].font = f(True)
    ws[f"H{s_pd}"] = f"=SUM(H5:H{ult})"
    ws[f"H{s_pd}"].font = f(True)
    ws[f"H{s_pd}"].number_format = USD_FMT
    if datos.get("aprobado_mi_usd") is not None:
        ws[f"G{s_pd + 1}"] = "Approved in TR"
        ws[f"H{s_pd + 1}"] = datos["aprobado_mi_usd"]
        ws[f"H{s_pd + 1}"].font = f(color=AZUL)
        ws[f"H{s_pd + 1}"].number_format = USD_FMT
        ws[f"I{s_pd + 1}"] = "Meals and incidentals approved in the Travel Request (USD)"

    oe = s_pd + 3
    ws.merge_cells(f"A{oe}:H{oe}")
    ws[f"A{oe}"] = "Other expenses"
    ws[f"A{oe}"].font = f(True)
    for col, h in zip("ABCDGH", ["Descrition", "Date", "Currency", "Amount", "Exchange rate", "Amount in USD"]):
        c = ws[f"{col}{oe + 1}"]
        c.value = h
        c.font = f(True)
        c.border = borde
    fila = oe + 2
    primera = fila
    for o in datos.get("otros", []):
        ws[f"A{fila}"] = o["descripcion"]
        ws[f"B{fila}"] = o["fecha"]
        ws[f"C{fila}"] = o["moneda"]
        ws[f"D{fila}"] = o["monto"]
        ws[f"D{fila}"].font = f(color=AZUL)
        ws[f"D{fila}"].number_format = USD_FMT
        ws[f"G{fila}"] = o["tasa"]
        ws[f"G{fila}"].font = f(color=AZUL)
        ws[f"G{fila}"].number_format = "0.0000000"
        ws[f"H{fila}"] = f"=ROUND(D{fila}*G{fila},2)"
        ws[f"H{fila}"].number_format = "0.00"
        usd = r2(o["monto"] * o["tasa"])
        calc["otros"].append({**o, "usd": usd})
        calc["otros_total"] = round(calc["otros_total"] + usd, 2)
        fila += 1
    s_o = fila + 1
    ws[f"G{s_o}"] = "Sum"
    ws[f"G{s_o}"].font = f(True)
    ws[f"H{s_o}"] = f"=SUM(H{primera}:H{max(primera, fila - 1)})"
    ws[f"H{s_o}"].font = f(True)
    ws[f"H{s_o}"].number_format = USD_FMT

    tot = s_o + 2
    ws[f"A{tot}"] = "Overall Total "
    ws[f"A{tot}"].font = f(True)
    ws[f"H{tot}"] = f"=H{s_o}+H{s_pd}"
    ws[f"H{tot}"].font = f(True)
    ws[f"H{tot}"].number_format = USD_FMT
    ws[f"H{tot}"].fill = PatternFill("solid", fgColor="F2F2F2")
    calc["total"] = round(calc["per_diem"] + calc["otros_total"], 2)

    n = tot + 2
    ws[f"A{n}"] = "Notes"
    ws[f"A{n}"].font = f(True)
    for i, t in enumerate(datos.get("notas", []), start=1):
        ws[f"A{n + i}"] = t
        ws[f"A{n + i}"].font = f()

    for k, v in {"A": 34, "B": 14, "C": 14, "D": 14, "E": 12, "F": 15, "G": 14, "H": 17, "I": 34, "J": 16}.items():
        ws.column_dimensions[k].width = v
    for fila_c in ws.iter_rows():
        for c in fila_c:
            if c.font and c.font.name != ARIAL:
                c.font = Font(name=ARIAL, bold=c.font.b, color=c.font.color, size=c.font.sz or 10)
    ws.row_dimensions[3].height = 30
    ws.freeze_panes = "A5"
    wb.save(ruta_xlsx)
    return calc


def pdf(datos, calc, ruta_pdf):
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

    def m(x):
        return f"{x:,.2f}" if x else ""

    ss = getSampleStyleSheet()
    chico = ss["Normal"]
    chico.fontName = "Helvetica"
    chico.fontSize = 8
    el = [Paragraph(datos.get("titulo", ""), ss["Heading3"]), Paragraph("PERDIEM", ss["Heading4"])]
    t = [["Date", "Breakfast", "Lunch", "Dinner", "Meals", "Room allowance", "Incidentals",
          "Total per diem", "Location", "Rate to USD (Concur)"], [""] + ["USD"] * 7 + ["", ""]]
    for d in calc["dias"]:
        t.append([d["fecha"], m(d["desayuno"]), m(d["almuerzo"]), m(d["cena"]), m(d["comidas"]),
                  m(d["alojamiento"]), m(d["imprevistos"]), m(d["total"]), d["ubicacion"], f"{d['tasa']:.4f}"])
    t.append(["", "", "", "", "", "", "Sum", f"{calc['per_diem']:,.2f}", "", ""])
    if datos.get("aprobado_mi_usd") is not None:
        t.append(["", "", "", "", "", "", "Approved in TR", f"{datos['aprobado_mi_usd']:,.2f}",
                  "M&I approved in the Travel Request (USD)", ""])
    n_sum = 2 + len(calc["dias"])
    tb = Table(t, repeatRows=1)
    tb.setStyle(TableStyle([("FONT", (0, 0), (-1, -1), "Helvetica", 7.5), ("FONT", (0, 0), (-1, 1), "Helvetica-Bold", 7.5),
                            ("GRID", (0, 0), (-1, n_sum), 0.3, colors.grey), ("ALIGN", (1, 2), (7, -1), "RIGHT"),
                            ("FONT", (6, n_sum), (7, n_sum), "Helvetica-Bold", 7.5)]))
    el += [tb, Spacer(1, 10), Paragraph("Other expenses", ss["Heading4"])]
    o = [["Description", "Date", "Currency", "Amount", "Exchange rate", "Amount in USD"]]
    for x in calc["otros"]:
        o.append([x["descripcion"], x["fecha"], x["moneda"], f"{x['monto']:,.2f}", f"{x['tasa']:.7f}", f"{x['usd']:,.2f}"])
    o.append(["", "", "", "", "Sum", f"{calc['otros_total']:,.2f}"])
    k = len(o) - 1
    t2 = Table(o)
    t2.setStyle(TableStyle([("FONT", (0, 0), (-1, -1), "Helvetica", 7.5), ("FONT", (0, 0), (-1, 0), "Helvetica-Bold", 7.5),
                            ("GRID", (0, 0), (-1, k - 1), 0.3, colors.grey), ("ALIGN", (3, 1), (-1, -1), "RIGHT"),
                            ("FONT", (4, k), (5, k), "Helvetica-Bold", 7.5)]))
    el += [t2, Spacer(1, 8)]
    t3 = Table([["Overall Total (USD, reimbursable to traveler)", f"{calc['total']:,.2f}"]])
    t3.setStyle(TableStyle([("FONT", (0, 0), (-1, -1), "Helvetica-Bold", 9), ("BOX", (0, 0), (-1, -1), 0.5, colors.black)]))
    el += [t3, Spacer(1, 8)]
    if datos.get("notas"):
        el.append(Paragraph("<b>Notes</b>", chico))
        el += [Paragraph("• " + n, chico) for n in datos["notas"]]
    SimpleDocTemplate(ruta_pdf, pagesize=landscape(A4), leftMargin=24, rightMargin=24,
                      topMargin=24, bottomMargin=24).build(el)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    with open(sys.argv[1], encoding="utf-8") as fh:
        datos = json.load(fh)
    calc = construir(datos, sys.argv[2])
    if len(sys.argv) > 3:
        try:
            pdf(datos, calc, sys.argv[3])
        except ImportError:
            print("AVISO: falta reportlab, no se generó el PDF. Instálalo con "
                  "'python3 -m pip install reportlab' o abre el Excel y expórtalo como PDF.",
                  file=sys.stderr)
    print(json.dumps({"per_diem_usd": calc["per_diem"], "otros_usd": calc["otros_total"],
                      "total_usd": calc["total"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
