from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def generate_result_pdf(student_name, score, total):

    file_name = f"{student_name}_result.pdf"

    c = canvas.Canvas(file_name, pagesize=letter)

    c.setFont("Helvetica-Bold", 20)
    c.drawString(180, 750, "ORO EXAM RESULT")

    c.setFont("Helvetica", 14)
    c.drawString(100, 700, f"Student Name: {student_name}")
    c.drawString(100, 670, f"Score: {score} / {total}")
    c.drawString(100, 640, f"Percentage: {round((score/total)*100, 2)} %")

    if score >= total * 0.5:
        status = "PASS"
    else:
        status = "FAIL"

    c.drawString(100, 610, f"Status: {status}")

    c.save()

    return file_name