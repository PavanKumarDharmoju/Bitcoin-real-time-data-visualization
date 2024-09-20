import unittest
from utils import get_current_price, get_historical_data

class TestUtils(unittest.TestCase):
    def test_get_current_price(self):
        price = get_current_price('USD')
        self.assertIsInstance(price, str)  # Ensure it returns a valid price string

    def test_get_historical_data(self):
        data = get_historical_data('2021-01-01', '2021-02-01', 'USD')
        self.assertIsInstance(data, dict)  # Ensure it returns a valid dictionary of historical prices

if __name__ == '__main__':
    unittest.main()
