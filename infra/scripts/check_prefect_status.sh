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
