import unittest
from calculadora import calcular_media

class TestCalculadora(unittest.TestCase):
    
    def test_media_basica(self):
        # Teste básico com três notas comuns
        self.assertEqual(calcular_media(10, 20, 30), 20)
        
    def test_notas_zero(self):
        # Teste com todas as notas zero
        self.assertEqual(calcular_media(0, 0, 0), 0)
        
    def test_notas_maximas(self):
        # Teste com todas as notas no valor máximo (considerando 100 como máximo)
        self.assertEqual(calcular_media(100, 100, 100), 100)
        
    def test_notas_decimais(self):
        # Teste com notas que têm valores decimais
        self.assertAlmostEqual(calcular_media(15.5, 20.3, 10.7), 15.5)
        
    def test_notas_misturadas(self):
        # Teste com uma combinação de valores máximos, zero e decimal
        self.assertAlmostEqual(calcular_media(0, 100, 50.5), 50.17, places=2)

if __name__ == '__main__':
    unittest.main()
