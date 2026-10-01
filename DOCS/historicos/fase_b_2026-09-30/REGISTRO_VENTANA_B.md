═══════════════════════════════════════════════════════════════════
REGISTRO DE VENTANA · FASE B
═══════════════════════════════════════════════════════════════════

ESTATUTO:   bitácora de la ventana B
            NO es acta de cierre
            NO es v1.0
            NO cierra deudas
            NO autoriza intervención
            NO modifica SCFV_DSR · NO modifica M
            NO firma §20

FECHA:      2026-09-30 → 2026-10-01
VENTANA:    B
ORIGEN:     traspaso VENTANA_2026-09-30_CONSOLIDADO (A→B)
CIERRE:     no alcanzado
═══════════════════════════════════════════════════════════════════

PREAMBULO

  Este registro documenta qué se ejecutó durante la ventana B,
  con qué estatuto, y qué quedó pendiente. NO sustituye a los
  documentos de trabajo materializados (metodología v0.12 · plan
  v0.3). Es la capa que los sitúa en su genealogía.

  Regla: la ventana registra; el cierre materializa.

  Bloques ejecutados:   B1–B13 · B11.V
  Bloques materializados:
    Bloque 1 → FASE_B_METODOLOGIA_v0.12.md
    Bloque 2 → FASE_B_PLAN_VERIFICACIONES_v0.3.md
    Bloque 3 → este registro

═══════════════════════════════════════════════════════════════════
BLOQUE B1 · RECONCILIACIÓN ~330 vs 341/344
═══════════════════════════════════════════════════════════════════

  Método:     comparación bloque_M §10 vs consolidado §2.6
  Resultado:
    · 341 ↔ 344 reconciliado (Δ = +3 por criterio, no error)
    · ~330 sin fuente · elevado a D-META-1
  Elevaciones:  D-META-1
  Estatuto:     parcial · ~330 sin resolver

═══════════════════════════════════════════════════════════════════
BLOQUE B2 · "RESUELTA" EN C-β §0
═══════════════════════════════════════════════════════════════════

  Método:     grep de "resuelta/resueltas" en acta C-β
  Resultado:
    · "resueltas: 4" en §0 · sin estatuto · §7 usa verbos más débiles
    · No mapea a ningún estado de M §1
    · Bajo CC1 · no produce cierre
  Elevaciones:  D-META-2 · OBS-B2-1
  Estatuto:     cerrado como observación · no como cierre

═══════════════════════════════════════════════════════════════════
BLOQUE B3 · H8P §22.4
═══════════════════════════════════════════════════════════════════

  Método:     lectura H8P_IMPORTADOR_CONTRATO.md §22.4–§22.5
  Resultado:
    · §22.4 contiene 5 deudas
    · M registra solo 2 (D-IMP-01/02)
    · Omisión verificada
    · D.5 no estaba señalada por nadie
  Elevaciones:  D-META-3 · OBS-B3-1 · OBS-B3-2
  Estatuto:     cerrado · requiere decisión del Operador

═══════════════════════════════════════════════════════════════════
BLOQUE B4 · D-BB-14 ≡ D-C-50
═══════════════════════════════════════════════════════════════════

  Método:     cruce de locus de MotorContable(None) en 3 fuentes
  Resultado:
    · mismo objeto material · dos IDs en familias distintas
    · DC-1 pasa de "no verificada" a "verificada en ≥1 caso"
    · segundo duplicado potencial: D-C-54 ≡ D-B-4
  Elevaciones:  D-META-4 · OBS-B4-1
  Estatuto:     cerrado · pendiente decisión de deduplicación

═══════════════════════════════════════════════════════════════════
BLOQUE B5 · FAMILIA D-EPIST
═══════════════════════════════════════════════════════════════════

  Método:     rastreo de D-EPIST-1..7 en DSR y scfv_v6
  Resultado:
    · solo 4 IDs verificables (1, 2, 4, 5)
    · FASE 4 ausente · no materializable
    · D-EPIST no es familia del corpus · es prefijo heredado
  Elevaciones:  D-META-5 · OBS-B5-1 · OBS-B5-2
  Estatuto:     parcial · 3 IDs sin locus

═══════════════════════════════════════════════════════════════════
BLOQUE B6 · SIN TRAZABILIDAD M
═══════════════════════════════════════════════════════════════════

  Método:     verificación de "SIN ESTADO" y F-H
  Resultado:
    · "SIN ESTADO" no existe en M · invento del consolidado
    · 11 IDs listados como SIN ESTADO tienen estado en M
    · F-H = "sin locus en M" · no "sin locus"
    · _EA_MATRIZ documenta 6 deudas operativas sin entrada H-XXX
    · Discrepancia §15 B-bis: 14 vs 12
  Elevaciones:  D-META-6 · OBS-B6-1..4
  Estatuto:     cerrado

