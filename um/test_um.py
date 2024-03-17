from um import count
import pytest


def test_succeed():
    assert count("um") == 1
    assert count("um?") == 1

def test_succeed_sentence():
    assert count("Um, thanks for the album.") == 1

def test_succeed_more_than_one():
    assert count("Um, thanks, um...") == 2

