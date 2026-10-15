import subprocess
import sys

from cuentas.__main__ import main


def test_imprime_cada_parte_y_el_total(capsys):
    main(["100", "3"])

    salida = capsys.readouterr().out
    assert "Persona 1: $33.34" in salida
    assert "Persona 3: $33.33" in salida
    assert "Total cobrado: $100.00" in salida


def test_se_ejecuta_como_modulo():
    resultado = subprocess.run(
        [sys.executable, "-m", "cuentas", "90", "3", "--propina", "10"],
        capture_output=True,
        text=True,
        check=True,
    )

    assert "Total cobrado: $99.00" in resultado.stdout
