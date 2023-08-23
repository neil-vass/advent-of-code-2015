# https://adventofcode.com/2015/day/5
import re

def fetch_data(path):
    with open(path, 'r') as f:
        for ln in f:
            yield ln.rstrip()

def is_nice_v1(s):
    vowel_count = len(re.findall(r'[aeiou]', s))
    a_letter_appears_twice = re.search(r'(.)\1', s) is not None
    has_no_forbidden_strings = re.search(r'ab|cd|pq|xy', s) is None
    return vowel_count >= 3 and a_letter_appears_twice and has_no_forbidden_strings

def is_nice_v2(s):
    has_2_pairs = re.search(r'(..).*\1', s) is not None
    has_repeat_with_gap = re.search(r'(.).\1', s) is not None
    return has_2_pairs and has_repeat_with_gap

#--------------------- tests -------------------------#

def test_is_nice_v1():
    assert is_nice_v1('ugknbfddgicrmopn')
    assert is_nice_v1('aaa')
    assert not is_nice_v1('jchzalrnumimnmhp') # No double letter
    assert not is_nice_v1('haegwjzuvuyypxyu') # Contains xy
    assert not is_nice_v1('dvszwmarrgswjxmb') # Only one vowel

def test_is_nice_v2():
    assert is_nice_v2('qjhvhtzxzqqjkmpb')
    assert is_nice_v2('xxyxx')
    assert not is_nice_v2('uurcxstgmygtbstg')

#-----------------------------------------------------#

if __name__ == "__main__":
    data = fetch_data('../data/day05.txt')
    print(sum(is_nice_v2(s) for s in data))
