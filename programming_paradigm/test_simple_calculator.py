import unittest

class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""
    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b
    
    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b
    
    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b
    
    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b


class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()
    
    def test_add(self):
        result = self.calc.add(2, 3)
        self.assertEqual(result, 5)
    
    def test_subtract(self):
        result = self.calc.subtract(10, 5)
        self.assertEqual(result, 5)
    
    def test_multiply(self):
        result = self.calc.multiply(3, 4)
        self.assertEqual(result, 12)
    
    def test_divide(self):
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)
    
    def test_divide_by_zero(self):
        result = self.calc.divide(10, 0)
        self.assertIsNone(result)


