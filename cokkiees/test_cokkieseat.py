from cokkieseat import Jar

import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    assert Jar(5).capacity == 5

def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.deposit(20)

def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3
    with pytest.raises(ValueError):
        jar.withdraw(10)