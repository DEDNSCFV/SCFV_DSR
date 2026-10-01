═══════════════════════════════════════════════════════════════════
FASE B · PLAN DE VERIFICACIONES PRIMARIAS v0.3
═══════════════════════════════════════════════════════════════════

ESTATUTO:   documento de trabajo de la fase de verificaciones
            NO es acta de cierre
            NO es v1.0
            NO ejecuta ningún comando
            NO modifica v0.12
            NO modifica SCFV_DSR
            NO modifica M
            NO firma §20

FECHA:      2026-09-30
VENTANA:    B
ORIGEN:     FASE_B_METODOLOGIA_v0.12 · congelada
FALSACIÓN:  ronda IA-2 de cierre · PASS
BLOQUES:    B14 (plan v0.1/v0.2/v0.3)
═══════════════════════════════════════════════════════════════════

PREAMBULO · REGLA TRANSVERSAL

  Los 8 frentes pueden PLANIFICARSE en paralelo.

  La EJECUCIÓN es secuencial por defecto:
    F1 -> F2 -> F3 -> F4 -> F5 -> F6 -> F7 -> F8.
    Un frente no se abre hasta cerrar el anterior.

  La ejecución paralela requiere autorización explícita del
  Operador frente por frente.

  Cada frente produce su archivo en resultados/F<N>_RESULTADO.md
  antes de declararse cerrado.

  Regla de formato:
    Los comandos de §4 son PROPUESTAS · no ejecución.
    Un comando = un bloque = una lectura.

═══════════════════════════════════════════════════════════════════
REGLAS DE VENTANA APLICABLES
═══════════════════════════════════════════════════════════════════

  RB-0   Ninguna conclusión sin verificación previa contra locus.
         Cinco retiradas del mismo patrón obligan a parar.

  RB-1   Asignación de repo solo por locus material o relación
         documental explícita · no por mención del nombre.

  RB-2   Duplicado cuenta una vez · segundo ID como marca cruzada.

  RB-3   Duplicado solo si comparten archivo:línea o módulo:objeto.

  RB-4   Duplicación intra-M solo si (a) locus idéntico o (b) fuente
         primaria declara "mismo objeto".

  RB-5   Estado asignado por B solo si M o fuente primaria lo declara.

  RB-6   Ninguna cifra desde narración. Toda cifra desde comando.
         Todo residuo se declara antes de cerrar.

  RB-7   Casos mixtos (código + doctrina) · prevalece TEC.
         Regla de ventana · no ontológica.

  RB-8   Una D-META cerrada no entra en el universo de intervención.

  RB-9   C-INTERV activo = TEC + DOC · sin cierres históricos
         · sin decisiones pendientes · sin discrepancias.

  RB-10  F2 · separar relación de estado:
           CONFIRMADA      mismo defecto material
           NO EQUIVALENTE  relación examinada · objetos distintos
           PENDIENTE       evidencia insuficiente
         RETIRADA es estado del ID · no resultado de comparación.

  RB-11  F8 · no restar duplicaciones antes de F8.
         F2 produce relaciones · F8 decide la operación.

  RB-12  La conversión relación -> operación aritmética ocurre en F8.
         Ningún frente anterior modifica el universo nominal.

═══════════════════════════════════════════════════════════════════
FRENTE 1 · M = 350
═══════════════════════════════════════════════════════════════════

§1 · ALCANCE

  Determinar qué significa "sostener 350" y qué evidencia primaria
  basta para ello. Separar concordancia cuantitativa de integridad
  ID x ID.

§2 · EVIDENCIA PRIMARIA REQUERIDA

  · M §2–§7 · §10 · §14 (cifras declaradas)
  · bloque_B_estatico.md (D-B)
  · bloque_Bbis_deudas.md (D-BB · D-IMP)
  · bloque_C_beta_deudas.md (D-C)
  · bloque_C_alpha_deudas.md (D-Calpha)
  · bloque_M1_alpha/beta/gamma/delta (M1)
  · bloque_M_deudas_catalogo_consolidado.md §7 (DM)

