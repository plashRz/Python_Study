from fnMaker import hello


def  test_hello():
    assert hello("Thomas") == "Hello, Thomas"
    assert hello("John") == "Hello, John"

def test_hello_default():
    assert hello() == "Hello, World"