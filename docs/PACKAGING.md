# Empaquetado y distribución

Scanner Suite terminará convertido en binarios (Windows, macOS, Linux) usando PyInstaller y/o Briefcase:

1. Crea un virtualenv y activa el entorno.
2. Instala dependencias en `requirements.txt` (presentes en raíz) y `core` + `ui`.
3. Usa el script `packaging/build-pyinstaller.sh` para generar un solo ejecutable:
   ```bash
   pyinstaller --onefile --name "scanner-suite" core/scanner.py
   ```
4. Para la interfaz, usa `tkinter` (mobile) o una pequeña web empaquetada (streamlit + PyInstaller).
5. Empaqueta assets: `profiles/*.json`, `docs/`, `ui/assets/` mediante `--add-data` de PyInstaller.
6. Genera `dist/` + `releases/releases.json` con metadatos mínimos (versión, fecha, checksum) para respaldar la app pública.
