"""
SCFV Motor 9.0.0 — Reportes desde EventStore.

Módulo EventStore-only. No lee proyecciones legacy (negocio_*).
Genera archivos en libros/ y devuelve la ruta como string.

Funciones puras. Sin prints a stdout (la TUI controla el output).
"""
import csv
import calendar
import json
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Dict


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------

def _timestamp_rango(periodo_id: str):
    """periodo_id = 'YYYY-MM' -> (inicio_unix, fin_unix)."""
    año, mes = map(int, periodo_id.split("-"))
    inicio = int(datetime(año, mes, 1).timestamp())
    ultimo_dia = calendar.monthrange(año, mes)[1]
    fin = int(datetime(año, mes, ultimo_dia, 23, 59, 59).timestamp())
    return inicio, fin


def _leer_asientos(db_path: str, periodo_id: str):
    """Devuelve lista de payloads dict de ASIENTO_REGISTRADO del período."""
    inicio, fin = _timestamp_rango(periodo_id)
    conn = sqlite3.connect(db_path)
    try:
        cur = conn.cursor()
        cur.execute("""
            SELECT payload FROM event_store
            WHERE tipo_evento = 'ASIENTO_REGISTRADO'
              AND timestamp >= ? AND timestamp <= ?
            ORDER BY timestamp ASC
        """, (inicio, fin))
        filas = cur.fetchall()
    finally:
        conn.close()

    asientos = []
    for (payload_str,) in filas:
        try:
            payload = json.loads(payload_str) if isinstance(payload_str, str) else payload_str
            if isinstance(payload, dict):
                asientos.append(payload)
        except (json.JSONDecodeError, TypeError):
            continue
    return asientos


def _saldos_mayor(asientos):
    """Agrega DEBE (+) y HABER (-) por cuenta."""
    saldos: Dict[str, float] = {}
    for a in asientos:
        for p in a.get("partidas", []):
            cuenta = p.get("cuenta_codigo", "?")
            monto = float(p.get("monto", 0))
            signo = +1 if p.get("ubicacion") == "DEBE" else -1
            saldos[cuenta] = saldos.get(cuenta, 0.0) + signo * monto
    return saldos


def _directorio_salida():
    d = Path("libros")
    d.mkdir(exist_ok=True)
    return d


# ----------------------------------------------------------------------
# API pública
# ----------------------------------------------------------------------

def generar_csv_diario(db_path: str, periodo_id: str) -> str:
    asientos = _leer_asientos(db_path, periodo_id)
    archivo = _directorio_salida() / f"motor_diario_{periodo_id}.csv"
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Asiento ID", "Fecha", "Período", "Total Debe", "Total Haber", "Correlation ID"])
        for a in asientos:
            w.writerow([
                a.get("id", ""),
                a.get("fecha", ""),
                a.get("periodo_id", ""),
                a.get("total_debe", 0),
                a.get("total_haber", 0),
                a.get("correlation_id", ""),
            ])
    return str(archivo)


def generar_csv_mayor(db_path: str, periodo_id: str) -> str:
    saldos = _saldos_mayor(_leer_asientos(db_path, periodo_id))
    archivo = _directorio_salida() / f"motor_mayor_{periodo_id}.csv"
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Cuenta", "Saldo"])
        for cuenta in sorted(saldos.keys()):
            w.writerow([cuenta, saldos[cuenta]])
    return str(archivo)


def generar_csv_balance(db_path: str, periodo_id: str) -> str:
    saldos = _saldos_mayor(_leer_asientos(db_path, periodo_id))
    activo = pasivo = capital = 0.0
    for cuenta, saldo in saldos.items():
        if cuenta.startswith("1"):
            activo += saldo
        elif cuenta.startswith("2"):
            pasivo += saldo
        elif cuenta.startswith("3"):
            capital += saldo
        elif cuenta.startswith("4"):
            capital += saldo
        elif cuenta.startswith("5"):
            capital += saldo

    archivo = _directorio_salida() / f"motor_balance_{periodo_id}.csv"
    with open(archivo, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["Rubro", "Saldo"])
        w.writerow(["ACTIVO", activo])
        w.writerow(["PASIVO", pasivo])
        w.writerow(["CAPITAL", capital])
        w.writerow(["TOTAL ACTIVO", activo])
        w.writerow(["TOTAL PASIVO + CAPITAL", pasivo + capital])
    return str(archivo)


def generar_pdf_diario(db_path: str, periodo_id: str) -> str:
    try:
        from fpdf import FPDF
    except ImportError:
        raise RuntimeError("fpdf no instalado. Ejecutar: pip install fpdf")

    asientos = _leer_asientos(db_path, periodo_id)
    archivo = _directorio_salida() / f"motor_diario_{periodo_id}.pdf"
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.cell(200, 10, txt=f"Libro Diario - {periodo_id}", ln=True, align="C")
    pdf.ln(5)
    pdf.cell(60, 8, "Asiento ID", 1)
    pdf.cell(30, 8, "Fecha", 1)
    pdf.cell(35, 8, "Total Debe", 1)
    pdf.cell(35, 8, "Total Haber", 1)
    pdf.ln()
    for a in asientos:
        pdf.cell(60, 6, str(a.get("id", ""))[:20], 1)
        pdf.cell(30, 6, str(a.get("fecha", "")), 1)
        pdf.cell(35, 6, str(a.get("total_debe", 0)), 1)
        pdf.cell(35, 6, str(a.get("total_haber", 0)), 1)
        pdf.ln()
    pdf.output(str(archivo))
    return str(archivo)
