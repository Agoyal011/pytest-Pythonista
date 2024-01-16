import pytest

import main.main as main


def test_divide():
    assert main.divide(5, 2) == 1


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = main.divide(10, 0)
        assert result == False

#     The test has passed meaning it successfully raised zero division error

def test_add_strings():

    assert main.divide("Aniket","Goyal") == "AniketGoyal"
