from working import convert
import pytest


def test_value_fail_more_then_12h():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")

def test_value_fail_more_then_60m():
    with pytest.raises(ValueError):
        convert("13:61 AM to 5:00 PM")

def test_value_fail_omit():
    with pytest.raises(ValueError):
        convert("9 AM5 PM")

def test_succeed():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

