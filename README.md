# Scanner Suite — Zenmap+ profesional

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Plan](https://img.shields.io/badge/progreso-4%20faces-brightgreen)](README.md)
[![Face2 Quality](https://github.com/as666/scanner-suite/actions/workflows/face2-quality.yml/badge.svg)](https://github.com/as666/scanner-suite/actions/workflows/face2-quality.yml)
[![Face3 Release](https://github.com/as666/scanner-suite/actions/workflows/face3-release.yml/badge.svg)](https://github.com/as666/scanner-suite/actions/workflows/face3-release.yml)

Scanner Suite fusiona CLI + UI + Release Automation para que equipos profesionales orquesten Nmap, Masscan, Httpx, Nuclei y otros scanners desde una sola app empaquetada. Perfilas a medida, pipelines prontos y reportes estructurados: todo configurable y auditado.

## Arquitectura pro
| Componente | Qué aporta |
| --- | --- |
| `config/scanners.yaml` | Define los motores, comandos, descripciones y formato de reporte centralizado (JSON/Markdown). |
| `core/config.py` | Carga la configuración, controla formato y rutas de reporte y centraliza los motores disponibles. |
| `core/scanner.py` | CLI asincrónica con logging profesional, ejecución paralela y reporte serializado. Permite parámetros dinámicos (targets, engines y salida). |
| `core/runner` | (próximamente) wrappers para cada engine, integraciones con pipelines, guardado de logs y hooks de post-procesado. |
| `ui/` | Prototipo de panel Tkinter que selecciona perfiles, engines y dispara `core/scanner.py`. |
| `profiles/` | Presets `quick`, `web-audit`, `custom` y repos de targets. |
| `packaging/` | PyInstaller script + workflow Face 3 para generar un ejecutable multiplataforma y subirlo como asset. |

## Tutorial pro
1. Clona, crea entorno y carga dependencias:
   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt -r requirements-dev.txt
   ```
2. Modifica `config/scanners.yaml` para añadir nuevos motores o ajustes en ruta/reporte.
3. Crea un perfil (`profiles/custom.json`) con `target`, `engines` y `description`.
4. Lanza el scan `python core/scanner.py profiles/custom.json --engines nmap,masscan` y guarda el reporte en JSON.
5. Usa `python ui/app.py` para comprobar visualmente el perfil y replicar la ejecución.
6. Empaqueta con PyInstaller (`packaging/build-pyinstaller.sh`) y publica el release; el workflow Face 3 subirá el ZIP y generará el asset.

## Flujos y valores
- **Reportes sólidos:** `core/scanner.py` usa `config/scanners.yaml` para decidir comandos y `report.format` para escribir JSON o Markdown.
- **Logging:** cada ejecución imprime logs con timestamp, motor usado y salida. Los operadores pueden analizar en `dist/logs/` (próximo módulo). 
- **Configuración extendida:** puedes clonar `config/scanners.yaml` por cliente, añadir otro engine + script y reutilizar la misma CLI.

## Pruebas y seguridad
- `tests/test_profiles.py` valida estructura de perfiles y motores admitidos.
- `.github/workflows/face2-quality.yml` ejecuta `ruff` + `pytest` y construye el binario en Ubuntu/Windows (pyinstaller incluido).
- `.github/workflows/face3-release.yml` se dispara en `release.published`, recompila el `ui/console.py` y genera el ZIP (`scanner-suite.zip`).

## Contribuye
- Crea nuevos perfiles/flows en `profiles/`.
- Añade integraciones en `core/runner/` (por ejemplo `nuclei`, `httpx` pipelines). 
- Escribe casos de estudio en `docs/case-studies/` y usa `docs/CHEAT_SHEETS.md` para entrenar a equipos.
- Mantén el uso ético: ejecuta solo sobre assets autorizados y documenta cada paso.
