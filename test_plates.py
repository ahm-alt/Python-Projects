from plates import is_valid

def test_start():
    assert is_valid("22") == False
    assert is_valid("a2cc") == False
    assert is_valid("Cs50") == True
    assert is_valid("HELLO") == True

def test_no_char():
    assert is_valid("cssssss50") == False
    assert is_valid("c") == False

def test_number():
    assert is_valid("cs50x") == False
    assert is_valid("cs05") == False

def test_punct():
    assert is_valid("cs 50") == False
    assert is_valid("cs05!") == False

