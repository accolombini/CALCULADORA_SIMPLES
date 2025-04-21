"""
Testes unitários para a classe Calculadora.

🔍 Objetivos:
- Garantir que as operações básicas (soma e subtração) funcionem corretamente.
- Validar que a estrutura modular está funcionando conforme esperado.
"""

import unittest
from modules.operacoes import Calculadora


class TestCalculadora(unittest.TestCase):
    """
    Classe de testes unitários para a Calculadora.
    """

    def setUp(self):
        """
        Configuração inicial antes de cada teste.
        """
        self.calc = Calculadora()

    def test_soma(self):
        """
        Testa se a soma entre dois números está correta.
        """
        resultado = self.calc.somar(10, 5)
        self.assertEqual(resultado, 15)

    def test_subtracao(self):
        """
        Testa se a subtração entre dois números está correta.
        """
        resultado = self.calc.subtrair(10, 5)
        self.assertEqual(resultado, 5)
    
    def test_multiplicacao(self):
        """
        Testa se a multiplicação entre dois números está correta.
        """
        resultado = self.calc.multiplicar(10, 5)
        self.assertEqual(resultado, 50) 
    
    def test_divisao(self):
        """
        Testa se a divisão entre dois números está correta.
        """
        resultado = self.calc.dividir(10, 5)
        self.assertEqual(resultado, 2)
    
    def test_divisao_por_zero(self):
        """
        Testa se a divisão por zero levanta uma exceção.
        """
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)
    


if __name__ == "__main__":
    unittest.main()
