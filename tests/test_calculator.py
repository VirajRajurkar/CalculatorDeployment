import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.calculate("add", 1, 1), 2)

    def test_sub(self):
        self.assertEqual(self.calc.calculate("subtract", 2, 1), 1)

    def test_invalidOperation(self):
        self.assertEqual(self.calc.calculate("invalid operation", 2, 1), "Error: Invalid operation")
    
if __name__ == "__main__":
    unittest.main()