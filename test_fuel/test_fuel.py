from fuel import convert, gauge
import pytest

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_value():
    with pytest.raises(ValueError):
        convert("5/4")

def test_convert():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("3/3") == 100
    assert convert("1/100") == 1


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(99) == "F"
    assert gauge(60) == "60%"
    assert gauge(89) == "89%"

