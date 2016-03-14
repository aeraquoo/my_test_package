from my_test_package.mymodule import *
from nose.tools import assert_equals

class TestMyModule():
    def test_multiply(self):
        threes = [(1,2,2),
                (3,3,9),
                (0.5,6,3)]
        for a,b,c in threes:
            assert_equals(multiply(a,b), c)