§3 · CRITERIO DE CIERRE

  El Frente 1 produce DOS resultados separados:

    R1a · CONCORDANCIA CUANTITATIVA
          Las 7 sub-cifras de M §10 coinciden con las declaraciones
          de las fuentes primarias por familia.
          -> Estatuto: 350 sostenida como cifra de concordancia.
          -> Registro: [DATO-2].

    R1b · INTEGRIDAD ID x ID
          Cada ID del universo nominal es enumerable y único.
          Requiere:
            · expandir rangos declarados como D-B-1..15
            · resolver dobles físicos como D-Calpha-100
            · verificar unicidad inter-familia
          -> Estatuto: universo nominal íntegro o no.
          -> Registro: [DATO] si íntegro · [PEND] si no.

  Los dos resultados son independientes.
  R1a positivo NO implica R1b positivo.

  Cierre del Frente 1:
    · [DATO-2] siempre que R1a cierre.
    · [DATO] solo si R1b cierra.
    · Si R1b no cierra, el frente se cierra con estatuto mixto
      y declara la parte del universo que no pudo verificar ID x ID.

§4 · COMANDOS PROPUESTOS

  P1.1 · extraer encabezados de M con cifras declaradas
    grep -nE "^## §[2-7]|^Total:|registradas" \
      bloque_M_deudas_catalogo_consolidado.md

  P1.2 · verificar sub-cifra por sub-cifra contra fuente primaria
    grep -cE "^\| D-BB-[0-9]+ " bloque_Bbis_deudas.md
    grep -cE "^\| D-C-[0-9]+ "  bloque_C_beta_deudas.md
    grep -cE "^\| D-Calpha-[0-9]+ " bloque_C_alpha_deudas.md

  P1.3 · buscar subdeclaraciones o rangos expandidos
    grep -nE "D-B-[0-9]+\.\.|D-Calpha-[0-9]+\.\.|D-M1" \
      bloque_M_deudas_catalogo_consolidado.md

  P1.4 · verificar partición 341+5+3+1 = 350
    grep -nE "341|350|reformuladas|retiradas" \
      bloque_M_deudas_catalogo_consolidado.md | head -30

§5 · RESULTADO ESPERADO

  · 350 clasificada como:
     [DATO-2]  si coincide con todas las fuentes primarias
     [PEND]    si alguna sub-cifra requiere resolución
     [DATO]    si se ejecuta enumeración ID x ID completa
  · Reporte por familia: sostenida / pendiente / discordante

§6 · IMPACTO POSIBLE SOBRE v0.12

  Si 350 sostenida -> §D4 confirma estatuto [DATO-2] (sin cambio).
  Si 350 requiere enumeración -> §D4 baja a [PEND].
  Si alguna sub-cifra discorda -> §D5 tabla se corrige en esa fila.

§7 · CONDICIONES DE STOP

  · Si más de 2 sub-cifras no coinciden con fuente primaria.
  · Si M §10 aparece contradicha por §2–§7 internamente.
  · Si se detecta que M cuenta rangos no expandidos como IDs.
  · Si el frente lleva más de 5 bloques sin converger.

═══════════════════════════════════════════════════════════════════
FRENTE 2 · DUPLICACIONES
═══════════════════════════════════════════════════════════════════

§1 · ALCANCE

  Construir matriz completa de correspondencias entre IDs.
  Clasificar cada par candidato como CONFIRMADA, NO EQUIVALENTE
  o PENDIENTE. NO restar del universo nominal todavía.

§2 · EVIDENCIA PRIMARIA REQUERIDA

  · bloques de origen de cada ID candidato
  · descripciones literales (no interpretadas)
  · locus declarado en cada descripción
  · commit / archivo:línea cuando aplique

  Pares candidatos conocidos:
    D-B-4    <-> D-C-54
    D-BB-14  <-> D-C-50
    D-C-14   <-> D-C-46
    D-C-13   <-> D-B-16..19
    D-C-61   <-> AUDITORIA_26-09 H4
    D-Calpha-69 <-> D-CONV-4

§3 · CRITERIO DE CIERRE

  Para cada par · tres relaciones posibles (RB-10):

    CONFIRMADA      mismo defecto material · mismo objeto
                    · locus idéntico o descripción idéntica.
    NO EQUIVALENTE  relación examinada · objetos distintos
                    · no es duplicación · no resta del cómputo.
    PENDIENTE       evidencia insuficiente para decidir
                    · se declara la fuente faltante.

  Estatuto separado · estado del ID (no de la relación):
    Si un ID está formalmente RETIRADO en su fuente primaria,
    su estado es RETIRADA. Independiente de la comparación de loci.

