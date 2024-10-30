import unittest
from calculadora import calcular_media

class TestCalculadora(unittest.TestCase):
    
    def setUp(self):
        """Método chamado antes de cada teste. Pode ser usado para inicializar dados comuns."""
        self.notas_comuns = [10, 20, 30]
        self.notas_zero = [0, 0, 0]
        self.notas_maximas = [100, 100, 100]
        self.notas_decimais = [15.5, 20.3, 10.7]
        self.notas_misturadas = [0, 100, 50.5]
    
    def test_media_basica(self):
        """Teste básico com três notas comuns."""
        resultado = calcular_media(*self.notas_comuns)
        self.assertEqual(resultado, 20)

    def test_notas_zero(self):
        """Teste com todas as notas zero."""
        resultado = calcular_media(*self.notas_zero)
        self.assertEqual(resultado, 0)

    def test_notas_maximas(self):
        """Teste com todas as notas no valor máximo (considerando 100 como máximo)."""
        resultado = calcular_media(*self.notas_maximas)
        self.assertEqual(resultado, 100)

    def test_notas_decimais(self):
        """Teste com notas que têm valores decimais."""
        resultado = calcular_media(*self.notas_decimais)
        self.assertAlmostEqual(resultado, 15.5, places=2)

    def test_notas_misturadas(self):
        """Teste com uma combinação de valores máximos, zero e decimal."""
        resultado = calcular_media(*self.notas_misturadas)
        self.assertAlmostEqual(resultado, 50.17, places=2)

    def test_notas_invalidas(self):
        """Teste para verificar se o código levanta uma exceção com notas inválidas."""
        with self.assertRaises(ValueError):
            calcular_media(-10, 50, 30)  # Nota negativa
        with self.assertRaises(ValueError):
            calcular_media(110, 50, 30)  # Nota acima do máximo

    def test_sem_notas(self):
        """Teste para verificar se o código levanta uma exceção quando nenhuma nota é fornecida."""
        with self.assertRaises(ValueError):
            calcular_media()  # Sem notas

if __name__ == '__main__':
    unittest.main()
