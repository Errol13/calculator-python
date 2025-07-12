import pytest
import calculator

#Test 1: Add all possible combinations in addition
@pytest.mark.parametrize("a,b,expected",[
    (1,1,2),
    (4,-1,3),
    (0,0,0),
])
def test_add(a, b, expected):
    assert calculator.addition(a,b) == expected
@pytest.mark.parametrize("a, b",[
    ('a', 2),
    ({}, 1),
    ([], -1),
    (-12, {})
])
def test_add_invalid_param(a,b):
    with pytest.raises(TypeError):
        calculator.addition(a,b)


#Test 2: Subtract all possible combinations in subtraction
@pytest.mark.parametrize("a,b,expected",[
    (2,1,1),
    (-2,-2,0),
    (5,-7,12),
    (-7,-5,-2),
    (0,0,0)
])
def test_subtract_param(a,b,expected):
    assert calculator.subtract(a,b) == expected


#Test 3: Multiply each case in multiplication 
@pytest.mark.parametrize("a,b, expected",[
    (2,2,4),
    (-2,-5, 10),
    (-7, 2,-14),
    (0,0,0)
])
def test_multiply_param(a,b,expected):
    assert calculator.multiply(a,b) == expected


#Test 4 : Divide each case in division
@pytest.mark.parametrize("a,b,expected",[
    (0,4,0),
    (6,-2, -3),
    (4,2,2)
])
def test_divide_param(a,b,expected):
    assert calculator.divide(a,b) == expected


# Test 5: Division when the divisor is zero
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculator.divide(3,0)