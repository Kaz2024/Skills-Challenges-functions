from lib.reading_time_estimation import *

def test_reading_200_words_is_a_minute():
    text = "".join(["word" for i in range(0,200)])
    result = reading_time_estimation(text)        
    assert result == 1.0

def test_400_words_reading_estmation():
    text = "".join(["word" for i in range(0,400)])
    result = reading_time_estimation(text)
    assert result  == 2.0

def test_reading_time_for_300_words():
    text = "".join(["word" for i in range(0,300)])
    result = reading_time_estimation(text)   
    assert result == 1.5


