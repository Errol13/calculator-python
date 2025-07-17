import pytest
from classes.calculator import Calculator


@pytest.fixture
def calc():
    return Calculator()

# Shared invalid input pairs used for multiple operations
invalid_inputs = [
    ('a', 2),
    ({}, 1),
    ([], -1),
    (-12, {}),
    (None, 'a')
]
#Test 1: Equivalence class combinations in addition
@pytest.mark.parametrize("a,b,expected",[
    (1,1,2),
    (4,-1,3),
    (0,0,0),
    (4.2, 3, pytest.approx(7.2)),
    (3.1, 4.5, pytest.approx(7.6))
])
def test_add(calc,a, b, expected):
    assert calc.addition(a,b) == expected

@pytest.mark.parametrize("a, b", invalid_inputs)
def test_add_invalid_param(calc,a,b):
    with pytest.raises(TypeError):
        calc.addition(a,b)


#Test 2: Equivalence class combinations in subtraction
@pytest.mark.parametrize("a,b,expected",[
    (2,1,1),
    (-2,-2,0),
    (5,-7,12),
    (-7,-5,-2),
    (0,0,0),
    (3.2, 4, pytest.approx(-0.8)),
    (3.5, 2.2, pytest.approx(1.3))
])
def test_subtract_param(calc,a,b,expected):
    assert calc.subtract(a,b) == expected

@pytest.mark.parametrize("a, b", invalid_inputs)
def test_subtract_invalid_param(calc,a,b):
    with pytest.raises(TypeError):
        calc.subtract(a,b)


#Test 3: Equivalence class combinations in multiplication 
@pytest.mark.parametrize("a,b, expected",[
    (2,2,4),
    (-2,-5, 10),
    (-7, 2,-14),
    (0,0,0),
    (4.2, -1, pytest.approx(-4.2)),
    (3.2, 2.2, pytest.approx(7.04))
])
def test_multiply_param(calc,a,b,expected):
    assert calc.multiply(a,b) == expected

@pytest.mark.parametrize("a, b", invalid_inputs)
def test_multiply_invalid_param(calc,a,b):
    with pytest.raises(TypeError):
        calc.multiply(a,b)

#Test 4 : Equivalence class combinations  in division
@pytest.mark.parametrize("a,b,expected",[
    (0,4,0),
    (6,-2, -3),
    (4,2,2),
    (7,2, pytest.approx(3.5)),
    (0.5,0.5, pytest.approx(1)),
    (5.6, 4.7, pytest.approx(1.19))
])
def test_divide_param(calc,a,b,expected):
    assert calc.divide(a,b) == expected

@pytest.mark.parametrize("a, b", invalid_inputs)
def test_divide_invalid_param(calc,a,b):
    with pytest.raises(TypeError):
        calc.divide(a,b)

# Test 5: Division when the divisor is zero
def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(3,0)