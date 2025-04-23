
"""
    ||>Objetivo deste Flow
        |>Orquestrar a execução de uma calculadora simples com duas operações implementadas em modules/operacoes.py: adição e subtração.
        |>Este flow também serve para validar toda a estrutura do repositório e os benefícios iniciais da orquestração com o Prefect.
    
        ||> Importante:
            |> Usamos @task para transformar executar_operacoes() em uma tarefa isolada e observável pelo Prefect.
            |> @flow encapsula a orquestração das tarefas, e poderá ser versionado, agendado ou acionado via CI/CD.
            |> O bloco if __name__ == "__main__" permite testes locais sem necessidade de deploy.
            |> Integra-se diretamente ao Prefect via prefect.yaml.
"""

"""
flow_versao1.py — Orquestra o primeiro fluxo da Calculadora Simples
Executa testes automatizados antes de executar operações
"""


import subprocess
from prefect import flow, task
from modules.operacoes import Calculadora


@task(name="Executar Testes Automatizados")
def executar_testes():
    """
    Executa os testes da pasta `tests/` usando o framework unittest.
    Se os testes falharem, o processo será interrompido.
    """
    print("🔍 Executando testes unitários com unittest...")
    resultado = subprocess.run(
        ["python", "-m", "unittest", "discover", "tests"], capture_output=True, text=True)

    print("📄 Saída dos testes:\n", resultado.stdout)
    if resultado.returncode != 0:
        print("❌ Testes falharam:\n", resultado.stderr)
        raise Exception(
            "Os testes automatizados falharam. O fluxo foi interrompido.")
    print("✅ Todos os testes passaram com sucesso.")


@task(name="Executar Operações da Calculadora")
def executar_operacoes(valor1: float, valor2: float) -> None:
    """
    Instancia a calculadora e executa as operações básicas da versão 1.
    """
    calc = Calculadora()
    print("Soma:", calc.somar(valor1, valor2))
    print("Subtração:", calc.subtrair(valor1, valor2))
    print("Multiplicação:", calc.multiplicar(valor1, valor2))
    try:
        print("Divisão:", calc.dividir(valor1, valor2))
    except ValueError as e:
        print("Erro ao dividir:", str(e))
    print("Operações concluídas.")


@flow(name="flow-versao1")
def flow_versao1():
    """
    Primeiro fluxo da calculadora orquestrada com Prefect.
    """
    valor1 = 10.0
    valor2 = 5.0

    executar_testes()  # Executa testes antes da operação
    executar_operacoes(valor1, valor2)


if __name__ == "__main__":
    flow_versao1()
