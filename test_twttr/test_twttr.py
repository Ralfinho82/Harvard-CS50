from twttr import shorten

def test_shorten_vowels_only():
    assert shorten("aeiouAEIOU") == ""

def test_shorten_names():
    assert shorten("Ralf") == "Rlf"
    assert shorten("Melanie") == "Mln"

def test_shorten_capital_letters():
    assert shorten("GAS") == "GS"

def test_shorten_numbers_letters():
    assert shorten("90Bleiziffer82") == "90Blzffr82"

def test_shorten_punctuation():
    assert shorten(".,;:!?") == ".,;:!?"