# Proceso de releases (Face 3)

1. Etiqueta la versión (`v0.1.0`, etc.) y crea un **draft release** en GitHub.
2. La acción `Face 3 — Release automation` (ver `.github/workflows/face3-release.yml`) se dispara con el evento `release.published`: ejecuta `packaging/build-pyinstaller.sh`, empaqueta `dist/scanner-suite` y lo sube automáticamente como asset.
3. Incluye en la descripción del release los comandos clave (`python core/scanner.py ...`) y qué perfiles se actualizan.
4. Si quieres un checksum adicional, puedes correr `sha256sum dist/scanner-suite` en el entorno local antes de publicar.
