import unittest
from app.itbms import calcular_itbms

class TestITBMS(unittest.TestCase):
    def test_calcular_itbms(self):
        self.assertEquals(calcular_itbms(1.0),0.07)

if __name__ == '__main__':
    unittest.main()
