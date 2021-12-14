import sys

import math_func
import pytest

#@pytest.mark.string
#@pytest.mark.skip(reason=" do not run number add test")
@pytest.mark.skipif(sys.version_info<(3,3),reason=" do not run number add test")

def test_add():
    assert  math_func.add(7,3)==11
    assert  math_func.add(7) == 9

def test_product():
    assert  math_func.product(5,5)==25
    assert  math_func.product(5)==10
    assert  math_func.product(7)==14

def test_add_strings():
    result=math_func.add('Hello','World');
    assert result=='Hello World'
    assert 'ads' not in result