#!/bin/sh

# Salir inmediatamente si un comando falla
set -e

# Instalar dependencias
echo "Instalando dependencias..."
pip install --upgrade pip
pip install -r requirements.txt

# Configurar PYTHONPATH
# Reemplaza "/ruta/a/tu/directorio" con la ruta del directorio que quieres añadir a PYTHONPATH
export PYTHONPATH="$PYTHONPATH:$(pwd)/src"

# Ejecutar pruebas
echo "Ejecutando pruebas..."
pytest

echo "Pruebas finalizadas..."