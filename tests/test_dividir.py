from decimal import Decimal

from cuentas.dividir import dividir


def test_divide_en_partes_iguales():
    assert dividir(Decimal("90"), 3) == [Decimal("30.00")] * 3


def test_suma_la_propina():
    assert dividir(Decimal("100"), 2, Decimal("10")) == [Decimal("55.00")] * 2
