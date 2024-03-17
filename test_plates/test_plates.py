from plates import is_valid


def test_first_two_alpha():
    assert is_valid("1234") == False
    assert is_valid("H13") == False
    assert is_valid("!#%&?") == False
    assert is_valid("CS50") == True


def test_length():
    assert is_valid("C") == False
    assert is_valid("TWO") == True
    assert is_valid("Tlll") == True
    assert is_valid("Slaye") == True
    assert is_valid("Slayer") == True
    assert is_valid("Slayer8") == False


def test_no_numbers_in_middle():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False


def test_first_number():
    assert is_valid("AB012") == False
    assert is_valid("AB020") == False


def test_all_alphanumeric():
    assert is_valid("CS50") == True
    assert is_valid("ECTO88") == True
    assert is_valid("CS%&?0") == False
    assert is_valid("PI3.14") == False

