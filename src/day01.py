# https://adventofcode.com/2015/day/2

def fetch_data(path):
    with open(path, 'r') as f:
        return f.readline().rstrip()

def find_floor(data):
    return data.count('(') - data.count(')')

def pos_for_basement(data):
    floor = 0
    for pos, c in enumerate(data, 1):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return pos


#--------------------- tests -------------------------#

def test_find_floor():
    assert find_floor('(())') == 0
    assert find_floor(')())())') == -3

#-----------------------------------------------------#

if __name__ == "__main__":
    data = fetch_data('data/day01.txt')
    print(pos_for_basement(data))
