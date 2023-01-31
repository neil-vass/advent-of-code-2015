# https://adventofcode.com/2015/day/8
import ast
import re

def fetch_data(path):
    with open(path, 'r') as f:
        for ln in f:
            yield ln.rstrip()

def code_and_chars(s):
    return len(s), len(ast.literal_eval(s))

def find_diff(data):
    pairs = (code_and_chars(s) for s in data)
    return sum(code-chars for code, chars in pairs)

def code_and_encode(s):
    return len(s), len(re.sub(r'["\\]', lambda m: '\\' + m[0], s)) +2

def find_encoded_diff(data):
    pairs = (code_and_encode(s) for s in data)
    return sum(encode-code for code, encode in pairs)

#--------------------- tests -------------------------#

def test_code_and_chars():
    data = fetch_data('sample_data/day08.txt')
    assert code_and_chars(next(data)) == (2, 0)
    assert code_and_chars(next(data)) == (5, 3)
    assert code_and_chars(next(data)) == (10, 7)
    assert code_and_chars(next(data)) == (6, 1)

def test_find_diff():
    data = fetch_data('sample_data/day08.txt')
    assert find_diff(data) == 12

def test_code_and_encode():
    data = fetch_data('sample_data/day08.txt')
    assert code_and_encode(next(data)) == (2, 6)
    assert code_and_encode(next(data)) == (5, 9)
    assert code_and_encode(next(data)) == (10, 16)
    assert code_and_encode(next(data)) == (6, 11)

def test_find_encoded_diff():
    data = fetch_data('sample_data/day08.txt')
    assert find_encoded_diff(data) == 19

#-----------------------------------------------------#

if __name__ == "__main__":
    data = fetch_data('data/day08.txt')
    print(find_encoded_diff(data))
