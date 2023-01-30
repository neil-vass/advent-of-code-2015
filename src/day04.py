# https://adventofcode.com/2015/day/4
import hashlib

def find_hash(key, zeroes=5):
    n = 0
    leading = '0' * zeroes
    while True:
        s = f'{key}{n}'.encode('utf-8')
        if hashlib.md5(s).hexdigest().startswith(leading):
            return n
        n += 1

#--------------------- tests -------------------------#

def test_generate_md5():
    assert find_hash('abcdef') == 609043
    assert find_hash('pqrstuv') == 1048970

#-----------------------------------------------------#

if __name__ == "__main__":
    print(find_hash('key', zeroes=6))
