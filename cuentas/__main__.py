"""Uso: python -m cuentas TOTAL PERSONAS [--propina PCT]"""

import argparse
from decimal import Decimal

from cuentas.dividir import dividir


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="cuentas")
    parser.add_argument("total", type=Decimal)
    parser.add_argument("personas", type=int)
    parser.add_argument("--propina", type=Decimal, default=Decimal("0"))
    args = parser.parse_args(argv)

    partes = dividir(args.total, args.personas, args.propina)
    for i, parte in enumerate(partes, start=1):
        print(f"Persona {i}: ${parte}")
    print(f"Total cobrado: ${sum(partes)}")


if __name__ == "__main__":
    main()
