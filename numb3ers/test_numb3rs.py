from numb3rs import validate
import pytest


def test_succeed():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
    assert validate("123.0.0.123") == True


def test_fail():
    assert validate("-127.0.0.1") == False
    assert validate("666.0.0.0") == False
    assert validate("1.2.3") == False
    assert validate("123.666.666.666") == False

