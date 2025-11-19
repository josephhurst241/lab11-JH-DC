#https://github.com/josephhurst241/lab11-JH-DC.git
# Partner 1: Joseph Hurst
# Partner 2: David Chen
import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
         output = add(3, 4)
         self.assertEqual(output, 7)

    def test_subtract(self):
        output = sub(5, 3)
        self.assertEqual(output, 2)

    def test_multiply(self): # 3 assertions
        output = mul(7, 8)
        self.assertEqual(output, 56)

    def test_divide(self): # 3 assertions
        output = div(49, 7)
        self.assertEqual(output, 7)

    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(5,0)

    def test_logarithm(self): # 3 assertions
        output = logarithm(2, 16)
        self.assertEqual(output, 4)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            logarithm(7, 0)
    
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self):
         output = hypotenuse(3, 4)
         self.assertEqual(output, 5)

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-4)


if __name__ == "__main__":
    unittest.main()