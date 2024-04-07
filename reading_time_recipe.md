# Reading time Estimation function Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

# as a user 
# So that i can manage my time
# I want to see an estimation of reading time for a text, assuming that I can read 200 words a minute

```python
# EXAMPLE

# I can read 200 words in 1 minute

def test_200_words_per_minute(text):
    # parameter:
    #    text: a string representing human readable time
    # return 
    #    a float representing a reading time
    pass 

```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given a text of 200 words
It returns will return 1
"""
reading_time_estimation(...200...):
=> 1.0

"""
Given a text of 400 words
It returns will return 2
"""
reading_time_estimation(...400...):
=> 2.0


"""
Given a text of 300 words
It returns  a reading time of 1.5
"""
reading_time_estimation(...300...):
=> 1.5

"""
Given an empty string
It raise an error
"""
reading_time_estimation(""):
=> raises error, "Can't estimate reading time for an empty text."


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```

Ensure all test function names are unique, otherwise pytest will ignore them!
