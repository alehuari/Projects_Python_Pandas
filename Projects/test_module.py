import unittest
from unittest.mock import patch
from mean_var_std import calculate

class TestCalculator(unittest.TestCase):
    
    @patch('builtins.input', return_value='1 2 3 4 5 6 7 8 9')
    def test_calculate_with_valid_input(self, mock_input):   
        nums = mock_input.return_value.split()        
        if len(nums) == 9:
            result = calculate([int(num) for num in nums])
            expected_result = {
                'mean': 5.0,
                'variance': 6.67,
                'standard_deviation': 2.58,
                'max': 9,
                'min': 1,
                'sum': 45
            }
            self.assertEqual(result, expected_result)
        else:
            self.fail("Invalid number of inputs")
                  
    @patch('builtins.input', return_value='1 2 3 4 5 6 7 8') 
    # Incorrect input with 8 numbers
    def test_calculate_with_invalid_input(self, mock_input):
        nums = mock_input.return_value.split()
        if len(nums) != 9:
            with self.assertRaises(ValueError):
                calculate([int(num) for num in nums])
        else:
            self.fail("Test failed: Unexpected number of inputs")

if __name__ == "__main__":
    unittest.main()