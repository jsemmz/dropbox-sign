from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from reportlab.pdfbase.ttfonts import TTFont 

pdf = canvas.Canvas('example.pdf')
pdf.setTitle('Examples of Pdfs')

pdf.setFont("Helvetica", 24)
pdf.drawString(20, 400, "Examples Of")
pdf.drawString(40, 360, "PDFs")

pdf.setFont("Courier", 16)
pdf.drawString(60, 300, "Another PDF Line")

text = pdf.beginText(40, 680)
text.setFont('Courier', 18)
text.setFillColor(colors.red)

lines = ['Report Lab is a great', 'python library for pdfs']

for line in lines:
    text.textLine(line)

pdf.drawText(text)

pdf.save()