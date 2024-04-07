def extract_uppercase_words(text):
    words = text.split()
    uppercase_words=[word for word in words if word.isupper()]
    filtered_uppercase_words = []
    for word in uppercase_words:
        filtered_letter=[letter for letter in word if letter.isalpha()]
        filtered_words="".join(filtered_letter)
        filtered_uppercase_words.append(filtered_words)
    return filtered_uppercase_words



