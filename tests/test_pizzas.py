import unittest
from unittest.mock import patch

import pizzas


class MyTestCase(unittest.TestCase):
    @patch('builtins.print')
    def test_something(self, print_mock):
        orders = [["1","2"], ["3", "4"]]
        pizzas.prepare_pizzas(orders)
        self.assertEqual(print_mock.call_count, len(orders)+2)


if __name__ == '__main__':
    unittest.main()
