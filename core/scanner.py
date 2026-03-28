import asyncio
import json
from pathlib import Path
from typing import List, Dict
import logging

import typer
from core.config import load_config

app = typer.Typer(help="Orquesta motores profesionales con logging y configuración centralizada.")
logger = logging.getLogger("scanner-suite")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s %(message)s"))
logger.addHandler(handler)

CONFIG = load_config()
ENGINES = CONFIG.get("engines", {})
REPORT = CONFIG.get("report", {})
REPORT_PATH = Path(REPORT.get("output", "scanner-report.json"))
REPORT_FORMAT = REPORT.get("format", "json")


def build_command(engine: str, target: str) -> str:
    template = ENGINES.get(engine, {}).get("command")
    if not template:
        raise ValueError(f"Motor desconocido: {engine}")
    return f"{template} {target}"


def serialize_report(report: Dict) -> None:
    if REPORT_FORMAT == "json":
        REPORT_PATH.write_text(json.dumps(report, indent=2), encoding="utf-8")
    else:
        REPORT_PATH.write_text(str(report), encoding="utf-8")


async def run_command(cmd: str) -> Dict[str, str]:
    process = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await process.communicate()
    return {
        "command": cmd,
        "stdout": stdout.decode(errors="ignore").strip(),
        "stderr": stderr.decode(errors="ignore").strip(),
        "return_code": process.returncode,
    }


@app.command()
def scan(
    profile: Path = typer.Argument(..., exists=True, dir_okay=False, readable=True),
    engines: List[str] = typer.Option(["nmap"], help="Motores definidos en config/scanners.yaml"),
    output: Path = typer.Option(REPORT_PATH, help="Ruta base del reporte"),
):
    data = json.loads(profile.read_text(encoding="utf-8"))
    target = data.get("target")
    logger.info("Iniciando scan para %s con motores %s", target, engines)
    tasks = [run_command(build_command(engine, target)) for engine in engines]
    results = asyncio.run(asyncio.gather(*tasks))
    report = {"profile": profile.name, "target": target, "engines": engines, "results": results}
    serialize_report(report)
    logger.info("Reporte guardado en %s", output)
    typer.echo(f"Reporte guardado en {output}")


if __name__ == "__main__":
    app()
