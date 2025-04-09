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


if __name__ == "__main__":
    unittest.main()
