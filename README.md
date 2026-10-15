# claude-code-desde-cero

Proyecto de ejemplo del video **"Claude Code desde cero"** del canal [Código Aumentado](https://www.youtube.com/@codigoaumentado).

Una calculadora para dividir la cuenta de un grupo, con propina. Es pequeña a propósito: sirve para practicar el flujo completo de Claude Code (explorar, planificar, implementar con tests y verificar).

## Requisitos
- Python 3.11 o superior

## Uso
```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-dev.txt
.venv/bin/pytest
.venv/bin/python -m cuentas 100 3 --propina 10
```
