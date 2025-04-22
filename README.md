# 📐 Projeto: CALCULADORA_SIMPLES

---

## 🎯 Objetivo

Desenvolver uma **calculadora aritmética modular** e orientada a objetos (OO), com foco didático, demonstrando:

- A importância de **boas práticas de Engenharia de Software**.
- O uso de **orquestração com Prefect** para automação de deploys e versionamento.
- A **escalabilidade de soluções bem projetadas**.

---

## ⚙️ Funcionalidades da Versão Inicial

- [x] Operação de **adição**
- [x] Operação de **subtração**

### Próximas funcionalidades (versões futuras):

- [ ] Multiplicação
- [ ] Divisão
- [ ] Porcentagem

---

## 🧾 Justificativa

Este projeto será utilizado como **base didática** para demonstrar:

- Como **estruturar um projeto profissional** desde o início.
- A importância da **modularização e documentação adequada**.
- Como utilizar um orquestrador (Prefect) para **realizar deploys automáticos** e controlados.
- A evolução de um sistema em **ciclos incrementais com controle de versão** (`Git + GitHub Actions + Prefect`).

---

## 📌 Premissas do Projeto

- Linguagem principal: **Python 3.12.5**
- Ambiente virtual: `DEV`
- Repositório GitHub: [`CALCULADORA_SIMPLES`](https://github.com/SEU_USUARIO/CALCULADORA_SIMPLES) (link ilustrativo)
- Plataforma de orquestração: **Prefect Cloud**

---

## 🧱 Organização Modular

```text
CALCULADORA_SIMPLES/
│
├── modules/     → Operações aritméticas (módulos separados)
├── tests/       → Testes unitários e funcionais
├── flows/       → Fluxos orquestrados com Prefect
└── infra/       → Scripts de infraestrutura e CI/CD
```

---

## 📐 Padrões e Boas Práticas

- Princípio da Responsabilidade Única (**SRP – Single Responsibility Principle**)
- Nomeação clara e semântica para arquivos, funções e classes.
- Uso de `README.md` (apresentação do repositório) e `readme.txt` (documentação funcional).
- **Versionamento semântico** com tags e changelog.

---

## 🚀 Forma de Uso Esperada (Versão Inicial)

- Execução via **linha de comando (CLI)**.
- O fluxo `hello_world` do Prefect será usado para testar a orquestração.
- Os comandos de execução e testes estarão documentados na **ETAPA 1**.

---

## 🔁 Controle de Versão e Deploy

A cada nova funcionalidade:

1. `git commit`
2. `git push`
3. **Deploy automático** via GitHub Actions + Prefect Cloud

O pipeline CI/CD estará centralizado em `infra/`.

---

## 🧩 Sobre Type Hints

**Type hints** são anotações de tipo usadas em funções e métodos, como:

```python
def somar(self, a: float, b: float) -> float:
    return a + b
```

### Vantagens:

- Facilitam leitura e manutenção.
- Ajudam editores como VSCode com **autocompletar e linting**.
- Permitem documentação automática com ferramentas como Sphinx.

---

## 📦 Sobre `__init__.py`

Transforma o diretório em **pacote Python**, permitindo importações estruturadas.

Exemplo:

```python
from .operacoes import Calculadora
```

Pode conter:

- Inicializações de submódulos.
- Aliases.
- Registros.

---

## 📚 Uso de Docstrings

Docstrings são cadeias de caracteres que documentam **classes, funções e métodos** diretamente no código.

### Benefícios:

- Melhoram a **compreensão do código** por outros desenvolvedores.
- Podem ser lidas por ferramentas de **documentação automática**.
- Exibidas no **autocompletar de editores modernos**, como o VSCode.

---

> Este projeto segue os princípios de **evolução incremental**, com foco em clareza, manutenção e automação contínua.

### Criando script para testes iniciais com o ambiente assegurando configuração e conexão com o Prefect Cloud

```bash
    #!/bin/bash

    echo "🔍 Verificando status do Prefect 2.x..."

    echo -e "\n👉 Versão do Prefect:"
    prefect version

    echo -e "\n👉 Perfil ativo do Prefect:"
    prefect profile inspect || echo "⚠️ Nenhum perfil ativo encontrado."

    echo -e "\n👉 Configuração atual (variáveis relevantes):"
    prefect config view | grep "PREFECT_API"

    echo -e "\n👉 Testando listagem de deployments:"
    prefect deployment ls || echo "⚠️ Nenhum deployment encontrado ou Prefect não autenticado corretamente."

    echo -e "\n✅ Diagnóstico concluído."
    
``` 

#### Tornando o script executável
```bash
    chmod +x ./infra/scripts/check_prefect_status.sh
```
##### Executando o script

```bash
    ./infra/scripts/check_prefect_status.sh
```
#### Tornando os scripts run_server.sh e run_worker.sh executáveis

```bash
    chmod +x infra/run_server.sh infra/run_worker.sh
```

### Dica importante:

#### Se você versionar esse script no GitHub, vale lembrar que:

O __chmod +x__ não é preservado via __Git__ para o sistema local do usuário

_É boa prática documentar isso no README.md com, por exemplo:_

```bash
    chmod +x infra/run_server.sh infra/run_worker.sh
```
#### Para verificar arquivos executáveis no seu projeto, use:

```bash
    ls -l infra/
```