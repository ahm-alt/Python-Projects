from numb3rs import validate

def test_true():
    assert validate("1.0.9.4") == True
    assert validate("6.100.11.22") == True
    assert validate("156.200.99.255") == True
    assert validate("1a1.1.1") == False
    assert validate("255.255.255.255") == True

def test_false():
    assert validate("0.0.0.256") == False
    assert validate("256.0.3.2") == False
    assert validate("23.3.3.") == False
    assert validate("cat") == False
    assert validate("255.199.65.0") == True

def test_3():
    assert validate("1..1.1.1") == False
    assert validate("1.1.1.1.1") == False
    assert validate("140.247.235.144") == True
    assert validate("122") == False
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False
