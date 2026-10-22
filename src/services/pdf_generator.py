import io
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generar_pdf_alumnos(curso: str, alumnos: list[dict]) -> io.BytesIO:
    """Genera un archivo PDF con la lista de alumnos matriculados."""
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    elements = []
    styles = getSampleStyleSheet()

    # Título principal
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#1E3A8A'),
        alignment=1,  # Centrado
        spaceAfter=8
    )
    elements.append(Paragraph("SIGA-U - Reporte Oficial de Matrícula", title_style))

    # Metadatos del reporte
    meta_style = ParagraphStyle(
        'DocMeta',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#4B5563'),
        alignment=1,
        spaceAfter=15
    )
    fecha_str = datetime.now().strftime("%d/%m/%Y %H:%M")
    elements.append(Paragraph(
        f"<b>Curso:</b> {curso.upper()} &nbsp;&nbsp;|&nbsp;&nbsp; <b>Fecha de Emisión:</b> {fecha_str} &nbsp;&nbsp;|&nbsp;&nbsp; <b>Total:</b> {len(alumnos)}",
        meta_style
    ))
    elements.append(Spacer(1, 10))

    # Tabla de alumnos
    table_data = [["#", "ID", "Nombre del Estudiante", "Curso"]]
    if alumnos:
        for idx, alumno in enumerate(alumnos, start=1):
            table_data.append([
                str(idx),
                str(alumno.get("id", "")),
                alumno.get("nombre", ""),
                str(alumno.get("curso", "")).capitalize()
            ])
    else:
        table_data.append(["-", "-", "No hay alumnos matriculados en este curso", "-"])

    t = Table(table_data, colWidths=[30, 60, 300, 140])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1E3A8A')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (0, 0), (1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 7),
        ('TOPPADDING', (0, 0), (-1, 0), 7),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#D1D5DB')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#F9FAFB')]),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 6),
        ('TOPPADDING', (0, 1), (-1, -1), 6),
    ]))
    elements.append(t)

    doc.build(elements)
    buffer.seek(0)
    return buffer