═══════════════════════════════════════════════════════════════════
BLOQUE B7 · F-Z · REPARACIÓN SIN DEUDA
═══════════════════════════════════════════════════════════════════

  Método:     git log + lectura de AUDITORIA_26-09
  Resultado:
    · F-Z materializada en commits 015d6d4 y abd746e
    · FASE 2.a repara código sin acta · FASE 2.b/2.c al revés
    · AUDITORIA_26-09 contiene 8 hallazgos · 4-7 documentales
    · Hallazgo 1 = D-C-26
  Elevaciones:  D-META-7 · OBS-B7-1..5
  Estatuto:     cerrado · requiere política retroactiva

═══════════════════════════════════════════════════════════════════
BLOQUE B8 · DC-9 · DC-14
═══════════════════════════════════════════════════════════════════

  Método:     verificar si DC-9/DC-14 están en M §0
  Resultado:
    · DC-9 y DC-14 sí están en M §12 y §14
    · M §0 subdeclara · 1 DC vs 5 DC
    · F21 confirmada con cifra exacta
    · git no es fuente paralela · es canal de M
  Elevaciones:  D-META-8 · OBS-B8-1
  Estatuto:     cerrado

═══════════════════════════════════════════════════════════════════
BLOQUE B9 · F-AD
═══════════════════════════════════════════════════════════════════

  Método:     rastreo de F-AD en 3 corpus · verificación de locus
  Resultado:
    · F-AD ≡ INFORME_FASE_4 §1 · C-1..C-4
    · C-4 ≡ D-CONV-4 (ya en M)
    · §7.3 del ACTO_6_0_CONV_CONVERGENCIA ≠ F-AD
    · 3 hipótesis retiradas en la búsqueda
  Elevaciones:  D-META-9 · OBS-B9-1..16
  Estatuto:     cerrado en B9 · restaurado tras v0.11 (F-B11-1)


═══════════════════════════════════════════════════════════════════
BLOQUE B10 · CLASIFICACIÓN C-INTERV · INTENTO
═══════════════════════════════════════════════════════════════════

  Método:     asignación TEC/DOC/NO-INT/META/DISCREP por familia
  Resultado:
    · partición inicial 350 entradas
    · errores detectados en B12:
        F-B10-1 · D-C-13 duplicado (retirada RB-4)
        F-B10-2 · D-C-32 reformulada (retirada RB-5)
        F-B10-3 · D-C 84 contables (retirada RB-6)
  Elevaciones:  —
  Estatuto:     cifras RETIRADAS · sustituidas por B11

═══════════════════════════════════════════════════════════════════
BLOQUE B11 · RECUENTO DESDE FUENTE
═══════════════════════════════════════════════════════════════════

  Método:     grep/awk por familia · sin interpretación intermedia
  Resultado:
    · 350 nominales (M §2/§5/§10)
    · 3 retiradas confirmadas
    · 2 duplicados por locus (D-B-4 ≡ D-C-54 · D-BB-14 ≡ D-C-50)
    · 1 cerrada documental (D-BB-58)
    · 0 cerradas verificadas en M (D-C-26 sólo en consolidado)
    · Residuo 349 vs 350 declarado
  Elevaciones:  —
  Estatuto:     cifras oficiales del substrato

═══════════════════════════════════════════════════════════════════
BLOQUE B11.V · VERIFICACIÓN DEL SUBSTRATO
═══════════════════════════════════════════════════════════════════

  Método:     lectura de partición M §10 · retiradas · reformuladas
  Resultado:
    · M §10: 341 + 5 + 3 + 1 = 350
    · CERRADA VERIFICADA no aparece en M
    · El consolidado la añade (D-C-26)
    · Bajo RT1 → D-C-26 ABIERTA
  Elevaciones:  D-META-10
  Estatuto:     cerrado · residuo resuelto por RT1

═══════════════════════════════════════════════════════════════════
BLOQUE B12 · REVISIÓN DE MÉTODO (RB-0)
═══════════════════════════════════════════════════════════════════

  Método:     análisis del patrón de errores de B
  Resultado:
    · 6 retiradas acumuladas · supera umbral RB-0 (5)
    · Patrón F-AH confirmado: B reproduce el vicio de A
    · Taxonomía de errores propios: E-B1..E-B5
    · 3 nuevas reglas: RB-4 · RB-5 · RB-6
    · Cifras de B10 retiradas · B11 las sustituye
  Elevaciones:  —
  Estatuto:     cerrado · reglas RB-4/5/6 añadidas

═══════════════════════════════════════════════════════════════════
BLOQUE B13 · CLASIFICACIÓN POR REPO
═══════════════════════════════════════════════════════════════════

  Método:     asignación de cada ID a R1..R6 por locus material
              (RB-1: no por mención del nombre)
  Sub-bloques:
    B13.1 · M1 + D-IMP + DM   37/37 · alta confianza
    B13.2 · D-B               26/26 · alta confianza
    B13.3 · D-BB              49/73 · parcial (24 media/baja)
    B13.4 · D-C               88/88 · alta confianza
    B13.5 · D-Calpha          78/126 · parcial (47 media/baja)

  Resultado:
    · 278 de 350 verificados con alta confianza (79.4%)
    · 72 pendientes (24 D-BB + 47 D-Calpha + 1 D-C)
    · 2 retiradas fuera de clasificación por repo
    · Distribución: R1 56 · R2 1 · R3 148 · R4 45 · R5 2 · R6 1
                    META 9 · MIX 14
  Elevaciones:  OBS-B13-1..4
  Estatuto:     cerrado con residuo declarado

  Hallazgo mayor:
    · M no es un catálogo mono-repo
    · 42% scfv-dsr · 16% scfv_v6 · 13% Programa · 20% sin clasificar
    · "cuerpo SCFV-DSR" no corresponde a un objeto único

