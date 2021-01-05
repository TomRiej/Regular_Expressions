import re

def chal1(text):
    patterns = "ab+"
    if re.search(patterns, text):
        return "Found"
    else:
        return "Not found"

def chal2(text):
    patterns = "ab?"
    if re.search(patterns, text):
        return "Found"
    else:
        return "Not found"

def chal3(text):
    patterns = "abbb"
    if re.search(patterns, text):
        return "Found"
    else:
        return "Not found"

def chal4(text):
    patterns = "abbb?"
    if re.search(patterns, text):
        return "Found"
    else:
        return "Not found"


tests = ["a", "aaa", "ab", "ac", "abb", "abbb", "abbbbb", "abbbc", "accbbbba"]
funcs = [chal1, chal2, chal3, chal4]

for func in funcs:
    print(str(func))
    for t in tests:
        print(t, func(t))
    