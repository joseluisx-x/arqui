import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_obtener_alumnos_matriculados():
    """Valida la consulta de alumnos por curso según el contrato OpenAPI."""
    response = client.get("/api/v1/alumnos-matriculados?curso=comunicacion")
    assert response.status_code == 200
    data = response.json()
    assert data["curso"] == "comunicacion"
    assert data["total_encontrados"] == 2
    assert len(data["alumnos"]) == 2
    assert data["alumnos"][0]["nombre"] == "Ana Pérez"

def test_registrar_pago_caja():
    """Valida el registro de pago en caja según el contrato OpenAPI."""
    payload = {
        "alumno_id": 1,
        "monto": 150.50,
        "concepto": "Matricula 2026-I"
    }
    response = client.post("/api/v1/caja/pagos", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["mensaje"] == "Pago registrado exitosamente en caja"
    assert data["data"]["alumno_id"] == 1
    assert data["data"]["monto"] == 150.50
    assert data["data"]["estado"] == "registrado"
