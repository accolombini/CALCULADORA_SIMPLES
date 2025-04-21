# modules/operacoes.py
"""
Módulo de operações básicas da calculadora.
Este módulo contém a classe Operacoes, que implementa métodos para realizar
adição e subtração de números.
Versão 1: Apenas adição e subtração.
    ||> Por que criar uma classe Operacoes? Para permitir escalabilidade e reutilização. Futuras funcionalidades (multiplicação, divisão, porcentagem) serão adicionadas como novos métodos, respeitando o princípio aberto-fechado (OCP) da Engenharia de Software.
    ||> Por que usar float? Para garantir flexibilidade com números decimais, pois operações podem envolver casas decimais.
    ||> Por que separar em modules/? Organização modular favorece testes, manutenção e integração com outros sistemas e orquestração.
    ||> Este módulo é parte de um projeto maior de calculadora.
    ||> Por que usar docstrings? Para documentar o código, facilitando a compreensão e manutenção.
    ||> Por que usar type hints? Para melhorar a legibilidade e facilitar a detecção de erros, indicando os tipos esperados para os parâmetros e o retorno dos métodos. Onde usamos?
    Parâmetros de métodos (a: float, b: float) => Tipo de retorno (-> float)
    ||> Por que usar __init__? Para inicializar o objeto Operacoes, mesmo que não faça nada no momento. Permite a criação de instâncias da classe.

"""

# Note o uso de docstrings para documentar a classe e seus métodos.
# Isso é uma boa prática de programação, pois facilita a compreensão do código.
# Onde usamos: Na definição da classe("""docstring da classe""")
# Em cada método("""docstring do método""")

# modules/operacoes.py

"""
Módulo com as classes Operacoes e Calculadora para a calculadora simples.
Versão 1: Apenas adição e subtração.

📌 Motivações e boas práticas aplicadas:
- Modularização em `modules/` para facilitar manutenção e reuso
- Uso de type hints para melhorar legibilidade e facilitar debug
- Docstrings em todos os métodos e classes
- Classe `Calculadora` como fachada, promovendo escalabilidade
"""


class Operacoes:
    """
    Classe responsável pelas operações básicas da calculadora.
    """

    def somar(self, a: float, b: float) -> float:
        """
        Retorna a soma de dois números.

        :param a: Primeiro número
        :param b: Segundo número
        :return: Resultado da soma
        """
        return a + b

    def subtrair(self, a: float, b: float) -> float:
        """
        Retorna a subtração entre dois números.

        :param a: Primeiro número
        :param b: Segundo número
        :return: Resultado da subtração
        """
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        """
        Retorna a multiplicação entre dois números.
        :param a: Primeiro número
        :param b: Segundo número
        :return: Resultado da multiplicação
        """
        return a * b

    def dividir(self, a: float, b: float) -> float:
        """
        Retorna a divisão entre dois números.
        :param a: Primeiro número
        :param b: Segundo número
        :return: Resultado da divisão
        """
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b


class Calculadora:
    """
    Classe fachada que encapsula o uso da classe Operacoes.

    Permite crescimento modular da aplicação com novas operações,
    respeitando o princípio aberto-fechado da Engenharia de Software.
    """

    def __init__(self):
        """
        Inicializa a calculadora com um objeto de operações.
        """
        self.operacoes = Operacoes()

    def somar(self, a: float, b: float) -> float:
        """
        Realiza a operação de soma usando a classe Operacoes.
        """
        return self.operacoes.somar(a, b)

    def subtrair(self, a: float, b: float) -> float:
        """
        Realiza a operação de subtração usando a classe Operacoes.
        """
        return self.operacoes.subtrair(a, b)

    def multiplicar(self, a: float, b: float) -> float:
        """
        Realiza a operação de multiplicação usando a classe Operacoes.
        """
        return self.operacoes.multiplicar(a, b)

    def dividir(self, a: float, b: float) -> float:
        """
        Realiza a operação de divisão usando a classe Operacoes.
        """
        return self.operacoes.dividir(a, b)
