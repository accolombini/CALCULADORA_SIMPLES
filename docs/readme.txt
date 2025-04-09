===============================================================
Projeto: CALCULADORA_SIMPLES
===============================================================

🔹 OBJETIVO
Desenvolver uma calculadora aritmética modular e orientada a objetos (OO), com foco didático, demonstrando:
- A importância de boas práticas de Engenharia de Software.
- O uso da orquestração com Prefect para automação de deploys e versionamento.
- A escalabilidade de soluções bem projetadas.

🔹 FUNCIONALIDADES DA VERSÃO INICIAL
- Operação de adição
- Operação de subtração

As funcionalidades serão incrementadas gradualmente nas próximas versões:
- Multiplicação
- Divisão
- Porcentagem

🔹 JUSTIFICATIVA
Este projeto será utilizado como base didática para demonstrar:
- Como estruturar um projeto profissional de software desde o início.
- A importância da modularização e da documentação adequada.
- Como utilizar um orquestrador para realizar deploys automáticos e controlados.
- A evolução de um sistema em ciclos incrementais com controle de versão (Git + GitHub Actions + Prefect).

🔹 PREMISSAS DO PROJETO
- Todo o código será escrito em Python 3.12.5.
- O ambiente de desenvolvimento será gerenciado por um ambiente virtual chamado `DEV`.
- O repositório principal será versionado no GitHub: `CALCULADORA_SIMPLES`.
- O Prefect Cloud será utilizado para monitoramento e execução dos fluxos automatizados.

🔹 ORGANIZAÇÃO MODULAR
- Cada operação será implementada em módulos separados dentro do diretório `modules/`.
- Os testes estarão no diretório `tests/`.
- A orquestração com o Prefect será organizada em `flows/`.
- Arquivos de infraestrutura e integração contínua estarão em `infra/`.

🔹 PADRÕES E BOAS PRÁTICAS
- Estrutura baseada em separação de responsabilidades (SRP - Single Responsibility Principle).
- Nomeação clara e semântica dos arquivos e funções.
- Uso de `README.md` para apresentação do repositório e `readme.txt` para documentação funcional.
- Uso de versionamento semântico nas tags e documentação de alterações.

🔹 FORMA DE USO ESPERADA (versão inicial)
- O sistema será executado por linha de comando.
- O fluxo `hello_world` do Prefect será usado para testar a orquestração.
- Comandos de execução e testes serão documentados na próxima etapa (ETAPA 1).

🔹 CONTROLE DE VERSÃO E DEPLOY
- A cada nova funcionalidade adicionada, será realizado:
  - Novo commit.
  - Novo push.
  - Novo deploy automático via GitHub Actions e Prefect Cloud.
- O pipeline de CI/CD será mantido em `infra/`.

🔹 SOBRE TYPE HINTS
- São anotações de tipo (`int`, `float`, `str`, etc.) usadas para indicar o tipo esperado de argumentos e retornos.
- Facilitam a leitura, a manutenção e a análise por ferramentas como linters, editores (VSCode) e documentação automatizada.
- Exemplo:
  ```python
  def somar(self, a: float, b: float) -> float:
      return a + b

🔹 SOBRE __init__.py

Esse arquivo transforma o diretório em um pacote Python, permitindo importações estruturadas.
Pode ser vazio ou conter inicializações de submódulos, aliases ou registros.
Alternativamente, pode conter código como: from .operacoes import Calculadora

🔹 USO DE DOCSTRINGS

São cadeias de caracteres usadas para documentar classes, funções e métodos diretamente no código.

Vantagens:

    Facilitam a compreensão por outros desenvolvedores.
    Podem ser lidas por ferramentas automáticas de geração de documentação.
    São exibidas automaticamente no autocompletar de editores como VSCode.
