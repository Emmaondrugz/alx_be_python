# 1. Import the Necessary Modules
import unittest
from simple_calculator import SimpleCalculator


# 2. Define a Test Class (inherits from unittest.TestCase)
class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        """Set up test fixtures - runs before each test method."""
        self.calc = SimpleCalculator()
    
    # 3. Write Test Methods for each operation
    
    def test_addition(self):
        """Test the add method."""
        # 4. Use assertions to verify results
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(3, 3), 0)
    
    def test_multiply(self):
        """Test the multiply method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
    
    def test_divide(self):
        """Test the divide method with normal operation."""
        # Test normal division
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(9, 3), 3)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
    
    def test_divide_by_zero(self):
        """Test the divide method with division by zero (edge case)."""
        # Test edge case: division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(0, 0))


# 5. Running Your Tests
if __name__ == '__main__':
    unittest.main()