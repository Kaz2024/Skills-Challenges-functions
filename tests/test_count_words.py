from lib.count_words import *
"""
A function called count_words that takes a string as an argument and returns the number of words in that string.

"""

def test_string_return_empty_string():
    result = count_words("")
    assert result == 0

def test_count_a_single_word():
    result = count_words("hello world")
    assert result == 2