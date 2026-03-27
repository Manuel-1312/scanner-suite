# Scanner Suite — Zenmap+ para profesionales

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Face Plan](https://img.shields.io/badge/plan-face%201--4-brightgreen)](README.md)
[![Face2 Quality](https://github.com/as666/scanner-suite/actions/workflows/face2-quality.yml/badge.svg)](https://github.com/as666/scanner-suite/actions/workflows/face2-quality.yml)
[![Face3 Release](https://github.com/as666/scanner-suite/actions/workflows/face3-release.yml/badge.svg)](https://github.com/as666/scanner-suite/actions/workflows/face3-release.yml)

## ¿Qué es?
Una plataforma empaquetada (Python + UI ligera) que orquesta los mejores escáneres de red: Nmap, Masscan, httpx, nuclei, dnsx, entre otros. Está dirigida a profesionales que necesitan elegir el motor ideal, reutilizar perfiles, ver resultados y empaquetarlos sin abrir múltiples terminales.

## Face 1 — MVP disponible
- `core/`: wrappers de Python que lanzan nmap/masscan/httpx y normalizan la salida a JSON/Markdown.
- `ui/`: prototipo Tkinter que permite seleccionar perfiles y motores.
- `profiles/`: presets (`quick`, `web-audit`) con target, motores y notas.
- `docs/`: visión, fases, empaquetado (PyInstaller) y guías.
- `packaging/`: scripts para construir `.exe`/`.app` y un entrypoint release-ready con PyInstaller.

## Visión y objetivos
1. **Scanner orchestration:** combina motores diferentes, maneja credenciales y encadena filtros (`httpx` → `nuclei`).
2. **Interfaz Zenmap-style:** panel lateral con checklist y visor de resultados, exportable a HTML/Markdown.
3. **Distribución profesional:** binario multiplataforma empaquetado, instalaciones offline, ejemplo de PyInstaller en `packaging/`.
4. **Documentación y ética:** scope, permisos y código ético en `SECURITY.md`, `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`.

## Plan Face (1→4)
- **Face 1 (MVP):** base del repo y primera UI + perfiles.
- **Face 2 (Calidad):** lint, tests, workflow CI y packaging básico (ya completado).
- **Face 3 (Automatizaciones):** release automation (PyInstaller + upload de ZIP) + docs de releases (ya activo).
- **Face 4 (Community):** cheatsheets, onboarding, tutoriales y casos de uso compartidos.

## Face 2 — Calidad y pruebas
- `tests/test_profiles.py` valida los `profiles/*.json` y los motores admitidos.
- El workflow `.github/workflows/face2-quality.yml` instala dependencias, ejecuta `ruff` y `pytest` sobre Ubuntu/Windows, y en pushes a `master` crea el binario y lo sube como artifact `scanner-suite-dist`.
- Para contribuir ejecuta `python -m pytest` y `ruff check .` localmente.

## Face 3 — Release automation
- `.github/workflows/face3-release.yml` responde a `release.published`, corre `packaging/build-pyinstaller.sh`, crea un ZIP con el ejecutable y lo sube como asset mediante `softprops/action-gh-release@v1`.
- El proceso está documentado en `docs/RELEASES.md` junto con notas sobre perfiles y packaging.
- Actualiza siempre el título/descripción del release para explicar qué perfiles se utilizaron (`profiles/quick.json`, `profiles/web.json`).

## Cómo arrancar
```bash
python -m venv .venv
pip install -r requirements.txt
python core/scanner.py profiles/quick.json --engines nmap,masscan
```

## Contribuye
Revisa `docs/ROADMAP.md` para ver las fases y `CONTRIBUTING.md` para flujos de issues/PR. Mantén el enfoque en pruebas autorizadas, documenta cada escena y agrega referencias oficiales.
