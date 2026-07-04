from reportlab.pdfgen import canvas


def generate_result_pdf(student, score, total):

    file = f"{student}_result.pdf"

    c = canvas.Canvas(file)

    c.drawString(200, 800, "ORO EXAM RESULT")

    c.drawString(100, 750, f"Student: {student}")
    c.drawString(100, 730, f"Score: {score}/{total}")

    percent = (score / total) * 100
    c.drawString(100, 710, f"Percentage: {percent}%")

    status = "PASS" if score >= total/2 else "FAIL"
    c.drawString(100, 690, f"Status: {status}")

    c.save()

    return file