═══════════════════════════════════════════════════════════════════
RETIRADAS RB-0 ACUMULADAS
═══════════════════════════════════════════════════════════════════

  F-B9-1   F-AD ≡ §7.3 CONV              retirada
  F-B9-2   INFORME_FASE_4 cita bien      retirada
  F-B9-3   F-AD ≡ §7.3 G05               retirada
  F-B10-1  D-C-13 duplicado              retirada (RB-4)
  F-B10-2  D-C-32 reformulada            retirada (RB-5)
  F-B10-3  D-C 84 contables              retirada (RB-6)
  F-B11-1  D-META-9 = hipótesis          retirada (v0.11)

  Total: 7 retiradas · F-AH confirmada

═══════════════════════════════════════════════════════════════════
DEUDAS META ELEVADAS POR B
═══════════════════════════════════════════════════════════════════

  D-META-1    ~330 vs 348 · requiere Lista de Cierre v1.0
  D-META-2    "resuelta" C-beta §0 sin estatuto
  D-META-3    H8P §22.4 · 5 deudas · M registra 2
  D-META-4    D-BB-14 ≡ D-C-50 · deduplicación
  D-META-5    D-EPIST-1..7 · FASE 4 ausente
  D-META-6    "SIN ESTADO" no existe en M
  D-META-7    FASE 2.a.1/2.a.2 · reparaciones sin deuda
  D-META-8    M §0 subdeclara DC (1 vs 5)
  D-META-9    F-AD ≡ INFORME_FASE_4 §1 · CERRADA en B9
  D-META-10   CERRADA VERIFICADA del consolidado
  D-META-11   reformuladas 3/5/7 · tres cifras coexisten

  11 históricas · 1 cerrada (D-META-9) · 10 activas

═══════════════════════════════════════════════════════════════════
OBSERVACIONES REGISTRADAS
═══════════════════════════════════════════════════════════════════

  Total: 32+ observaciones B2-1 .. B13-4
  Listado en FASE_B_METODOLOGIA_v0.12 §D5 · §D6 y en los bloques.

  Observaciones clave:
    OBS-B13-4  M no es mono-repo
    OBS-B9-15  C-1/C-2/C-3 sin deuda en M · es F-Z, no F-H
    OBS-B7-4   AUDITORIA_26-09 contiene Hallazgos 1-8
    OBS-B6-2   _EA_MATRIZ documenta 6 deudas sin entrada H-XXX

═══════════════════════════════════════════════════════════════════
MATERIALIZACIÓN DE LA VENTANA
═══════════════════════════════════════════════════════════════════

  Bloque 1 · FASE_B_METODOLOGIA_v0.12.md
    commit   c61bc74
    hash     d834a459ff835fd26c02e483d68f53589ce7ecd216b87eed1bf3db4f32f45002
    tamaño   18.257 B

  Bloque 2 · FASE_B_PLAN_VERIFICACIONES_v0.3.md
    commit   83c67c4
    hash     3c13bcfc30c49495924306f29b8546b81923c9905cf430267006936c44741443
    tamaño   28.662 B

  Bloque 3 · REGISTRO_VENTANA_B.md
    commit   (pendiente · este bloque)
    hash     (pendiente · este bloque)

  Certificado  HASHES.txt
    hash     e5d36f91... (4 entradas + ancla)
    ancla    5833327c... (HASHES.txt fundacional)
    fundacional y SCFV_DSR intactos

═══════════════════════════════════════════════════════════════════
ESTADO AL CIERRE DEL REGISTRO
═══════════════════════════════════════════════════════════════════

  Fase B · materialización inicial     completada
  Fase B · cierre formal               NO alcanzado
  Fase B · verificaciones primarias    planificadas · no ejecutadas
  Intervención (Fase C)                NO habilitada

  Pendiente:
    · congelar v0.3 (acto del Operador)
    · autorizar F1..F8 (acto por acto)
    · materializar cada resultado
    · materializar FASE_B_ACTA_CIERRE.md
    · habilitar Intervención

  Reglas de ventana fijadas:
    RB-0 .. RB-12
    RB-13 (propuesta · no formalizada):
      materialización por bloque · un frente no se ejecuta
      sin que el archivo del frente anterior esté materializado

═══════════════════════════════════════════════════════════════════
FIN DEL REGISTRO DE VENTANA B
═══════════════════════════════════════════════════════════════════
