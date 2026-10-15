from decimal import Decimal

import pytest

from cuentas.dividir import dividir


def test_divide_en_partes_iguales():
    assert dividir(Decimal("90"), 3) == [Decimal("30.00")] * 3


def test_suma_la_propina():
    assert dividir(Decimal("100"), 2, Decimal("10")) == [Decimal("55.00")] * 2


def test_no_pierde_el_centavo_que_sobra():
    partes = dividir(Decimal("100"), 3)

    assert partes == [Decimal("33.34"), Decimal("33.33"), Decimal("33.33")]
    assert sum(partes) == Decimal("100.00")


@pytest.mark.parametrize(
    ("total", "personas", "propina", "cobrado"),
    [
        ("100", 3, "0", "100.00"),
        ("100", 3, "10", "110.00"),
        ("87.45", 4, "15", "100.57"),
        ("0.01", 2, "0", "0.01"),
        ("1000", 7, "18", "1180.00"),
    ],
)
def test_la_suma_siempre_es_el_total_con_propina(total, personas, propina, cobrado):
    partes = dividir(Decimal(total), personas, Decimal(propina))

    assert len(partes) == personas
    assert sum(partes) == Decimal(cobrado)
    assert max(partes) - min(partes) <= Decimal("0.01")


@pytest.mark.parametrize(
    ("total", "personas", "propina", "mensaje"),
    [
        ("-1", 2, "0", "El total no puede ser negativo"),
        ("100", 0, "0", "Debe haber al menos una persona"),
        ("100", 2, "-5", "La propina debe estar entre 0 y 100"),
        ("100", 2, "101", "La propina debe estar entre 0 y 100"),
    ],
)
def test_rechaza_datos_invalidos(total, personas, propina, mensaje):
    with pytest.raises(ValueError, match=mensaje):
        dividir(Decimal(total), personas, Decimal(propina))
