def make_snippet(text):
    texts = text.split()
    if len(texts)>5:
        return " ".join(texts[:5])+ " ..."
    else: 
        return text