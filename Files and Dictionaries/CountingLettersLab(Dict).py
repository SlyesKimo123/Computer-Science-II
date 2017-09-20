def countAll(text):
    d = {}
    for letter in text:
        d[letter] = text.count(letter)
    return d
d = countAll("soccer")
print(d)
