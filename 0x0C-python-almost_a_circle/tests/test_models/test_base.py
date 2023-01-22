#!/usr/bin/python3
"""Module for unittest"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Testcases for Unittesting of class Base"""

    def test_base_auto_id(self):
        """Test of Base() for assigning automatically an ID exists"""
        b1 = Base()
        b2 = Base()
        assert b1.id == 1
        assert b2.id == 2

    def test_base_auto_id_increment(self):
        """Test of Base() for assigning automatically ID + 1 of previous"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        assert b3.id == b2.id + 1

    def test_base_passed_id(self):
        """Test of Base(89) saving the ID passed exists"""
        b1 = Base(89)
        assert b1.id == 89

if __name__ == '__main__':
    unittest.main()
