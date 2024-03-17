from bank import value


def test_value_0():
    assert value("hello") == 0
    assert value("Hello") == 0

def test_value_20():
    assert value("hey") == 20
    assert value("Hey") == 20
    assert value("holla") == 20
    assert value("Holla") == 20

def test_value_100():
    assert value("ollah") == 100
    assert value("Ollah") == 100
    assert value("what's up?") == 100
    assert value("What's up?") == 100
    assert value("good day.") == 100
    assert value("Good day.") == 100

