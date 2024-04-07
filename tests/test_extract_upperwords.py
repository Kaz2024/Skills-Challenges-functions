from lib.extract_uppperwords import *

def test_with_empty_string():
    assert extract_uppercase_words ("") == []

def test_with_only_lowercase_words():
    result = extract_uppercase_words ("hello world i am a text") 
    assert result == []

def  test_with_only_one_uppercase_word():
    result = extract_uppercase_words ("hello WORLD")
    assert result == ["WORLD"]

def test_mixed_with_upper_and_lower():
    result = extract_uppercase_words (" am A hello WORLD")
    assert result == ["A", "WORLD"]

def test_return_upper_without_punctation():
    result = extract_uppercase_words ("am A hello WORLD:")
    assert result == ["A", "WORLD"]

def test_mixed_case_words_dont_count_as_uppercase():
    result = extract_uppercase_words ("am A hello WorLD YES")
    assert result == ["A", "YES"]
