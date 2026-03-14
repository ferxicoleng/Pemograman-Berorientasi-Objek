import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(2,3),5)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5,3),2)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(4,3),12)

    def test_divide(self):
        self.assertEqual(calculator.divide(10,2),5)

    def test_exponent(self):
        self.assertEqual(calculator.exponent(2,3),8)

if __name__ == "__main__":
    unittest.main()