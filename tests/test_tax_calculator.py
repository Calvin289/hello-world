import sys
import unittest
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from tax_calculator import STANDARD_DEDUCTION, calculate_tax


class TaxCalculatorTestCase(unittest.TestCase):
    def test_zero_income(self):
        result = calculate_tax(0)
        self.assertEqual(result.taxable_income, 0)
        self.assertEqual(result.tax_due, 0)
        self.assertEqual(result.net_income, 0)

    def test_typical_annual_income(self):
        annual_income = 120_000
        result = calculate_tax(annual_income)
        self.assertAlmostEqual(result.taxable_income, annual_income - STANDARD_DEDUCTION)
        self.assertAlmostEqual(result.tax_due, 3480.0)
        self.assertAlmostEqual(result.net_income, annual_income - 3480.0)
        self.assertAlmostEqual(result.tax_rate, 0.10)
        self.assertAlmostEqual(result.quick_deduction, 2520.0)

    def test_deductions_lower_taxable_income(self):
        annual_income = 300_000
        deductions = 50_000
        result = calculate_tax(annual_income, deductions=deductions)
        expected_taxable = max(0, annual_income - STANDARD_DEDUCTION - deductions)
        self.assertAlmostEqual(result.taxable_income, expected_taxable)
        self.assertAlmostEqual(result.tax_rate, 0.20)
        self.assertAlmostEqual(result.quick_deduction, 16920.0)
        self.assertAlmostEqual(result.tax_due, 21080.0)

    def test_high_income_bracket(self):
        annual_income = 1_200_000
        result = calculate_tax(annual_income)
        expected_taxable = annual_income - STANDARD_DEDUCTION
        self.assertAlmostEqual(result.taxable_income, expected_taxable)
        # For manual check: taxable income 1,140,000 -> highest bracket 45% quick deduction 181,920
        expected_tax = expected_taxable * 0.45 - 181_920
        self.assertAlmostEqual(result.tax_due, expected_tax)

    def test_negative_income_raises(self):
        with self.assertRaises(ValueError):
            calculate_tax(-1)

    def test_negative_deductions_raise(self):
        with self.assertRaises(ValueError):
            calculate_tax(100_000, deductions=-1)


if __name__ == "__main__":
    unittest.main()
