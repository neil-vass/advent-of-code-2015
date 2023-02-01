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



valid_letters = string.ascii_lowercase

# LOL well I have solved a much harder puzzle than I needed to here
def _find_next_too_complex(fixed_part, rotating_part, original):
    if len(rotating_part) == 0:
        if valid(fixed_part) and fixed_part != original:
            return fixed_part
    else:
        initial_idx = valid_letters.index(rotating_part[0])
        for i in range(len(valid_letters) +1):
            next_letter = valid_letters[(initial_idx+i) % len(valid_letters)]
            valid_password = _find_next(fixed_part + next_letter, rotating_part[1:], original)
            if valid_password:
                return valid_password   
    return None

def _find_next(fixed_part, rotating_part, original):
    if len(rotating_part) == 0:
        if valid(fixed_part) and fixed_part != original:
            return fixed_part
    else:
        # Find it without changing this wheel?
        valid_password = _find_next(fixed_part + rotating_part[0], rotating_part[1:], original)
        if valid_password:
                return valid_password 
        # Nope, start rotating this one.
        initial_idx = valid_letters.index(rotating_part[0])
        for next_letter in valid_letters[initial_idx+1:]:
            valid_password = _find_next(fixed_part + next_letter, (len(rotating_part)-1)*'a', original)
            if valid_password:
                return valid_password   
    return None

def find_next(password):
    return _find_next(fixed_part='', rotating_part=password, original=password)

#--------------------- tests -------------------------#

def test_valid():
    assert not valid('hijklmmn')
    assert not valid('abbceffg')
    assert not valid('abbcegjk')

def test_find_next():
    assert valid('aabbabc')
    assert find_next('aabbaba') == 'aabbabc'
    assert find_next('abcdefgh') == 'abcdffaa'
    assert find_next('ghijklmn') == 'ghjaabcc'


#-----------------------------------------------------#

if __name__ == "__main__":
    new_pass = find_next('<input>')
    new_pass = find_next(new_pass)
    print(new_pass)
