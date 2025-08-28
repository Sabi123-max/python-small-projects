from birth_check import minutes_in_words
from datetime import date

def test_today():
    today = date.today()
    assert minutes_in_words(today) == "Zero minutes"



