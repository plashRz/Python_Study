from square_it import sq
import pytest

# def main():
#     test_sq()

def test_possq():
    assert sq(2) == 4
    assert sq(4) == 16

def test_negsq():
    assert sq(-3) == 9
    assert sq(-1) == 1
    assert sq(-2) == 4

def test_0sq():
    assert sq(0) == 0

def test_strsq():
    with pytest.raises(TypeError):
        sq("abc")          

# if __name__ == "__main__":
#     main()

# testing, printing, main fn creation, exception handling all addressed via pytest 3rd party library