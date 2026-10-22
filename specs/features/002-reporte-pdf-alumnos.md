# Feature Specification: Generación de Reporte PDF de Alumnos Matriculados

- **ID**: `FEAT-002`
- **Status**: `Approved`
- **Owner / Author**: Core Team
- **Target Release / Milestone**: `v1.1.0`
- **Created**: 2026-10-15
- **Last Updated**: 2026-10-15

---

## 1. Context & Problem Statement

Los coordinadores académicos y docentes requieren descargar e imprimir la lista oficial de alumnos matriculados por asignatura en formato PDF para el control de asistencia y actas físicas.

## 2. Goals & Non-Goals

### Goals
- [x] Generar un documento PDF dinámico a partir del listado de alumnos filtrado por curso.
- [x] Formatear el PDF con encabezado institucional, nombre del curso, fecha de emisión y tabla con columnas (N°, ID, Nombre del Alumno).
- [x] Retornar el archivo con cabeceras HTTP adecuadas (`Content-Type: application/pdf`, `Content-Disposition: attachment; filename=reporte_alumnos_{curso}.pdf`).

### Non-Goals
- Firma digital criptográfica de actas (diferida a una etapa posterior).
- Envío automatizado por correo electrónico.

## 3. User Stories & Scenarios

- **US-1**: Como docente/coordinador, quiero solicitar el reporte PDF indicando el curso para obtener un archivo listo para imprimir.
  - **Scenario 1.1 (Con alumnos)**: Cuando el curso tiene alumnos (ej. `comunicacion`), se genera un PDF con la lista de los matriculados.
  - **Scenario 1.2 (Sin alumnos)**: Cuando el curso no tiene alumnos registrados, se genera el PDF indicando que no hay registros matriculados.

## 4. Technical Contracts & Data Schemas

Referencia al contrato OpenAPI: [`specs/contracts/siga-u-api.yaml`](../contracts/siga-u-api.yaml#L18-L34)

- **Endpoint**: `GET /api/v1/alumnos-matriculados/pdf`
- **Query Params**: `curso` (string, obligatorio)
- **Response**: `200 OK`, `Content-Type: application/pdf`, Payload binario.

## 5. Acceptance Criteria (BDD)

```gherkin
Scenario: Generar PDF exitosamente para curso con alumnos
  Given existen alumnos matriculados en el curso "comunicacion"
  When el cliente realiza una petición GET a "/api/v1/alumnos-matriculados/pdf?curso=comunicacion"
  Then el código de respuesta HTTP debe ser 200
  And la cabecera "Content-Type" debe ser "application/pdf"
  And la cabecera "Content-Disposition" debe contener "reporte_alumnos_comunicacion.pdf"
  And el cuerpo de la respuesta debe comenzar con la firma de archivo PDF "%PDF"
```

## 6. Verification & Test Plan

- **Acceptance Test**: [`tests/acceptance/test_pdf_export.py`](../../tests/acceptance/test_pdf_export.py)
- **Criterio de éxito**: Respuesta binaria válida con contenido generado en memoria.
