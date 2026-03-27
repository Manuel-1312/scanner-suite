import asyncio
import json
from pathlib import Path
from typing import List, Dict

import typer

app = typer.Typer(help="Orquesta varios motores de escaneo (nmap, masscan, httpx).")

SUPPORTED_ENGINES = {
    "nmap": "nmap -sC -sV",
    "masscan": "masscan -p1-1024",
    "httpx": "httpx -status-code",
}


async def run_command(cmd: str) -> Dict[str, str]:
    """Simula ejecutar un comando y recoge salida."""
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
    engines: List[str] = typer.Option(
        ["nmap"], help="Motores permitidos: nmap, masscan, httpx"),
    output: Path = typer.Option("scanner-report.json", help="Ruta del reporte JSON"),
):
    """Ejecuta un perfil contra los motores elegidos."""
    data = json.loads(profile.read_text(encoding="utf-8"))
    host = data.get("target")
    tasks = []
    for engine in engines:
        if engine not in SUPPORTED_ENGINES:
            typer.echo(f"Motor desconocido: {engine}")
            raise typer.Exit(code=1)
        cmd = SUPPORTED_ENGINES[engine] + f" {host}"
        tasks.append(run_command(cmd))
    results = asyncio.run(asyncio.gather(*tasks))
    report = {
        "profile": profile.name,
        "target": host,
        "engines": engines,
        "results": results,
    }
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    typer.echo(f"Reporte guardado en {output}")


if __name__ == "__main__":
    app()
