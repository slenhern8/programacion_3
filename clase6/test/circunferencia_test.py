import unittest
from app.circunferencia import circunferencia

class CircunferenciaTestCase(unittest.TestCase):
    def setUp(self):
        self.circunferencia = circunferencia(5)

    def test_calcular_area(self):
        self.assertEquals(self.circunferencia.calcular_area(),78.54, "Radio incorrecto")

    def test_calcular_diametro(self):
        self.assertEquals(self.circunferencia.calcular_diametro(),10.0, "Radio incorrecto")

    @unittest.skip("Esto es una prueba de demo")
    def test_nada(self):
        pass
