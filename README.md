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
- **Face 2 (Calidad):** lint, tests, workflow CI y packaging básico (ya completado).[face2 link](#face-2--calidad-y-pruebas)
- **Face 3 (Automatizaciones):** release automation (PyInstaller + upload de ZIP) + docs de releases (ya activo).[face3 link](#face-3—release-automation)
- **Face 4 (Community):** cheatsheets, onboarding, tutoriales y casos de uso compartidos.
  - Documenta avances en `docs/COMMUNITY_GUIDE.md`.
  - Usa `docs/STATUS.md` para mostrar triage `TODO/IN PROGRESS/DONE`.
  - Comparte casos en `docs/case-studies/` (puedes crear este folder) y actualiza `docs/CHEAT_SHEETS.md`.

## Face 2 — Calidad y pruebas
- `tests/test_profiles.py` valida los `profiles/*.json` y los motores admitidos.
- El workflow `.github/workflows/face2-quality.yml` instala dependencias, ejecuta `ruff` y `pytest` sobre Ubuntu/Windows, y en pushes a `master` crea el binario y lo sube como artifact `scanner-suite-dist`.
- Para contribuir ejecuta `python -m pytest` y `ruff check .` localmente.

## Face 3 — Release automation
- `.github/workflows/face3-release.yml` responde a `release.published`, corre `packaging/build-pyinstaller.sh`, crea un ZIP con el ejecutable y lo sube como asset mediante `softprops/action-gh-release@v1`.
- El proceso está documentado en `docs/RELEASES.md` junto con notas sobre perfiles y packaging.
- Actualiza siempre el título/descripción del release para explicar qué perfiles se utilizaron (`profiles/quick.json`, `profiles/web.json`).

## Face 4 — Comunidad y difusión
- Sigue los pasos de `docs/COMMUNITY_GUIDE.md` para publicar avances, entrenamientos y feedback.
- Usa el tablero `docs/STATUS.md` para mostrar qué etapas están en `TODO`, `IN PROGRESS` o `DONE`.
- Comparte casos en `docs/case-studies/README.md` y añade nuevas notas siguiendo la plantilla (objetivo, herramientas, resultados y lecciones).
- Actualiza `docs/CHEAT_SHEETS.md` con atajos o tips derivados de esos estudios.

## Cómo arrancar
```bash
python -m venv .venv
pip install -r requirements.txt
python core/scanner.py profiles/quick.json --engines nmap,masscan
```

## Tutorial paso a paso
1. **Clona el repositorio** y crea entornos virtuales como arriba (`python -m venv .venv`).
2. **Revisa los perfiles** en `profiles/` y duplica `quick.json` para crear tu propio preset (`profiles/custom.json`). Asegúrate de declarar `target`, `engines` y `description`.
3. **Ejecuta el CLI** con el perfil: `python core/scanner.py profiles/custom.json --engines nmap,httpx`.
   - El runner invocará los motores predefinidos y escribirá `scanner-report.json` con stdout/stderr y códigos de retorno.
4. **Revisa el reporte** (JSON) y, si quieres, pásalo por `ui/app.py` para listar el perfil ejecutado y confirmar el motor.
5. **Empaqueta o expórtalo** usando `packaging/build-pyinstaller.sh` para obtener un binario listo (`dist/scanner-suite`).
   - Puedes agregar tu propio perfil en `profiles/` antes de empaquetar para que el .exe ya lo incluya.
6. **Comparte el output** exportando `scanner-report.json` como Markdown/HTML (liberado en la próxima fase) o subiendo el ZIP de `dist/scanner-suite` en los releases.

## Contribuye
Revisa `docs/ROADMAP.md` para ver las fases y `CONTRIBUTING.md` para flujos de issues/PR. Mantén el enfoque en pruebas autorizadas, documenta cada escena y agrega referencias oficiales.
