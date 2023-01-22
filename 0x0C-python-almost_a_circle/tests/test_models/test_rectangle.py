#!/usr/bin/python3
"""Module for unittest"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Testcases for Unittesting of class Base"""

    def test_rectangle_auto_id(self):
        """Test of Base() for assigning automatically an ID exists"""
        r1 = Rectangle(1, 2)
        r2 = Rectangle(5, 6)
        assert r1.id == r2.id - 1

if __name__ == '__main__':
    unittest.main()
