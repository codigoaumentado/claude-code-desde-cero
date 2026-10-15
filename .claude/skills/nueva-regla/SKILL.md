---
name: nueva-regla
description: Agrega o cambia una regla de negocio de cuentas con el test primero. Úsala cuando pidan una regla nueva de división, propina o redondeo.
---

Regla a implementar: $ARGUMENTS

1. Lee `CLAUDE.md` y `cuentas/dividir.py`.
2. Escribe primero el test en `tests/test_dividir.py`, con valores exactos
   y el caso límite. Confirma que falla con `.venv/bin/pytest -q`.
3. Implementa el cambio mínimo en `cuentas/dividir.py`.
4. Corre `.venv/bin/pytest` y `.venv/bin/ruff check .`:
   todo en verde y cobertura de 90 % o más.
5. Resume en tres líneas: qué cambió, qué test lo prueba
   y qué caso límite cubriste.
