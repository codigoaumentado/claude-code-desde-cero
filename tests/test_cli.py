from cuentas.__main__ import main


def test_imprime_cada_parte_y_el_total(capsys):
    main(["90", "3"])

    salida = capsys.readouterr().out
    assert "Persona 3: $30.00" in salida
    assert "Total cobrado: $90.00" in salida
