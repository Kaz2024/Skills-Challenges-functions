from lib.check_grammar import *

def test_sentence_grammar_with_captial_letter_and_fullstop():
    result = check_sentence_grammar("Hello, today is Monday.")
    assert result == True 

def test_no_full_stop_and_capital_lettet():
    result = check_sentence_grammar("Hello, today is Monday")
    assert result == False