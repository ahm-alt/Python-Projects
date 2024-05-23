from fuel import convert, gauge
import pytest

def test_convert_valueerror():
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("8/2")

def test_convert_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_convert():
    assert convert("1/4") == 25
    assert convert("1/3") == 33

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(23) == "23%"
    assert gauge(99) == "F"

