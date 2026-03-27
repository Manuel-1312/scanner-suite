# Scanner Suite — Zenmap+ para profesionales

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)
[![Face Plan](https://img.shields.io/badge/plan-face%201--4-brightgreen)](README.md)

Una plataforma empaquetada (Python + UI ligera) que orquesta los mejores escáneres de red: Nmap, Masscan, httpx, nuclei, dnsx, etc. La idea es darle a un profesional una sola app (CLI + GUI) para seleccionar el motor, configurar presets y exportar informes sin tocar la terminal de cada herramienta.

## ¿Qué incluye la versión inicial (Face 1)?
- `core/`: wrappers de Python que lanzan nmap/masscan/httpx y normalizan la salida a JSON/Markdown.
- `ui/`: prototipo Tkinter + panel de selección de motores y perfiles.
- `profiles/`: presets (`quick`, `deep`, `web-audit`) definidos en JSON.
- `docs/`: visión, fases, empaquetado (PyInstaller) y guías de uso.
- `packaging/`: ejemplos de scripts para construir `.exe`/`.app` y un release-ready entrypoint.

## Vision y objetivos
1. **Scanner orchestration:** mezcla dinámicamente motores, maneja credenciales y enlaza a filtros `nuclei/httpx` para validaciones web.
2. **Interfaz Zenmap-style:** panel lateral con checklist de motores, parámetros, y visor de resultados, con exportación a HTML/Markdown.
3. **Distribución profesional:** empaquetado en PyInstaller + release (binarios multiplataforma) con opciones offline.
4. **Documentación y ética:** guías de scope, permisos, code of conduct y security disclosures en `SECURITY.md`.

## Plan Face (1→4)
- **Face 1 (MVP):** estructura repo, README + docs, wrappers básicos (Nmap/Masscan/httpx), UI mínimo con Typer/Tkinter y `profiles` base.
- **Face 2 (Calidad):** tests, lint, workflows, templates de contribución, flujo de presets.
- **Face 3 (Automatizaciones):** pipeline CI para lint, link-check, packaging (PyInstaller), generador de releases.
- **Face 4 (Community):** docs de difusión, cheat sheets, onboarding, casos y tutoriales cortos.

## Face 2 — Calidad y pruebas
- `tests/test_profiles.py` valida los `profiles/*.json` (target, engines y motors admitidos).
- La acción `Face 2 — Calidad` (en `.github/workflows/face2-quality.yml`) instala dependencies (`requirements-dev.txt`), ejecuta `ruff` y corre `pytest`.
- Para seguir la calidad, ejecuta `python -m pytest` y `ruff check .` antes de abrir PR.

## Cómo arrancar
```bash
python -m venv .venv
pip install -r requirements.txt
python core/scanner.py profiles/quick.json --engines nmap,masscan
```

## Contribuye
Revisa `docs/ROADMAP.md` para ver las fases y `CONTRIBUTING.md` para flujos de issues/PR. Esta app va dirigida a profesionales; mantén el enfoque en pruebas autorizadas y reportes responsables.
