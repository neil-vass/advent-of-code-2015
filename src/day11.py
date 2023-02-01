# https://adventofcode.com/2015/day/11
import re
import string 

def has_straight_of_3(s):
    for i in range(len(s) -2):
        if ord(s[i]) +1 == ord(s[i+1]) == ord(s[i+2]) -1:
            return True
    return False

forbidden ='iol'
def has_no_forbidden_letters(s):
    return re.search(f'[{forbidden}]', s) is None

def has_two_pairs(s):
    return re.search(r'(.)\1.*(.)\2', s) is not None

def valid(password):
    return (has_straight_of_3(password) and
            has_no_forbidden_letters(password) and
            has_two_pairs(password))

def find_next(password):
    stem, last = password[:-1], password[-1]
    last_idx = string.ascii_lowercase.index(last)
    for i in range(1, 26):
        new_password = stem + string.ascii_lowercase[(last_idx+i) % 26]
        if valid(new_password):
            return new_password
    raise Exception('Welp, out of ideas')


#--------------------- tests -------------------------#

def test_valid():
    assert not valid('hijklmmn')
    assert not valid('abbceffg')
    assert not valid('abbcegjk')

def test_find_next():
    assert find_next('abcdefgh') == 'abcdffaa'
    assert find_next('ghijklmn') == 'ghjaabcc'


#-----------------------------------------------------#

if __name__ == "__main__":
    data = fetch_data('data/day11.txt')
    print('Hello, World!')
