from bank import value

def test_hello():
    assert value("hello man") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("how are you") == 20
    assert value("How") == 20

def test_other():
    assert value("good morning") == 100
    assert value("What's happening?") == 100