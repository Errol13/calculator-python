import pytest
from calculator import addition

#Test 1: Add all possible combinations in addition

@pytest.mark.parametrize("a,b,expected",[
    (1,1,2),
    (1,-1,0),
    (0,0,0),
])

def test_add(a, b, expected):
    assert addition(a,b) == expected

@pytest.mark.parametrize("a, b",[
    ('a', 2),
    ({}, 1),
    ([], -1),
    (-12, {})
])

def test_add_invalid_param(a,b):
    with pytest.raises(TypeError):
        addition(a,b)
