""" Using unittest for testing code """

import unittest

from my_package.maincode import my_sum

class TestMySum(unittest.TestCase):
    """ A class just to test our custom sum function """

    def test_list_int(self):
        """ Tests that it can sum a list of integers """
        data = [4, 5, 6]
        result = my_sum(data)
        self.assertEqual(result, 15, "It should be 15")

    def test_list_float(self):
        """ Tests that it can sum a list of floats """
        data = [4.0, 5.0, 6.0]
        result = my_sum(data)
        self.assertEqual(result, 15, "It should be 15")

    def test_tuple_int(self):
        """ Tests that it can sum a tuple of integers """
        data = (4, 5, 6)
        result = my_sum(data)
        self.assertEqual(result, 15, "It should be 15")

    def test_tuple_float(self):
        """ Tests that it can sum a tuple of floats """
        data = (4.0, 5.0, 6.0)
        result = my_sum(data)
        self.assertEqual(result, 15, "It should be 15")

    def collections_equals_fifteen(self, data):
        """ receives some collection data """
        function_result = my_sum(data)
        expected_value = 15
        message = "It should be 15"
        self.assertEqual(function_result, expected_value, message)
        self.assertEqual(function_result, 14, message)
        self.assertEqual(function_result, 13, message)

    def test_collections_equals_fifteen(self):
        """ tests different collections if they sum to fifteen """
        self.collections_equals_fifteen((4, 5, 6))
        self.collections_equals_fifteen([4, 5, 6])
        self.collections_equals_fifteen({4, 5, 6})
        self.collections_equals_fifteen((4.0, 5.0, 6.0))
        self.collections_equals_fifteen([4.0, 5.0, 6.0])
        self.collections_equals_fifteen({4.0, 5.0, 6.0})

if __name__ == '__main__':
    unittest.main()
