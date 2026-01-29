"""
libro_diario_refactor.py

Implementación refactorizada de un Libro Diario contable.
Se separa la lógica de cálculo de la lógica de presentación,
siguiendo buenas prácticas y convención PEP8.
"""

from typing import List, Dict, Union


class LibroDiario:
    """
    Representa un libro diario que almacena transacciones
    de ingresos y egresos y permite calcular sus totales.
    """

    VALID_TRANSACTION_TYPES = ("ingreso", "egreso")

    def __init__(self) -> None:
        """
        Inicializa el libro diario con una lista vacía de transacciones.
        """
        self.transacciones: List[Dict[str, Union[str, float]]] = []

    def agregar(
        self,
        fecha: str,
        descripcion: str,
        monto: float,
        tipo: str
    ) -> None:
        """
        Agrega una transacción al libro diario.

        :param fecha: Fecha de la transacción.
        :param descripcion: Descripción de la transacción.
        :param monto: Monto positivo de la transacción.
        :param tipo: Tipo de transacción ('ingreso' o 'egreso').
        :raises ValueError: Si los datos son inválidos.
        """

        if not fecha.strip():
            raise ValueError("La fecha no puede estar vacía.")

        if not descripcion.strip():
            raise ValueError("La descripción no puede estar vacía.")

        if tipo not in self.VALID_TRANSACTION_TYPES:
            raise ValueError(
                "El tipo de transacción debe ser 'ingreso' o 'egreso'."
            )

        if monto <= 0:
            raise ValueError("El monto debe ser un número positivo.")

        self.transacciones.append(
            {
                "fecha": fecha,
                "descripcion": descripcion,
                "monto": monto,
                "tipo": tipo,
            }
        )

    def resumen(self) -> Dict[str, float]:
        """
        Calcula el total de ingresos y egresos.

        :return: Diccionario con los totales calculados.
        """
        ingresos = 0.0
        egresos = 0.0

        for transaccion in self.transacciones:
            if transaccion["tipo"] == "ingreso":
                ingresos += transaccion["monto"]
            else:
                egresos += transaccion["monto"]

        return {
            "ingresos": ingresos,
            "egresos": egresos,
        }
