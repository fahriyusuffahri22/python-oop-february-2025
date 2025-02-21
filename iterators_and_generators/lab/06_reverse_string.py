def reverse_text(text):
    i = len(text)
    while i > 0:
        i -=1
        yield text[i]
