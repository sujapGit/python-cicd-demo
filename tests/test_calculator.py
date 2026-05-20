from app.calculator import add


# --  Add --

def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-1, -3) == -4
