# Roadmap de Scanner Suite (Visión Face 1→4)

## Face 1 — MVP básico
- Wraps Python para nmap, masscan, httpx (core/scanner.py).
- Prefabricados (`profiles/`) Quick, Deep, Web Audit.
- Interfaz mínima (ui/placeholder) que permite lanzar perfiles guardados.
- Documentación: README, docs/ROADMAP.md, docs/PACKAGING.md.
- Entradas de configuración (packaging/scripts) para preparar binarios.

## Face 2 — Calidad y flujos
- Tests unitarios para parsers `reports/` y validadores de perfiles.
- Templates de contribución (`CONTRIBUTING.md`, `.github/ISSUE_TEMPLATE`, `.github/PULL_REQUEST_TEMPLATE`).
- Checklist de calidad (Face 3) y scripts para validar configuraciones.

## Face 3 — Automatización y packaging
- Workflows GitHub para lint/format + tests.
- Scripts `packaging/build-pyinstaller.sh` o `packaging/build.ps1`.
- Documentación de lanzamiento y release notes integradas en `docs/RELEASES.md`.

## Face 4 — Comunidad y adopción
- Cheatsheets (`docs/CHEAT_SHEETS.md`) y `COMMUNITY.md`.
- Integraciones opcionales (plugins, API partner).
- Ejemplos de uso real (lab-notes, exploits, guías en docs/).
