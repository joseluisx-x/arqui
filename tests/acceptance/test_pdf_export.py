import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_generar_pdf_alumnos_exitoso():
    """Valida la generación de PDF según FEAT-002 y el contrato OpenAPI."""
    response = client.get("/api/v1/alumnos-matriculados/pdf?curso=comunicacion")
    
    # 1. Código de estado
    assert response.status_code == 200
    
    # 2. Content-Type binario
    assert response.headers["content-type"] == "application/pdf"
    
    # 3. Disposición de descarga con nombre de archivo
    assert 'attachment; filename="reporte_alumnos_comunicacion.pdf"' in response.headers["content-disposition"]
    
    # 4. Firma válida de archivo PDF (%PDF)
    assert response.content.startswith(b"%PDF")

def test_generar_pdf_curso_sin_alumnos():
    """Valida que genera un PDF válido incluso cuando un curso no tiene alumnos."""
    response = client.get("/api/v1/alumnos-matriculados/pdf?curso=quimica")
    
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/pdf"
    assert response.content.startswith(b"%PDF")
