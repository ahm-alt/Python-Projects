from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(8)
    assert jar.capacity == 8
    with pytest.raises(ValueError):
        jar = Jar(-2)
    with pytest.raises(ValueError):
        jar = Jar(2.3)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(10)
    assert jar.size == 12
    with pytest.raises(ValueError):
        jar.deposit(1)



def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(2)
    assert jar.size == 10
    jar.withdraw(10)
    assert jar.size == 0
    with pytest.raises(ValueError):
        jar.withdraw(1)