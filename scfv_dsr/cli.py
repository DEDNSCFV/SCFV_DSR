"""CLI del SCFV_DSR. Uso:

    python -m scfv_dsr.cli init
    python -m scfv_dsr.cli run --fractal INVENTARIOS --marco NIIF_PYMES --evidencia ev.json
    python -m scfv_dsr.cli list
    python -m scfv_dsr.cli saldos
"""
import argparse
import json
import os
import sqlite3
import sys
from pathlib import Path

DSR_HOME = Path(__file__).resolve().parent.parent
VAR = DSR_HOME / 'var'
DB_DEFAULT = VAR / 'scfv.db'


def cmd_init(args):
    VAR.mkdir(parents=True, exist_ok=True)
    from scfv_dsr.contable.event_store import EventStore
    store = EventStore(str(DB_DEFAULT))
    store.cerrar()
    print(f"✓ Inicializado: {DB_DEFAULT}")
    print(f"✓ Directorio: {VAR}")


def cmd_list(args):
    fr_dir = DSR_HOME / 'scfv_dsr' / 'fractales'
    for f in sorted(fr_dir.glob('*.scfv')):
        print(f"  {f.name}")


def cmd_run(args):
    from scfv_dsr.integrador import ejecutar_fractal_en_pipeline
    fr_path = DSR_HOME / 'scfv_dsr' / 'fractales' / f"{args.fractal}.scfv"
    if not fr_path.exists():
        print(f"Fractal no encontrado: {fr_path}")
        sys.exit(1)
    if args.evidencia:
        ev = json.load(open(args.evidencia))
    else:
        ev = json.loads(args.evidencia_json)
    db = args.db or str(DB_DEFAULT)
    r = ejecutar_fractal_en_pipeline(
        fractal_path=str(fr_path),
        marco=args.marco,
        evidencia=ev,
        justificacion=args.justificacion or 'Sin justificación',
        db_path=db,
    )
    a = r['resultado_s0']['asiento']
    print(f"Asiento: {a['id']}")
    print(f"  D={a['total_debe']}  H={a['total_haber']}  partidas={len(a['partidas'])}")
    print(f"  Cadena: {r['cadena_integra']}")


def cmd_saldos(args):
    if not DB_DEFAULT.exists():
        print(f"DB no existe: {DB_DEFAULT}")
        sys.exit(1)
    conn = sqlite3.connect(str(DB_DEFAULT))
    conn.row_factory = sqlite3.Row
    rows = conn.execute("SELECT id, tipo_evento, correlation_id FROM event_store").fetchall()
    print(f"Eventos: {len(rows)}")
    for r in rows:
        print(f"  id={r['id']} {r['tipo_evento']} corr={r['correlation_id'][:8]}")
    conn.close()


def main():
    parser = argparse.ArgumentParser(prog='scfv_dsr')
    sub = parser.add_subparsers(dest='cmd')

    p_init = sub.add_parser('init', help='Inicializa base de datos local')
    p_init.set_defaults(func=cmd_init)

    p_list = sub.add_parser('list', help='Lista fractales disponibles')
    p_list.set_defaults(func=cmd_list)

    p_run = sub.add_parser('run', help='Ejecuta un fractal')
    p_run.add_argument('--fractal', required=True)
    p_run.add_argument('--marco', default='NIIF_PYMES')
    p_run.add_argument('--evidencia', help='Path a JSON de evidencia')
    p_run.add_argument('--evidencia-json', help='Evidencia como string JSON')
    p_run.add_argument('--justificacion', default=None)
    p_run.add_argument('--db', default=None)
    p_run.set_defaults(func=cmd_run)

    p_saldos = sub.add_parser('saldos', help='Lista eventos registrados')
    p_saldos.set_defaults(func=cmd_saldos)

    args = parser.parse_args()
    if not hasattr(args, 'func'):
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == '__main__':
    main()
