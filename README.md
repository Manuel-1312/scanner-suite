# Scanner Suite — Zenmap+ para profesionales

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Plan](https://img.shields.io/badge/progreso-4%20faces-brightgreen)](README.md)
[![Face2 Quality](https://github.com/as666/scanner-suite/actions/workflows/face2-quality.yml/badge.svg)](https://github.com/as666/scanner-suite/actions/workflows/face2-quality.yml)
[![Face3 Release](https://github.com/as666/scanner-suite/actions/workflows/face3-release.yml/badge.svg)](https://github.com/as666/scanner-suite/actions/workflows/face3-release.yml)

Scanner Suite es una app empaquetada (Python + UI ligera) que combina todos los motores imprescindibles para escanear redes: Nmap, Masscan, httpx, nuclei, dnsx y más. El usuario elige el motor, configura un perfil/arquetipo y recibe un reporte completo, listo para exportar o empaquetar en un binario profesional.

## Qué ofrece hoy
| Módulo | Qué hace |
| --- | --- |
| `core/` | Orquesta los comandos (nmap/masscan/httpx) y normaliza stdout/stderr en JSON/Markdown. |
| `ui/` | Panel Tkinter minimalista: selecciona perfiles, motores y activa el scan. |
| `profiles/` | Presets (`quick`, `web-audit`, `custom`) con `target`, `engines` y notas. |
| `docs/` | Roadmap, packaging, comunidad, cheatsheets y releases. |
| `packaging/` | Scripts PyInstaller para convertir la app en un `.exe` multiplataforma. |

## Objetivo
1. **Zenmap-style UX:** interfaz clara, checklist de motores y visor de resultados con export fácil.
2. **Scanner orchestration:** lanza diferentes engines, encadena HTTP → nuclei y agrega filtros configurables.
3. **Distribución profesional:** binarios listos en `dist/`, release automation y artefactos firmados.
4. **Comunicación:** documentación viva (guide, status, case studies), ética y políticas (= `SECURITY.md`, `CODE_OF_CONDUCT.md`).

## Tutorial paso a paso
1. Clona y crea entorno:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # o .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```
2. Revisa `profiles/quick.json` y duplica para crear `profiles/custom.json` con `target`, `engines` y notas.
3. Ejecuta un scan:
   ```bash
   python core/scanner.py profiles/custom.json --engines nmap,httpx
   ```
4. Revisa `scanner-report.json` generado y abre `ui/app.py` para validar visualmente el perfil.
5. Empaqueta con PyInstaller:
   ```bash
   chmod +x packaging/build-pyinstaller.sh
   packaging/build-pyinstaller.sh
   ```
6. Publica un release en GitHub; el workflow `face3-release` recompila y adjunta el ZIP en el release.

## Recursos clave
- **docs/ROADMAP.md:** fases planificadas.
- **docs/CHEAT_SHEETS.md:** comandos rápidos.
- **docs/RELEASES.md:** guía de publicación.
- **docs/COMMUNITY_GUIDE.md** y **docs/STATUS.md:** comunidad, feedback y tablero de estado.
- **docs/case-studies/**: guarda cada investigación con objetivo, herramientas y lecciones.

## Pruebas y packaging
- `tests/test_profiles.py` verifica que los perfiles tengan `target`, `engines` y motores válidos.
- `.github/workflows/face2-quality.yml` corre `ruff`, `pytest` y empaqueta el binario en Ubuntu/Windows; el artifact es `scanner-suite-dist`.
- `.github/workflows/face3-release.yml` responde a `release.published`, recompila y sube un ZIP `scanner-suite.zip`.

## Contribuye
Añade perfiles, mejora wrappers, escribe casos en `docs/case-studies/` o ayuda con la UI. Sigue el flujo de `CONTRIBUTING.md`, respeta `CODE_OF_CONDUCT.md` y reporta vulnerabilidades en `SECURITY.md`. Mantén todo orientado a entornos autorizados y documenta el alcance de cada scan.
