# test_cities.py

import unittest
from city_functions import city_country  # Import the function to be tested

class TestCityCountry(unittest.TestCase):
    
    def test_city_country(self):
        # Call the function with 'Santiago' and 'Chile'
        result = city_country('Santiago', 'Chile')
        
        # Verify that the function returns the expected string
        self.assertEqual(result, 'Santiago, Chile')  # Check if the result matches 'Santiago, Chile'

if __name__ == '__main__':
    unittest.main()
