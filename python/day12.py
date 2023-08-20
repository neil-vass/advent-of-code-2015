# https://adventofcode.com/2015/day/12
import re
import json

def fetch_data(path):
    with open(path, 'r') as f:
        return f.readline().rstrip()

def sum_numbers(s):
    return sum(int(n) for n in re.findall(r'(-?\d+)', s))

def _sum_numbers_ignore_red(data):
    total = 0
    values = data if type(data) == list else data.values()
    for v in values:
        if type(data) == dict and v == 'red':
            return 0
        elif type(v) == int:
            total += int(v)
        elif type(v) in (list, dict):
            total += _sum_numbers_ignore_red(v)
    return total

def sum_numbers_ignore_red(s):
    data = json.loads(s)
    return _sum_numbers_ignore_red(data)

#--------------------- tests -------------------------#

def test_sum_numbers():
    assert sum_numbers('{"a":{"b":4},"c":-1}') == 3

def test_sum_numbers_ignore_red():
    assert sum_numbers_ignore_red('[1,{"c":"red","b":2},3]') == 4
    
#-----------------------------------------------------#

if __name__ == "__main__":
    data = fetch_data('data/day12.txt')
    print(sum_numbers_ignore_red(data))