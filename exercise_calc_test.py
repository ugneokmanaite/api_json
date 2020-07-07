#create a test for below file using pytest
# import math
#
# def find_sqrt(num):
#     return math.sqrt(num)
#
# def find_ceil(num):
#     return math.ceil(num)

import pytest

import unittest

from exercise_calc import *

class Calc_Test(unittest.TestCase):

    simple_calc= Calc()

    def test_sqrt(self):
        # we are testing if sqrt of 64 is 8
        self.assertEqual(self.simple_calc.sqrt(64),8)

    def test_ceil(self):
        self.assertEqual(self.simple_calc.ceil(14.6),15)

# test by entering -m pytest into terminal  to test
