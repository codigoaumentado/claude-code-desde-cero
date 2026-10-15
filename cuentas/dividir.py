"""Reparte la cuenta de un grupo, con propina."""

from decimal import ROUND_HALF_UP, Decimal

CENTAVO = Decimal("0.01")


def dividir(
    total: Decimal, personas: int, propina_pct: Decimal = Decimal("0")
) -> list[Decimal]:
    """Devuelve lo que paga cada persona."""
    con_propina = total * (1 + propina_pct / 100)
    parte = (con_propina / personas).quantize(CENTAVO, ROUND_HALF_UP)
    return [parte] * personas
