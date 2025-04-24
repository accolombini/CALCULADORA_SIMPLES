# CALCULADORA_SIMPLES

Este projeto demonstra uma calculadora modular orientada a objetos com orquestração Prefect e CI/CD com GitHub Actions.

## Estrutura

- `src/`: código da calculadora
- `flows/`: flows Prefect
- `tests/`: testes unitários
- `infra/`: Prefect Server local com Docker
- `.github/workflows/`: deploy CI
- `docs/`: documentação do projeto

## Executar localmente

```bash
./infra/run_server.sh
./infra/run_worker.sh
```

Acesse http://localhost:4200 para visualizar a interface Prefect Server.