§4 · COMANDOS PROPUESTOS

  P2.1 · extraer línea completa de cada ID candidato
    grep -nE "D-B-4 |D-C-54" bloque_B_estatico.md bloque_C_beta_deudas.md
    grep -nE "D-BB-14 |D-C-50" bloque_Bbis_deudas.md bloque_C_beta_deudas.md
    grep -nE "D-C-14 |D-C-46" bloque_C_beta_deudas.md
    grep -nE "D-C-13 " bloque_C_beta_deudas.md
    grep -nE "D-B-16|D-B-17|D-B-18|D-B-19" bloque_B_estatico.md
    grep -nE "D-C-61" bloque_C_beta_deudas.md
    grep -nE "H4|Hallazgo 4" ~/scfv-dsr/DOCS/AUDITORIA_2026-09-26.md
    grep -nE "D-Calpha-69" bloque_C_alpha_deudas.md
    grep -nE "D-CONV-4" bloque_M_deudas_catalogo_consolidado.md

  P2.2 · buscar menciones cruzadas explícitas
    grep -rniE "mismo objeto|duplicad|equivalent" bloque_*.md

  P2.3 · verificar si algún par adicional no fue detectado
    grep -rnoE "MotorContable\(None\)" bloque_*.md
    grep -rnoE "evaluar_operacion" bloque_*.md
    grep -rnoE "ALTA_INCERTIDUMBRE" bloque_*.md
    grep -rnoE "Tetrada" bloque_*.md
    grep -rnoE "23 commits ahead" bloque_*.md

§5 · RESULTADO ESPERADO

  Matriz cerrada:
    CONFIRMADA:  N pares
    NO EQUIVALENTE: M pares
    PENDIENTE:   K pares

  Regla: solo CONFIRMADA entra en RB-2.
  Ningún par entra en el cómputo antes de cierre.

§6 · IMPACTO POSIBLE SOBRE v0.12

  · §D4 duplicados = 2 -> revisado según matriz.
  · FD2 · 348 provisional -> puede cerrarse como cifra derivada
    solo si la matriz cierra sin PENDIENTES.
  · §X2 · duplicadas = 2 -> actualizado.

§7 · CONDICIONES DE STOP

  · Si aparece un par no listado con locus idéntico evidente.
  · Si el criterio RB-3 vs RB-4 produce resultado ambiguo.
  · Si las descripciones son idénticas pero los loci difieren.
  · Si un par afecta a más de dos IDs.

═══════════════════════════════════════════════════════════════════
FRENTE 3 · D-C · RESIDUAL
═══════════════════════════════════════════════════════════════════

§1 · ALCANCE

  Localizar la única ?a de D-C (1 activa sin repo/locus clasificado).

§2 · EVIDENCIA PRIMARIA REQUERIDA

  · bloque_C_beta_deudas.md · listado completo de 88 IDs
  · clasificación B13.4 · 84 R3 + 1 MIX
  · diff nominal entre ambos conjuntos

§3 · CRITERIO DE CIERRE

  · La ?a queda identificada con ID.
  · Se le asigna repo/capa por RB-1 o se declara R7.
  · Si no se localiza -> declarar la discrepancia explícitamente.

§4 · COMANDOS PROPUESTOS

  P3.1 · extraer lista completa de IDs activos D-C
    grep -E "^\| D-C-[0-9]+ " bloque_C_beta_deudas.md | \
      awk -F'|' '{print $2}' | tr -d ' ' | sort -V > ~/tmp/dc_all.txt

  P3.2 · reconstruir lista clasificada B13.4 · transcripción manual
    # 85 IDs clasificados -> ~/tmp/dc_classified.txt

  P3.3 · diff
    comm -23 ~/tmp/dc_all.txt ~/tmp/dc_classified.txt

  P3.4 · extraer descripción del ID huérfano resultante
    grep -nE "<ID_huerfano>" bloque_C_beta_deudas.md

§5 · RESULTADO ESPERADO

  · 1 ID identificado
  · repo/capa asignada o R7 declarado
  · si hubiera más de 1 huérfano -> no es corrección menor
    · abre sub-frente

§6 · IMPACTO POSIBLE SOBRE v0.12

  · §D5 · D-C pasa de 84+1+1?a+2?r a 84+1+1 (completa).
  · §X2 · sin cambio numérico (ya contaba la activa).
  · cierra un residuo declarado.

