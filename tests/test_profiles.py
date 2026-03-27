import json
from pathlib import Path

def test_profiles_have_required_fields():
    profiles = list(Path('profiles').glob('*.json'))
    assert profiles, "No se encontraron perfiles definidos"
    for profile in profiles:
        data = json.loads(profile.read_text())
        assert 'target' in data, f"Falta 'target' en {profile.name}"
        assert 'engines' in data and isinstance(data['engines'], list) and data['engines'], (
            f"'engines' debe ser lista no vacía en {profile.name}"
        )
        assert all(engine in ('nmap', 'masscan', 'httpx', 'nuclei') for engine in data['engines']), (
            f"Motor no soportado en {profile.name}: {data['engines']}"
        )
