#!/bin/bash
set -e

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo ${GREEN} "Starting application in $ENVIRONMENT mode..." ${NC}
echo ${GREEN} "Host: $BACKEND_HOST, Port: $BACKEND_PORT" ${NC}

if [ "$ENVIRONMENT" = "development" ]; then
    echo ${GREEN} "Development mode with auto-reload enabled" ${NC}
    exec uvicorn app.main:app --host $BACKEND_HOST --port $BACKEND_PORT --reload
else
    echo ${GREEN} "Production/Staging mode with $BACKEND_WORKERS workers" ${NC}
    exec uvicorn app.main:app --host $BACKEND_HOST --port $BACKEND_PORT --workers $BACKEND_WORKERS
fi
