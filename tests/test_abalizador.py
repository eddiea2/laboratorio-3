import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("data/sri_ventas_2024.csv")

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_por_provincia()
        self.assertIsInstance(resumen, dict)
        

    def test_exclusion_de_provincia_nd(self):
        resumen = self.analizador.ventas_por_provincia()
        self.assertNotIn("ND", resumen)



    def test_ventas_totales_todas_las_provincias(self):
        resumen = self.analizador.ventas_por_provincia()
        total_provincias = len(resumen)
        self.assertEqual(total_provincias, 25)  # <- No pongas 25, porque "ND" fue eliminada



    def test_ventas_totales_todaslas_mayores_0(self):
        resumen = self.analizador.ventas_por_provincia()
        self.assertTrue(all(float(v) > 5000 for v in resumen.values()))

