import unittest
from src.procesador import Analizador
import os

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ruta_csv = os.path.join(os.path.dirname(__file__), '..', 'data', 'sri_ventas_2024.csv')
        cls.analizador = Analizador(ruta_csv)

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_por_provincia()
        self.assertIsInstance(resumen, dict)

    def test_exclusion_de_provincia_nd(self):
        resumen = self.analizador.ventas_por_provincia()
        self.assertNotIn("ND", resumen)

    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_por_provincia()
        self.assertEqual(len(resumen), 24)  # Asumiendo que hay 24 provincias válidas

    def test_ventas_totales_todaslas_mayores_0(self):
        resumen = self.analizador.ventas_por_provincia()
        self.assertTrue(all(float(v) > 5000 for v in resumen.values()))

    def test_exportaciones_por_mes_diccionario(self):
        exportaciones = self.analizador.exportaciones_por_mes()
        self.assertIsInstance(exportaciones, dict)

    def test_exportaciones_por_mes_valores_mayores_0(self):
        exportaciones = self.analizador.exportaciones_por_mes()
        self.assertTrue(all(float(v) >= 0 for v in exportaciones.values()))

    def test_provincia_con_mayor_importacion(self):
        provincia = self.analizador.provincia_con_mayor_importacion()
        self.assertIsInstance(provincia, str)
        self.assertGreater(len(provincia), 1)
