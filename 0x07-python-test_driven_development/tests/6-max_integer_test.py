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

    def test_m_b_is_string(self):
        with self.assertRaises(TypeError, msg="m_b must be a list"):
            matrix_mul([[1, 2], [3, 4]], 'not a list')

    def test_m_b_is_list_of_ints(self):
        with self.assertRaises(TypeError, msg="m_b must be a list of lists"):
            matrix_mul([[1, 2], [3, 4]], [[1], [2]])

    def test_m_b_is_empty(self):
        with self.assertRaises(ValueError, msg="m_b can’t be empty"):
            matrix_mul([[1, 2], [3, 4]], [])

    def test_m_b_contains_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            matrix_mul([[1, 2], [3, 4]], [[1, 'a'], [2, 'b']])

    def test_m_b_rows_of_different_sizes(self):
        with self.assertRaises(TypeError):
            matrix_mul([[1, 2], [3, 4]], [[1, 2], [2]])

    def test_missing_argument(self):
        with self.assertRaises(TypeError):
            matrix_mul([[1, 2], [3, 4]])

    def test_missing_arguments(self):
        with self.assertRaises(TypeError):
            matrix_mul()

if __name__ == '__main__':
    unittest.main()

