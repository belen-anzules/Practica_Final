import unittest
from libro_diario_refactor import LibroDiario


class TestLibroDiario(unittest.TestCase):
    def setUp(self):
        self.libro = LibroDiario()

    def test_resumen_con_transacciones(self):
        self.libro.agregar("2024-01-01", "Venta", 1000, "ingreso")
        self.libro.agregar("2024-01-02", "Compra", 300, "egreso")

        resumen = self.libro.resumen()

        self.assertEqual(resumen["ingresos"], 1000)
        self.assertEqual(resumen["egresos"], 300)

    def test_resumen_sin_transacciones(self):
        resumen = self.libro.resumen()

        self.assertEqual(resumen["ingresos"], 0)
        self.assertEqual(resumen["egresos"], 0)

    def test_error_monto_negativo(self):
        with self.assertRaises(ValueError):
            self.libro.agregar("2024-01-01", "Error", -100, "ingreso")


if __name__ == "__main__":
    unittest.main()
