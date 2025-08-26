from validateipv4 import validate


def test_alphabet():
    assert validate("cat") ==  False


def test_validate():
    assert validate("1.2.3.4") == True
def test_false():
    assert validate("277.2.3.4") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False

def test_trailing_zero():
    assert validate("192.168.001.1") == False
    assert validate("192.168.01.1") == False