§7 · CONDICIONES DE STOP

  · Si el diff produce más de un ID huérfano.
  · Si el ID huérfano no tiene descripción en la fuente.
  · Si aparece un ID que M declara y bloque_C_beta_deudas.md no contiene.

═══════════════════════════════════════════════════════════════════
FRENTE 4 · D-Calpha-69 <-> D-CONV-4
═══════════════════════════════════════════════════════════════════

§1 · ALCANCE

  Determinar si D-Calpha-69 y D-CONV-4 son el mismo objeto material
  o dos objetos relacionados.

§2 · EVIDENCIA PRIMARIA REQUERIDA

  · bloque_C_alpha_deudas.md · línea D-Calpha-69
  · bloque_M_deudas_catalogo_consolidado.md §11 · D-CONV-4
  · bloque_C_alpha_correcciones.md · RET-alpha-2
  · git log scfv-dsr · commits ahead al 28-09
  · Programa-de-Investigacion-SCFV · estado del repo

§3 · CRITERIO DE CIERRE

  Equivalencia material:     mismo objeto · mismo locus operativo
  Relación distinta:         mismo tema · distintos locus
  Pendiente:                 falta fuente para decidir

§4 · COMANDOS PROPUESTOS

  P4.1 · descripción literal de D-Calpha-69
    sed -n '<lín>p' bloque_C_alpha_deudas.md

  P4.2 · descripción literal de D-CONV-4
    sed -n '<lín>p' bloque_M_deudas_catalogo_consolidado.md

  P4.3 · acta correcciones C-alpha sobre D-CONV-4
    sed -n '/RET-alpha-2/,/^$/p' bloque_C_alpha_correcciones.md

  P4.4 · verificar estado actual de ambos repos
    git -C ~/scfv-dsr status -sb
    git -C ~/Programa-de-Investigacion-SCFV status -sb

§5 · RESULTADO ESPERADO

  · D-Calpha-69 <-> D-CONV-4 · estado final
  · Si equivalencia confirmada -> no resta del cuerpo 350
    (D-CONV está en anexo §11 · fuera del cuerpo).
  · Si equivalencia retirada -> D-Calpha-69 permanece en cuerpo.

§6 · IMPACTO POSIBLE SOBRE v0.12

  · FD5 · hipótesis -> confirmada o retirada.
  · §D4 · sin cambio de cifra (D-CONV está fuera del cuerpo).
  · §X2 · sin cambio.

§7 · CONDICIONES DE STOP

  · Si los estados de los repos son divergentes.
  · Si la descripción de D-Calpha-69 cita un objeto que no existe
    en scfv-dsr ni en Programa.
  · Si el commit "23 ahead" no puede localizarse en ninguno de los dos.


═══════════════════════════════════════════════════════════════════
FRENTE 5 · REFORMULADAS 3/5/7
═══════════════════════════════════════════════════════════════════

§1 · ALCANCE

  Reconstruir las tres cifras desde sus fuentes. Determinar si
  cuentan el mismo conjunto o conjuntos distintos.

§2 · EVIDENCIA PRIMARIA REQUERIDA

  · M §2 · §10 (cifra 5)
  · bloque_C_beta_correcciones.md §X (cifra 3)
  · bloque_C_alpha_correcciones.md §X (cifra 7)

§3 · CRITERIO DE CIERRE

  · Reconstruir el conjunto de IDs que cada fuente cuenta como
    reformulada.
  · Comparar conjuntos: idénticos / solapados / distintos.
  · Determinar qué significa "reformulada" en cada corpus.
  · No imponer M hasta terminar la comparación.

§4 · COMANDOS PROPUESTOS

  P5.1 · extraer bloque de reformuladas en M §2
    grep -nE "D-B-16\.\.19|D-BB-19|reformul" \
      bloque_M_deudas_catalogo_consolidado.md

  P5.2 · extraer bloque en C-beta correcciones
    sed -n '/REFORMULADAS/,/^$/p' bloque_C_beta_correcciones.md

  P5.3 · extraer bloque en C-alpha correcciones
    sed -n '/REFORMULADAS/,/^$/p' bloque_C_alpha_correcciones.md

  P5.4 · reconstruir qué IDs específicos cada lista incluye
    # (manual · solo 3 conjuntos pequeños)

