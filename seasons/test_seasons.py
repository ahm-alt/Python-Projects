from seasons import convert
import pytest

def test_1():
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("January 1, 1999")
    assert convert("2005-02-24") == "nine million, one hundred seventy-two thousand, eight hundred minutes"

