#!/usr/bin/env bash
set -euo pipefail

pyinstaller \
  --onefile \
  --name "scanner-suite" \
  --add-data "profiles:profiles" \
  --add-data "docs:docs" \
  core/scanner.py

echo "Build completo. Ejecutable en dist/scanner-suite"