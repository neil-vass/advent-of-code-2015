# https://adventofcode.com/2015/day/10
import re

def look_and_say(s):
    return ''.join(str(len(m[0])) + m[1] for m in re.finditer(r'(.)\1*', s))
    
#--------------------- tests -------------------------#

def test_look_and_say():
    assert look_and_say('1') == '11'
    assert look_and_say('11') == '21'

#-----------------------------------------------------#

if __name__ == "__main__":
    s = '<input>'
    for _ in range(50):
        s = look_and_say(s)
    print(len(s))
