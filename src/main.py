from fastapi import FastAPI, Query, status
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

try:
    from src.database import DB_ALUMNOS, DB_PAGOS
    from src.services.pdf_generator import generar_pdf_alumnos
except ImportError:
    try:
        from database import DB_ALUMNOS, DB_PAGOS
        from services.pdf_generator import generar_pdf_alumnos
    except ImportError:
        from tests.mocks.mock_db import DB_ALUMNOS, DB_PAGOS
        from services.pdf_generator import generar_pdf_alumnos

# Inicialización de la aplicación (cumpliendo el contrato OpenAPI)
app = FastAPI(
    title="SIGA-U Mini API",
    version="1.0.0",
    description="Implementación Spec-First para Matrículas y Caja"
)

# Esquema de validación para los pagos (DTO)
class PagoCreate(BaseModel):
    alumno_id: int
    monto: float
    concepto: str

# 1. Endpoint: Obtener alumnos matriculados por curso
@app.get("/api/v1/alumnos-matriculados")
def obtener_alumnos_matriculados(curso: str = Query(..., description="Nombre del curso")):
    # Consulta simulada sobre el ORM estático
    resultados = [a for a in DB_ALUMNOS if a["curso"].lower() == curso.lower()]
    return {
        "curso": curso,
        "total_encontrados": len(resultados),
        "alumnos": resultados
    }

# 2. Endpoint: Generar reporte en PDF de alumnos matriculados
@app.get("/api/v1/alumnos-matriculados/pdf")
def obtener_alumnos_matriculados_pdf(curso: str = Query(..., description="Nombre del curso")):
    # Consulta simulada sobre el ORM estático
    alumnos = [a for a in DB_ALUMNOS if a["curso"].lower() == curso.lower()]
    pdf_buffer = generar_pdf_alumnos(curso=curso, alumnos=alumnos)
    
    filename = f"reporte_alumnos_{curso.lower().replace(' ', '_')}.pdf"
    headers = {
        "Content-Disposition": f'attachment; filename="{filename}"'
    }
    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers=headers
    )

# 3. Endpoint: Registrar pagos en caja
@app.post("/api/v1/caja/pagos", status_code=status.HTTP_201_CREATED)
def registrar_pago_caja(pago: PagoCreate):
    # Simulación de inserción en base de datos estática
    nuevo_id_pago = len(DB_PAGOS) + 1
    registro_guardado = {
        "pago_id": nuevo_id_pago,
        "alumno_id": pago.alumno_id,
        "monto": pago.monto,
        "concepto": pago.concepto,
        "estado": "registrado"
    }
    DB_PAGOS.append(registro_guardado)

    return {
        "mensaje": "Pago registrado exitosamente en caja",
        "data": registro_guardado
    }

