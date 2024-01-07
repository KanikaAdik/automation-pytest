import pytest

from utils import str_to_int, str_to_bool

"""
def test_yes_is_true():
	result = str_to_nool('yes')
	assert result is True

def test_y_is_true():
	result = str_to_bool('y')
	assert result is True
"""
"""
import pdb
pdb.set_trace()
"""

def test_str_to_int_fails():
        result = str_to_int("14, 44") 
        assert result ==14

def test_str_to_int_decimals():
        result = str_to_int("14.44") 
        assert result ==14

def test_str_to_int_with_integers():
        result = str_to_int(10) 
        assert result ==10




@pytest.mark.parametrize('value',['N', 'no'])
def test_is_false(value):
        result = str_to_bool(value)
        assert result is False

@pytest.mark.parametrize('value',[ 'y','yes',''])
def test_is_true(value):
        result = str_to_bool(value)
        assert result is True

