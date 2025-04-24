#!/bin/bash
export PREFECT_API_URL=http://localhost:4200/api
prefect worker start -p hello-pool
