"""Reparte la cuenta de un grupo, con propina, sin perder centavos."""

from decimal import ROUND_HALF_UP, Decimal

CENTAVO = Decimal("0.01")


def dividir(
    total: Decimal, personas: int, propina_pct: Decimal = Decimal("0")
) -> list[Decimal]:
    """Devuelve lo que paga cada persona; la suma es exacta al centavo."""
    if total < 0:
        raise ValueError("El total no puede ser negativo")
    if personas < 1:
        raise ValueError("Debe haber al menos una persona")
    if not 0 <= propina_pct <= 100:
        raise ValueError("La propina debe estar entre 0 y 100")

    con_propina = (total * (1 + propina_pct / 100)).quantize(CENTAVO, ROUND_HALF_UP)
    centavos = int(con_propina / CENTAVO)
    base, sobrante = divmod(centavos, personas)
    # Los centavos que sobran los pagan las primeras personas, uno cada una.
    return [(base + (1 if i < sobrante else 0)) * CENTAVO for i in range(personas)]
