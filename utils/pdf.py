from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def export_pdf(student, score, total):
    file = "result.pdf"
    c = canvas.Canvas(file, pagesize=letter)

    c.drawString(100, 750, "ORO EXAM RESULT")
    c.drawString(100, 700, f"Student: {student}")
    c.drawString(100, 680, f"Score: {score}/{total}")

    c.save()

    return file