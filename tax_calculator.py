"""Simple personal income tax calculator for China's comprehensive income system.

Usage examples:
    python tax_calculator.py --income 120000
    python tax_calculator.py --monthly --income 15000 --social-insurance 2000 --deductions 12000

The calculator follows the tax brackets enacted in 2019 for comprehensive income
(personal wages, remuneration, etc.). It subtracts the standard deduction of
60,000 RMB per year and allows optional additional deductions such as social
insurance contributions or special deductions.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import List, Tuple

# Annual tax brackets for comprehensive income (after deductions)
# Each tuple: upper bound, rate, quick deduction
BRACKETS: List[Tuple[float, float, float]] = [
    (36000, 0.03, 0),
    (144000, 0.10, 2520),
    (300000, 0.20, 16920),
    (420000, 0.25, 31920),
    (660000, 0.30, 52920),
    (960000, 0.35, 85920),
    (float("inf"), 0.45, 181920),
]

STANDARD_DEDUCTION = 60000


@dataclass
class TaxResult:
    taxable_income: float
    tax_rate: float
    quick_deduction: float
    tax_due: float
    net_income: float


def calculate_tax(annual_income: float, *, deductions: float = 0.0) -> TaxResult:
    """Calculate annual tax for comprehensive income.

    Args:
        annual_income: Gross annual income before tax.
        deductions: Additional deductible amount beyond the standard deduction.

    Returns:
        TaxResult summarizing the calculation.
    """

    if annual_income < 0:
        raise ValueError("Annual income cannot be negative")
    if deductions < 0:
        raise ValueError("Deductions cannot be negative")

    taxable_income = max(0.0, annual_income - STANDARD_DEDUCTION - deductions)

    for upper, rate, quick in BRACKETS:
        if taxable_income <= upper:
            tax_due = max(taxable_income * rate - quick, 0.0)
            net_income = annual_income - tax_due
            return TaxResult(
                taxable_income=taxable_income,
                tax_rate=rate,
                quick_deduction=quick,
                tax_due=tax_due,
                net_income=net_income,
            )

    # Should never reach here because the last bracket upper bound is infinity.
    raise RuntimeError("Failed to find applicable tax bracket")


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="China personal income tax calculator")
    parser.add_argument(
        "--income",
        type=float,
        required=True,
        help="Income amount. Interpret as monthly income when --monthly is used, otherwise annual income.",
    )
    parser.add_argument(
        "--deductions",
        type=float,
        default=0.0,
        help="Additional deductible amount besides social insurance and the standard deduction (annual).",
    )
    parser.add_argument(
        "--social-insurance",
        type=float,
        default=0.0,
        help="Total annual social insurance and housing fund contributions. If --monthly is provided, treat this as monthly and it will be annualized.",
    )
    parser.add_argument(
        "--monthly",
        action="store_true",
        help="Interpret the provided income and social-insurance as monthly amounts.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_arguments()

    multiplier = 12 if args.monthly else 1
    annual_income = args.income * multiplier
    annual_social = args.social_insurance * multiplier

    result = calculate_tax(
        annual_income,
        deductions=args.deductions + annual_social,
    )

    if args.monthly:
        print("Monthly mode (values shown in RMB):")
        print(f"  Gross monthly income: {args.income:,.2f}")
        print(f"  Monthly social insurance: {args.social_insurance:,.2f}")
        print(f"  Monthly additional deductions: {args.deductions / 12:,.2f}")
        print(f"  Monthly taxable income: {result.taxable_income / 12:,.2f}")
        print(f"  Monthly tax due: {result.tax_due / 12:,.2f}")
        print(f"  Monthly net income: {result.net_income / 12:,.2f}")
    else:
        print("Annual mode (values shown in RMB):")
        print(f"  Gross annual income: {annual_income:,.2f}")
        print(f"  Annual deductions (incl. social insurance): {args.deductions + annual_social:,.2f}")
        print(f"  Taxable income: {result.taxable_income:,.2f}")
        print(f"  Tax rate: {result.tax_rate * 100:.0f}%")
        print(f"  Quick deduction: {result.quick_deduction:,.2f}")
        print(f"  Tax due: {result.tax_due:,.2f}")
        print(f"  Net income: {result.net_income:,.2f}")


if __name__ == "__main__":
    main()
