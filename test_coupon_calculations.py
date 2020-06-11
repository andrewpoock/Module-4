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



if __name__ == '__main__':
    unittest.main()
