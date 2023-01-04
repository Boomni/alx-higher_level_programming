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

    def test_validation(self):
        # Test that matrix_mul() raises the correct exceptions for invalid input
        with self.assertRaises(TypeError, msg='m_a must be a list'):
            matrix_mul('invalid', [[1, 2], [3, 4]])
        with self.assertRaises(TypeError, msg='m_a must be a list of lists'):
            matrix_mul([1, 2], [[1, 2], [3, 4]])
        with self.assertRaises(ValueError, msg='m_a can\'t be empty'):
            matrix_mul([], [[1, 2], [3, 4]])
        with self.assertRaises(TypeError, msg='m_a should contain only integers or floats'):
            matrix_mul([['invalid']], [[1, 2], [3, 4]])
        with self.assertRaises(TypeError, msg='each row of m_a must be of the same size'):
            matrix_mul([[1, 2], [3]], [[1, 2], [3, 4]])
        with self.assertRaises(TypeError, msg='m_b must be a list'):
            matrix_mul([[1, 2], [3, 4]], 'invalid')
        with self.assertRaises(TypeError, msg='m_b must be a list of lists'):
            matrix_mul([[1, 2], [3, 4]], [1, 2])
        with self.assertRaises(ValueError, msg='m_b can\'t be empty'):
            matrix_mul([[1, 2], [3, 4]], [])
        with self.assertRaises(TypeError, msg='m_b should contain only integers or floats'):
            matrix_mul([[1, 2], [3, 4]], [['invalid']])
        with self.assertRaises(TypeError, msg='each row of m_b must be of the same size'):
            matrix_mul([[1, 2], [3, 4]], [[1, 2], [3]])
        with self.assertRaises(ValueError, msg='m_a and m_b can\'t be multiplied'):
            matrix_mul([[1, 2], [3, 4]], [[1], [2]])

if __name__ == '__main__':
    unittest.main()

