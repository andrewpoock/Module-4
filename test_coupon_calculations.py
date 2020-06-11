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



if __name__ == '__main__':
    unittest.main()
