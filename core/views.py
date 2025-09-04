# core/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def home(request):
    return render(request, 'core/home.html')

def dashboard(request):
    return render(request, 'core/dashboard.html')

def planos(request):  # ← CORRIGIDO: mudado de "planes" para "planos"
    return render(request, 'core/planos.html')

@login_required
def exportar_cv(request):
    # Criar um buffer para o PDF
    buffer = BytesIO()

    # Criar o canvas do PDF
    p = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter

    # Adicionar conteúdo ao PDF
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, height - 100, f"Currículo de {request.user.first_name} {request.user.last_name}")

    p.setFont("Helvetica", 12)
    y_position = height - 130

    # Informações pessoais
    p.drawString(100, y_position, f"Email: {request.user.email}")
    y_position -= 30

    # Título da seção de experiência
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, y_position, "Experiência Profissional")
    y_position -= 25
    p.setFont("Helvetica", 12)

    # Experiência profissional (exemplo)
    experiencias = [
        "Desenvolvedor Python - Empresa XYZ (2020-2023)",
        "Analista de Sistemas - Empresa ABC (2018-2020)"
    ]

    for exp in experiencias:
        p.drawString(120, y_position, f"• {exp}")
        y_position -= 20

    # Título da seção de educação
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, y_position, "Formação Acadêmica")
    y_position -= 25
    p.setFont("Helvetica", 12)

    # Educação (exemplo)
    educacoes = [
        "Bacharelado em Ciência da Computação - Universidade Exemplo",
        "Certificação em Django Framework"
    ]

    for edu in educacoes:
        p.drawString(120, y_position, f"• {edu}")
        y_position -= 20

    # Título da seção de habilidades
    p.setFont("Helvetica-Bold", 14)
    p.drawString(100, y_position, "Habilidades")
    y_position -= 25
    p.setFont("Helvetica", 12)

    # Habilidades (exemplo)
    habilidades = [
        "Python", "Django", "JavaScript", "HTML/CSS", "SQL"
    ]

    for skill in habilidades:
        p.drawString(120, y_position, f"• {skill}")
        y_position -= 20

    p.save()

    # Criar resposta HTTP
    buffer.seek(0)
    response = HttpResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="curriculo_{request.user.username}.pdf"'

    return response