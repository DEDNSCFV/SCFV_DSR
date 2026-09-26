# SCFV_DSR

Artefacto Design Science Research del Programa de Investigación SCFV.

## Instalación

    git clone <repo> SCFV_DSR
    cd SCFV_DSR
    pip install -e .

## Uso

    # Inicializa base local en ~/SCFV_DSR/var/scfv.db
    python -m scfv_dsr.cli init

    # Lista fractales disponibles
    python -m scfv_dsr.cli list

    # Ejecuta un fractal sobre una evidencia
    python -m scfv_dsr.cli run --fractal INVENTARIOS --marco NIIF_PYMES \
        --evidencia-json '{"activo_es_inventario":true,"monto":850,"costo":1000,"precio_venta":900,"costos_terminacion_venta":50}'

    # Lista eventos registrados
    python -m scfv_dsr.cli saldos

## Estructura

    scfv_dsr/
    ├── kernel/         baldor.py + xnor.py + JSON de operaciones/cuentas/categorías/puente
    ├── epistemologico/ Perceptum, Intellectus, Dictum, generador de propuesta
    ├── contable/       Motor, EventStore, Núcleo, puentes
    ├── profesional/    H2, Orquestador v8.2
    ├── dsl/            Grammar y parser ADL-SCFV
    ├── fractales/      Fractales NIC / Pymes
    ├── evaluador.py    Activación de reglas por marco
    ├── extractor.py    Evento → Evidencia → dict del fractal
    ├── integrador.py   Pipeline completo: fractal → SCFV → EventStore
    └── cli.py          Punto de entrada

## Requisitos

- Python >= 3.10
- lark >= 1.0
- sqlite3 (incluido en Python)

## Autocontenido

El paquete no depende del corpus S0 (`scfv_v6`). Es portable.
