from lib.make_snippet import *

#given a string and return a string 

def test_string_return_a_string():
    result = make_snippet("one two three four")
    assert result == "one two three four"

# return the string if it is longer than 5 char

def test_return_the_first_5_char_of_string():
    result = make_snippet("one two three four five")
    assert result == ("one two three four five six")

# string is great than 5 return the first 5 word and "..."
def test_return_the_first_5_char_of_string():
    result = make_snippet ("one two three four five six")
    assert result == "one two three four five ..."
