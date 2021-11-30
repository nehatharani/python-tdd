#Excersie 1: 
'''
TDD - 
Using Python with a Test Driven approach, create a simple String Calculator

'''

import unittest
from string_calculator import add
from string_calculator_exceptions import ValueTooSmallError
from utility_functions import check_constraints


class TestUtilityFunctions(unittest.TestCase):
    def test_check_constraints(self):
        self.assertEqual(check_constraints(''), True)
        self.assertEqual(check_constraints(None), True)
        self.assertEqual(check_constraints('1,2,3'), False)
        self.assertEqual(check_constraints('None'), False)
        

class TestStringCalculator(unittest.TestCase):

    def test_adds_number_seperated_by_comma(self):
        self.assertEqual(add("5,10"),15)
        self.assertEqual(add("1,2"),3)
        self.assertEqual(add("10,4"),14)
        self.assertEqual(add("3,3,1"),7)

    def test_string_calculator_empty_str_returns_zero(self):
        self.assertEqual(add(''),0)
        self.assertEqual(add(None),0)

    def test_single_number_should_return_itself(self):
        self.assertEqual(add("5"),5)
        self.assertEqual(add("10"),10)

    def test_supports_different_delimiters(self):
        self.assertEqual(add("1 2 3", " "),6)
        self.assertEqual(add("1neha2neha3", "neha"),6)
        self.assertEqual(add("10\n20\n5", "\n"),35)
    
    def test_raise_error_for_negative_num(self):
        with self.assertRaises(ValueTooSmallError):
            add("-1,-2,-2")

    def test_ignores_nums_greater_than_100(self):
        self.assertEqual(add("5,100,1"),106)
        self.assertEqual(add("101"),0)
        self.assertEqual(add("7000,99,1,3,450"),103)




        



