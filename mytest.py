import pytest
import mycalc


def test_check_it_return_addition():
    res = mycalc.add(2, 3)
    assert res == 5
   
def test_check_it_return_substraction():
    res = mycalc.subtract(9, 5)
    assert res == 6
    
def test_check_it_return_multiply():
    res = mycalc.multiply(2, 5)
    assert res == 10
 