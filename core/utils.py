# utils.py

from io import BytesIO
from reportlab.pdfgen import canvas

def export_cv_to_pdf(user, cv_data):
    # Criar um buffer de memória para armazenar o PDF
    buffer = BytesIO()

    # Criar um objeto de canvas que vai desenhar o PDF
    c = canvas.Canvas(buffer)

    # Definir título do currículo
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, f"Currículo de {user.username}")

    # Adicionar experiência profissional
    c.drawString(100, 780, "Experiência Profissional:")
    y_position = 760
    for experience in cv_data['experience']:
        c.drawString(100, y_position, experience)
        y_position -= 20

    # Adicionar formação acadêmica
    c.drawString(100, y_position, "Formação Acadêmica:")
    y_position -= 20
    for education in cv_data['education']:
        c.drawString(100, y_position, education)
        y_position -= 20

    # Adicionar habilidades
    c.drawString(100, y_position, "Habilidades:")
    y_position -= 20
    for skill in cv_data['skills']:
        c.drawString(100, y_position, skill)
        y_position -= 20

    # Finalizar o PDF
    c.showPage()
    c.save()

    # Voltar para o início do buffer
    buffer.seek(0)
    return buffer
