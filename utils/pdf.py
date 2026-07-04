from reportlab.pdfgen import canvas


def generate_result_pdf(student, score, total):

    file = f"{student}_result.pdf"

    c = canvas.Canvas(file)

    c.drawString(100, 750, "ORO EXAM RESULT")
    c.drawString(100, 700, f"Student: {student}")
    c.drawString(100, 680, f"Score: {score}/{total}")

    percent = (score / total) * 100
    c.drawString(100, 660, f"Percentage: {percent}%")

    c.save()

    return file