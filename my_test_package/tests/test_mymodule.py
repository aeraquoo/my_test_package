from my_test_package.mymodule import *
from nose.tools import assert_equals

class TestMyModule():
    def test_multiply(self):
        threes = [(1,2,2),
                (3,3,9),
                (0.5,6,3)]
        for a,b,c in threes:
            assert_equals(multiply(a,b), c)
    def test_multiplication_table(self):
        table = \
"""4 times 1 is 4
4 times 2 is 8
4 times 3 is 12
4 times 4 is 16"""
        assert_equals(multiplication_table(4), table)
    def test_add(self):
        assert_equals(add(2,3), 5)
