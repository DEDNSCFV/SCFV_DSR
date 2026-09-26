"""
SCFV v8.1+ — Serializador Canónico
F3B.4-INFRA-D.1

Propósito:
    Convertir objetos Python soportados en estructuras JSON canónicas,
    deterministas y libres de representaciones Python no portables.

Reglas de serialización:
    None       -> None
    bool       -> bool
    int        -> int
    float      -> float
    str        -> str
    Enum       -> Enum.name
    datetime   -> datetime.isoformat()
    list       -> lista recursiva
    tuple      -> lista recursiva
    dict       -> diccionario recursivo
    dataclass  -> diccionario de campos recursivos

Todo tipo no soportado produce PersistenciaViolacion.

Reglas de deserialización:
    La reconstrucción tipada utiliza target_class.
    Enum       <- nombre del miembro
    datetime   <- ISO 8601
    dataclass  <- campos tipados recursivamente
    Optional   <- tipo interno cuando existe
"""

from dataclasses import fields, is_dataclass
from datetime import datetime
from enum import Enum
from typing import Any, Optional, Type, Union, get_args, get_origin


class PersistenciaViolacion(Exception):
    """
    Error de integridad de persistencia.

    Se utiliza cuando un objeto no puede representarse o reconstruirse
    mediante el contrato canónico.
    """
    pass


def _es_enum(tipo: Any) -> bool:
    """Determina si un tipo es una clase Enum."""
    return isinstance(tipo, type) and issubclass(tipo, Enum)


def _tipo_optional(tipo: Any) -> tuple[Any, bool]:
    """
    Extrae el tipo interno de Optional[T].

    Retorna:
        (tipo_interno, True)  si es Optional[T]
        (tipo_original, False) en cualquier otro caso
    """
    origen = get_origin(tipo)

    if origen is Union:
        argumentos = get_args(tipo)

        if type(None) in argumentos and len(argumentos) == 2:
            tipo_interno = next(
                argumento
                for argumento in argumentos
                if argumento is not type(None)
            )
            return tipo_interno, True

    return tipo, False


def serializar(obj: Any) -> Any:
    """
    Convierte recursivamente un objeto a una estructura JSON canónica.

    No utiliza default=str.
    Los tipos desconocidos son rechazados explícitamente.
    """

    # Primitivos
    if obj is None:
        return None

    # bool antes que int por herencia de Python
    if isinstance(obj, bool):
        return obj

    if isinstance(obj, int):
        return obj

    if isinstance(obj, float):
        return obj

    if isinstance(obj, str):
        return obj

    # Enum
    if isinstance(obj, Enum):
        return obj.name

    # datetime
    if isinstance(obj, datetime):
        return obj.isoformat()

    # list
    if isinstance(obj, list):
        return [serializar(item) for item in obj]

    # tuple -> lista JSON
    if isinstance(obj, tuple):
        return [serializar(item) for item in obj]

    # dict
    if isinstance(obj, dict):
        resultado = {}

        for clave, valor in obj.items():
            clave_serializada = serializar(clave)

            # Las claves JSON deben ser primitivas compatibles.
            if not isinstance(
                clave_serializada,
                (str, int, float, bool)
            ) and clave_serializada is not None:
                raise PersistenciaViolacion(
                    "Clave de diccionario no compatible con JSON: "
                    f"{type(clave).__name__}"
                )

            resultado[clave_serializada] = serializar(valor)

        return resultado

    # dataclass
    if is_dataclass(obj) and not isinstance(obj, type):
        resultado = {}

        for campo in fields(obj):
            valor = getattr(obj, campo.name)
            resultado[campo.name] = serializar(valor)

        return resultado

    # Todo lo demás se rechaza
    raise PersistenciaViolacion(
        "Tipo no soportado para serialización canónica: "
        f"{type(obj).__name__} "
        f"(valor: {repr(obj)})"
    )


