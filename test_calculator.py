import unittest
import math
from calculator import square_root, factorial, natural_log, power_function

class TestCalculatorFunctions(unittest.TestCase):

    # Test Square Root (√x)
    def test_square_root_positive(self):
        self.assertAlmostEqual(square_root(25), 5.0)
    
    def test_square_root_zero(self):
        self.assertAlmostEqual(square_root(0), 0.0)

    def test_square_root_negative_raises_error(self):
        with self.assertRaises(ValueError):
            square_root(-1)

    # Test Factorial (!x)
    def test_factorial_valid(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_factorial_negative_raises_error(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    # Test Natural Logarithm (ln(x))
    def test_natural_log_positive(self):
        self.assertAlmostEqual(natural_log(math.e), 1.0)
    
    def test_natural_log_one(self):
        self.assertAlmostEqual(natural_log(1), 0.0)

    def test_natural_log_zero_or_negative_raises_error(self):
        with self.assertRaises(ValueError):
            natural_log(0)
        with self.assertRaises(ValueError):
            natural_log(-1)

    # Test Power Function (x^b)
    def test_power_function(self):
        self.assertAlmostEqual(power_function(2, 3), 8.0)
        self.assertAlmostEqual(power_function(5, 0), 1.0)
        self.assertAlmostEqual(power_function(4, 0.5), 2.0)

if __name__ == '__main__':
    unittest.main()