§5 · RESULTADO ESPERADO

  · Los tres conjuntos reconstruidos.
  · Determinación: son el mismo conjunto (nombrado con criterios
    distintos) o son conjuntos distintos.
  · Regla de cómputo para v1.0.

§6 · IMPACTO POSIBLE SOBRE v0.12

  · §D4 · reformuladas = 5 -> revisado.
  · §D4 · FD4 · M prevalece -> puede confirmarse o caer.
  · §X2 · reformuladas = 5 -> actualizado.

§7 · CONDICIONES DE STOP

  · Si algún "reformulada" no tiene ID único asignable.
  · Si aparece un cuarto conjunto de reformuladas en otra fuente.
  · Si el criterio de reformulación es internamente contradictorio.

═══════════════════════════════════════════════════════════════════
FRENTE 6 · D-C-26 · ESTATUTO
═══════════════════════════════════════════════════════════════════

§1 · ALCANCE

  Determinar qué estatuto tiene D-C-26 frente al cómputo del cuerpo.

§2 · EVIDENCIA PRIMARIA REQUERIDA

  · bloque_M §5 · D-C-26 declarada ABIERTA
  · bloque_M §12 · DC-10 (no afecta D-C-26)
  · AUDITORIA_2026-09-26.md · Hallazgo 1
  · git log scfv-dsr · commit abb2bac
  · consolidado §2.6 · declara CERRADA VERIFICADA

§3 · CRITERIO DE CIERRE

  Determinar, en este orden:

    1. Qué declara M sobre D-C-26.
    2. Qué demuestra la evidencia externa (AUDITORIA_26-09 · abb2bac).
    3. Qué estatuto normativo/documental tiene esa evidencia
       dentro del régimen de M y del régimen de Fase A.
    4. Qué regla de precedencia resulta aplicable.

  Resultados posibles · no presupuestos:

    A · M ABIERTA + fuente externa sin autoridad para modificar M.
    B · cierre documental externo reconocido con autoridad declarada.
    C · doble estatuto explícitamente documentado.
    D · conflicto no resoluble con las fuentes actuales -> PEND.

§4 · COMANDOS PROPUESTOS

  P6.1 · verificar M §5 rango
    sed -n '/D-C-23\.\.42/,/D-C-44/p' \
      bloque_M_deudas_catalogo_consolidado.md

  P6.2 · verificar Hallazgo 1
    sed -n '/Hallazgo 1/,/Hallazgo 2/p' \
      ~/scfv-dsr/DOCS/AUDITORIA_2026-09-26.md

  P6.3 · verificar commit abb2bac
    git -C ~/scfv-dsr log abb2bac --stat
    git -C ~/scfv-dsr show abb2bac --stat | head -40

  P6.4 · verificar consolidado
    grep -nE "D-C-26|CERRADA VERIFICADA" \
      ~/scfv-dsr/DOCS/historicos/ventana_2026-09-30/VENTANA_2026-09-30_CONSOLIDADO.md

§5 · RESULTADO ESPERADO

  · Estatuto único o doble documentado.
  · Regla de cómputo explícita.
  · Sin cambiar M.

§6 · IMPACTO POSIBLE SOBRE v0.12

  · §D4 · CERRADA VERIFICADA · estatuto final definido.
  · §X2 · CERRADA DOCUMENTAL/VERIFICADA · cifras ajustadas si aplica.
  · FD3 · puede cerrarse.
  · Si D-C-26 se declara CERRADA -> reduce pendientes · ajusta C-INTERV.

§7 · CONDICIONES DE STOP

  · Si M y fuente externa producen estatutos incompatibles sin
    regla de precedencia.
  · Si el commit abb2bac no existe o no corresponde.
  · Si el consolidado cita "D-C-26" con otra descripción material.

═══════════════════════════════════════════════════════════════════
FRENTE 7 · ?a = 72
═══════════════════════════════════════════════════════════════════

§1 · ALCANCE

  Aplicar RB-1 sistemáticamente a los 72 IDs activos sin
  clasificación de repo: 24 D-BB + 47 D-Calpha + 1 D-C.

  No asumir 72 verificaciones independientes. Determinar cuáles
  tienen locus material o relación documental explícita en sus
  descripciones y cuáles no.

  Criterio de cierre: Determinar, para cada ?a, si existe:
    (a) locus material verificable, o
    (b) relación documental explícita.
  Solo los que carezcan de ambos permanecen como R7 / DISCREP.