def _deserializar_tipado(data: Any, tipo: Any) -> Any:
    """
    Reconstruye un valor utilizando su tipo declarado.
    """

    tipo_real, es_optional = _tipo_optional(tipo)

    # Optional[T] con None
    if data is None:
        if es_optional:
            return None

        # Los campos sin Optional también pueden tener None en datos
        # históricos; el constructor final determinará si es aceptable.
        return None

    # Enum
    if _es_enum(tipo_real):
        if not isinstance(data, str):
            raise PersistenciaViolacion(
                f"Valor inválido para Enum {tipo_real.__name__}: "
                f"{type(data).__name__}"
            )

        try:
            return tipo_real[data]
        except KeyError as exc:
            raise PersistenciaViolacion(
                f"Miembro Enum inválido para {tipo_real.__name__}: "
                f"{data!r}"
            ) from exc

    # datetime
    if tipo_real is datetime:
        if not isinstance(data, str):
            raise PersistenciaViolacion(
                "datetime canónico debe ser una cadena ISO 8601"
            )

        try:
            return datetime.fromisoformat(data)
        except ValueError as exc:
            raise PersistenciaViolacion(
                f"datetime ISO inválido: {data!r}"
            ) from exc

    # Dataclass
    if isinstance(tipo_real, type) and is_dataclass(tipo_real):
        return deserializar(data, tipo_real)

    # list[T]
    origen = get_origin(tipo_real)

    if origen is list:
        argumentos = get_args(tipo_real)

        if not isinstance(data, list):
            raise PersistenciaViolacion(
                f"Se esperaba lista para {tipo_real}"
            )

        if argumentos:
            tipo_elemento = argumentos[0]
            return [
                _deserializar_tipado(item, tipo_elemento)
                for item in data
            ]

        return list(data)

    # tuple[T, ...]
    if origen is tuple:
        argumentos = get_args(tipo_real)

        if not isinstance(data, list):
            raise PersistenciaViolacion(
                f"Se esperaba lista para {tipo_real}"
            )

        if len(argumentos) == 2 and argumentos[1] is Ellipsis:
            return tuple(
                _deserializar_tipado(item, argumentos[0])
                for item in data
            )

        if argumentos:
            if len(data) != len(argumentos):
                raise PersistenciaViolacion(
                    f"Longitud incorrecta para {tipo_real}"
                )

            return tuple(
                _deserializar_tipado(item, tipo_item)
                for item, tipo_item in zip(data, argumentos)
            )

        return tuple(data)

    # dict[K, V]
    if origen is dict:
        argumentos = get_args(tipo_real)

        if not isinstance(data, dict):
            raise PersistenciaViolacion(
                f"Se esperaba dict para {tipo_real}"
            )

        if len(argumentos) == 2:
            tipo_clave, tipo_valor = argumentos

            return {
                _deserializar_tipado(clave, tipo_clave):
                _deserializar_tipado(valor, tipo_valor)
                for clave, valor in data.items()
            }

        return dict(data)

    # Tipos primitivos
    if tipo_real in (str, int, float, bool):
        if not isinstance(data, tipo_real):
            raise PersistenciaViolacion(
                f"Tipo incorrecto: se esperaba "
                f"{tipo_real.__name__}, "
                f"se recibió {type(data).__name__}"
            )

        return data

    # Sin información tipada: conservar estructura JSON
    return deserializar(data)


def deserializar(
    data: Any,
    target_class: Optional[Type] = None
) -> Any:
    """
    Reconstruye una estructura JSON canónica.

    Si target_class es un dataclass, reconstruye sus campos utilizando
    las anotaciones de tipo.

    Sin target_class, devuelve una estructura Python equivalente,
    pero no intenta adivinar Enums ni datetime.
    """

    # Reconstrucción tipada de dataclass
    if target_class is not None:

        if not isinstance(target_class, type):
            raise PersistenciaViolacion(
                "target_class debe ser un tipo/clase"
            )

        if not is_dataclass(target_class):
            raise PersistenciaViolacion(
                "target_class debe ser un dataclass"
            )

        if not isinstance(data, dict):
            raise PersistenciaViolacion(
                f"Se esperaba dict para {target_class.__name__}"
            )

        kwargs = {}

        for campo in fields(target_class):

            if campo.name not in data:
                # Permitir que el dataclass utilice su valor por defecto.
                if (
                    campo.default is not campo.default_factory
                    and str(campo.default) != "<dataclasses._MISSING_TYPE object>"
                ):
                    continue

                # Forma robusta para detectar campos sin default.
                from dataclasses import MISSING

                if (
                    campo.default is MISSING
                    and campo.default_factory is MISSING
                ):
                    raise PersistenciaViolacion(
                        f"Campo requerido ausente: "
                        f"{target_class.__name__}.{campo.name}"
                    )

                continue

            try:
                kwargs[campo.name] = _deserializar_tipado(
                    data[campo.name],
                    campo.type
                )
            except PersistenciaViolacion:
                raise
            except Exception as exc:
                raise PersistenciaViolacion(
                    f"Error reconstruyendo campo "
                    f"{target_class.__name__}.{campo.name}: {exc}"
                ) from exc

        try:
            return target_class(**kwargs)
        except Exception as exc:
            raise PersistenciaViolacion(
                f"Error reconstruyendo dataclass "
                f"{target_class.__name__}: {exc}"
            ) from exc

    # None
    if data is None:
        return None

    # Primitivos
    if isinstance(data, (bool, int, float, str)):
        return data

    # Lista
    if isinstance(data, list):
        return [
            deserializar(item)
            for item in data
        ]

    # Diccionario
    if isinstance(data, dict):
        return {
            deserializar(clave):
            deserializar(valor)
            for clave, valor in data.items()
        }

    raise PersistenciaViolacion(
        "Tipo no soportado para deserialización: "
        f"{type(data).__name__}"
    )
