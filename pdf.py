from fpdf import FPDF

pdf = FPDF(
    orientation='P',
    unit='pt',
    format='A4'
)

pdf.add_page()

pdf.set_font(family='Arial', size=24, style='B')
pdf.cell(w=0, h=50, txt="Flatmates Bill", border=1, align='C', ln=1)
pdf.cell(w=100, h=40, txt="Period:", border=1)
pdf.cell(w=150, h=40, txt="March 2021", border=1)

pdf.output("deleteme.pdf")