from store import coupon_calculations
import unittest


class FunctionTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(8, 5, 10), 9, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(8, 5, 15), 9, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(8, 5, 20), 9, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(8, 10, 10), 4, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(8, 10, 15), 4, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(8, 10, 20), 4, 0)

    def test_price_ten_to_thirty(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(20, 5, 10), 22, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(20, 5, 15), 23, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(20, 5, 20), 23, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(20, 10, 10), 15, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(20, 10, 15), 16, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(20, 10, 20), 16, 0)

    def test_price_thirty_to_fifty(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 5, 10), 50, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 5, 15), 52, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 5, 20), 52, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 10, 10), 45, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 10, 15), 47, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(45, 10, 20), 47, 0)

    def test_price_above_fifty(self):
        self.assertAlmostEqual(coupon_calculations.calculate_price(60, 5, 10), 64, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(60, 5, 15), 54, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(60, 5, 20), 55, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(60, 10, 10), 60, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(60, 10, 15), 61, 0)
        self.assertAlmostEqual(coupon_calculations.calculate_price(60, 10, 20), 62, 0)


if __name__ == '__main__':
    unittest.main()
