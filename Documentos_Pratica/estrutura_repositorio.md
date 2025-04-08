prefect_calculadora/
├── .github/
│   └── workflows/
│       └── prefect-deploy.yml      # CI/CD automatizado via GitHub Actions
│
├── flows/
│   └── calculadora_flow.py         # Script Prefect Flow (orquestrador principal)
│
├── src/
│   ├── __init__.py
│   └── calculadora.py              # Lógica da calculadora (OO, modular)
│
├── tests/
│   └── test_calculadora.py         # Testes unitários com pytest
│
├── docs/
│   └── projeto_canvas.pdf          # Documento de projeto da solução (Canvas ou similar)
│
├── .gitignore
├── README.md                       # Instruções, objetivos, contexto didático
├── requirements.txt                # Lista de dependências fixadas
├── prefect.yaml                    # Arquivo de configuração do deployment Prefect


### ✍️ __Justificativa da Estrutura__
__flows/__ → onde ficam os scripts controlados pelo Prefect. Eles orquestram as tarefas do sistema, servindo como ponto de entrada do fluxo.

__src/__ → separa a regra de negócio (calculadora) da lógica de orquestração. Isso facilita testes, reuso e manutenibilidade.

__tests/__ → importante para garantia de qualidade. Aqui aplicamos testes unitários via pytest.

__docs/__ → guarda documentos de projeto, como Canvas, diagramas de classes UML e fluxogramas de processo.

__.github/workflows/__ → automação de deploy com GitHub Actions.

__prefect.yaml__ → configura o deployment automático dos flows no Prefect Cloud.

__README.md__ → apresenta o projeto aos alunos e colegas, com instruções e contexto didático.

