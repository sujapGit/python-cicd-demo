from app.calculator import add, substract, multiply, divide


# --  Add --

def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -3) == -4


# -- Substract --

def test_substract():
    assert substract(1, 4) == -3


def test_substract_negative_numbers():
    assert substract(-2, -1) == -1


# -- Multiply --

def test_multiply():
    assert multiply(1, 3) == 3


def test_multiply_withzero():
    assert multiply(3, 0) == 0


# -- Divide --

def test_divide():
    assert divide(4, 2) == 2


def test_divide_withzero():
    try:
        divide(10, 0)
        assert False, "Cannot divide by zero"
    except ValueError:
        assert True
