# cuentas

Calculadora para dividir la cuenta de un grupo, con propina.
Python 3.11, sin dependencias en producción.

## Comandos
- Tests y cobertura: `.venv/bin/pytest` (falla si la cobertura baja de 90 %)
- Lint: `.venv/bin/ruff check .`
- Formato: `.venv/bin/ruff format .`
- Probar a mano: `.venv/bin/python -m cuentas 100 3 --propina 10`

## Reglas de negocio
- El dinero siempre es `Decimal`, nunca `float`.
- Se redondea al centavo con `ROUND_HALF_UP`.
- La suma de las partes es exactamente el total con propina.
  Los centavos que sobran los pagan las primeras personas, uno cada una.
- Propina entre 0 y 100 %. Total no negativo. Al menos una persona.

## Forma de trabajar
- Antes de cambiar una regla, escribe el test que falla.
- Errores con `ValueError` y mensaje en español.
- Commits en inglés: `type(scope): description`.
- Nunca leas ni subas `.env`.