§2 · EVIDENCIA PRIMARIA REQUERIDA

  · descripciones literales de los 72 IDs
  · archivos mencionados en cada descripción
  · criterio RB-1

§3 · CRITERIO DE CIERRE

  Para cada ?a:

    LOCALIZADO    descripción cita archivo/línea/módulo explícito
                  -> asignar repo/capa por RB-1

    DOCUMENTAL    descripción cita documento con autoridad reconocida
                  -> asignar repo/capa por relación documental

    R7            sin locus material ni relación documental explícita
                  -> declarar sin repo · no asignar por mención

§4 · COMANDOS PROPUESTOS

  P7.0 · verificar cardinalidad y unicidad del conjunto ?a

  P7.0.1 · universo activo D-BB
    grep -E "^\| D-BB-[0-9]+ " bloque_Bbis_deudas.md | \
      awk -F'|' '{print $2}' | tr -d ' ' | sort -V > ~/tmp/dbb_all.txt

  P7.0.2 · universo activo D-Calpha (excluir doble D-Calpha-100)
    grep -E "^\| D-Calpha-[0-9]+ " bloque_C_alpha_deudas.md | \
      awk -F'|' '{print $2}' | tr -d ' ' | sort -V | uniq > ~/tmp/dca_all.txt

  P7.0.3 · universo activo D-C
    grep -E "^\| D-C-[0-9]+ " bloque_C_beta_deudas.md | \
      awk -F'|' '{print $2}' | tr -d ' ' | sort -V > ~/tmp/dc_all.txt

  P7.0.4 · conjunto clasificado en v0.12 · transcripción manual
    # a ~/tmp/dbb_classified.txt · dca_classified.txt · dc_classified.txt

  P7.0.5 · diff por familia
    comm -23 ~/tmp/dbb_all.txt ~/tmp/dbb_classified.txt > ~/tmp/dbb_qa.txt
    comm -23 ~/tmp/dca_all.txt ~/tmp/dca_classified.txt > ~/tmp/dca_qa.txt
    comm -23 ~/tmp/dc_all.txt  ~/tmp/dc_classified.txt  > ~/tmp/dc_qa.txt

  P7.0.6 · verificar cardinalidad
    wc -l ~/tmp/dbb_qa.txt ~/tmp/dca_qa.txt ~/tmp/dc_qa.txt

  Criterio de cierre P7.0:
    · dbb_qa debe tener 24 líneas
    · dca_qa debe tener 47 líneas
    · dc_qa  debe tener 1 línea
    Si alguna línea no coincide -> no ejecutar P7.1/P7.2.
    Declarar discrepancia · abrir sub-frente.

  P7.1 · extraer descripciones literales de los ?a (D-BB)
    while IFS= read -r id; do
      grep -nE "^\| $id " bloque_Bbis_deudas.md
    done < ~/tmp/dbb_qa.txt

  P7.2 · extraer descripciones literales de los ?a (D-Calpha)
    while IFS= read -r id; do
      grep -nE "^\| $id " bloque_C_alpha_deudas.md
    done < ~/tmp/dca_qa.txt

  P7.3 · clasificación por RB-1 · por descripción · manual

§5 · RESULTADO ESPERADO

  Sub-partición de los 72:
    LOCALIZADO       ~N1 IDs
    DOCUMENTAL       ~N2 IDs
    R7               ~N3 IDs
  N1 + N2 + N3 = 72

§6 · IMPACTO POSIBLE SOBRE v0.12

  · §D5 · reduce la columna "?"
  · §D5 · aumenta R1–R6 con los localizados
  · §X2 · puede afectar C-INTERV si algún ?a resulta ser R3/TEC
  · FD12 · 71 sin clasificar -> recalculado

§7 · CONDICIONES DE STOP

  · Si más de 3 IDs de una misma familia resultan no clasificables
    por descripción · indica problema estructural de la familia.
  · Si aparecen descripciones que citan repos no listados en R1–R6.
  · Si algún ID tiene descripción vacía en fuente.

═══════════════════════════════════════════════════════════════════
FRENTE 8 · C-INTERV · RECOMPUTACIÓN
═══════════════════════════════════════════════════════════════════

