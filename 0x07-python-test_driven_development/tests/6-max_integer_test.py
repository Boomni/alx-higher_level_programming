import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element_list(self):
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-1]), -1)

    def test_two_elements_list(self):
        self.assertEqual(max_integer([5, 3]), 5)
        self.assertEqual(max_integer([3, 5]), 5)
        self.assertEqual(max_integer([0.3, 0.4]), 0.4)

    def test_three_elements_list(self):
        self.assertEqual(max_integer([5, 3, 8]), 8)
        self.assertEqual(max_integer([5, 8, 3]), 8)
        self.assertEqual(max_integer([8, 5, 3]), 8)

    def test_negative_elements_list(self):
        self.assertEqual(max_integer([5, 3, -8]), 5)
        self.assertEqual(max_integer([-5, 3, 0, -8]), 3)
        self.assertEqual(max_integer([-5, -3, 0, -1 -8]), 0)


if __name__ == '__main__':
    unittest.main()

