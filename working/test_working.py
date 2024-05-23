from working import convert
import pytest

def test_single():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11 AM to 1 AM") == "11:00 to 01:00"
    with pytest.raises(ValueError):
        convert("12 AM to 2")
def test_multy():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:23 AM to 1:40 AM") == "00:23 to 01:40"
    with pytest.raises(ValueError):
        convert("12:60 AM to 2 PM")
    with pytest.raises(ValueError):
        convert("12:00 AM  2 PM")
    with pytest.raises(ValueError):
        convert("13:40 AM to 2:32 PM")
def test_mix():
    assert convert("12:23 AM to 1 AM") == "00:23 to 01:00"
    assert convert("12 AM to 12 PM")
    with pytest.raises(ValueError):
        convert("12:60 AM to 2:ff PM")
    with pytest.raises(ValueError):
        convert("12_ss AM to :ff PM")