§1 · ALCANCE

  No es un frente de investigación. Es el algoritmo formal que
  recibirá los resultados de los frentes 1–7 y producirá el
  universo C-INTERV activo.

§2 · INSUMOS DEL ALGORITMO

  El algoritmo recibe:

    · F1 · universo nominal verificado (aun si queda [DATO-2])
    · F2 · correspondencias como RELACIONES (CONFIRMADA /
                                            NO EQUIV / PENDIENTE)
    · F3–F7 · estados · loci · clasificación por repo

  F2 NO altera el universo nominal.
  F2 produce relaciones que F8 aplicará · no F2 directamente.

§3 · CRITERIO DE CIERRE

  El algoritmo no elimina registros. El algoritmo ASIGNA ESTADO.

    Universo nominal (N1)
          ↓
    Estado documental por entrada
          ↓
    Clasificación de actividad
          ↓
    C-INTERV activo (N4)

  Estados posibles por entrada:

    ACTIVO         justifica intervención (TEC · DOC)
    HISTÓRICO      cerrado o retirado con fuente · permanece en
                   el catálogo como registro
    META-PEND      requiere decisión posterior
    DISCREP        discrepancia no resuelta
    DUPLICADO      relación con otro ID · no resta del catálogo
                   hasta que F8 lo consuma con regla explícita

  RB-8 aplica:
    Una entrada HISTÓRICA (por cierre documental o retiro) no
    entra en C-INTERV activo.
    NO se elimina del universo nominal.
    Su registro permanece.

  Regla derivada:
    C-INTERV activo (N4) es subconjunto de Universo nominal (N1).
    N4 no es "N1 menos eliminados".
    N4 es "N1 filtrado por estado ACTIVO".

§4 · COMANDOS PROPUESTOS

  Ninguno. Es diseño algorítmico, no ejecución.
  Se redacta como pseudocódigo o regla textual.

§5 · RESULTADO ESPERADO

  Algoritmo documentado que puede ejecutarse cuando los frentes
  1–7 cierren. Producirá C-INTERV activo con trazabilidad completa.

§6 · IMPACTO POSIBLE SOBRE v0.12

  · §X2 · TEC+DOC = 267 (actual) -> recalculado
  · §X4 · META-{POL,ESTAT,RECON} -> reflejado
  · FD4 · asignación C-INTERV -> verificada contra el algoritmo

§7 · CONDICIONES DE STOP

  · Si algún frente 1–7 produce resultado ambiguo que el algoritmo
    no puede resolver por regla · detener y declarar.
  · Si el algoritmo produce un resultado que contradice M sin
    regla de precedencia.
  · Si el algoritmo requiere información no producida por 1–7.

═══════════════════════════════════════════════════════════════════
ESTADO DE LA PLANIFICACIÓN
═══════════════════════════════════════════════════════════════════

  Frentes planificados        8/8
  Correcciones aplicadas:
    v0.1 (original)
    v0.2 (ronda 1 · 4 correcciones)
    v0.3 (ronda 2 · 2 correcciones)

  Ejecución                   ninguna
  STOP de ejecución           vigente hasta autorización por frente

  Reglas de ventana acumuladas:
    RB-0..RB-9   (v0.12)
    RB-10        F2 · separar relación de estado
    RB-11        F8 · no restar duplicaciones antes de F8
    RB-12        conversión relación -> operación en F8

  Documento no compite con v0.12.
  Es anexo de trabajo de la fase de verificaciones.

═══════════════════════════════════════════════════════════════════
REGLAS TRANSVERSALES DE LA FASE
═══════════════════════════════════════════════════════════════════

  · Cada frente produce su propio bloque de resultados.
  · Un frente no se abre hasta cerrar el anterior · salvo
    autorización explícita del Operador para paralelizar.
  · Frente 8 no se ejecuta hasta que 1–7 cierren.
  · Los comandos de §4 son propuestas.
  · Toda cifra producida por un frente se declara [DATO] o [PEND].
  · Toda reasignación de v0.12 por resultado de un frente se
    registra como delta · no se reescribe v0.12.

═══════════════════════════════════════════════════════════════════
FIN DE FASE_B_PLAN_VERIFICACIONES_v0.3
═══════════════════════════════════════════════════════════════════
