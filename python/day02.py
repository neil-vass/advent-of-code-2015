# https://adventofcode.com/2015/day/2

def fetch_data(path):
    with open(path, 'r') as f:
        for ln in f:
            yield [int(n) for n in ln.split('x')]

def wrap(l, w, h):
    side_areas = (l*w, w*h, h*l)
    return sum(2*a for a in side_areas) + min(side_areas)

def ribbon(l, w, h):
    dimensions = sorted([l, w, h])
    return 2*dimensions[0] + 2*dimensions[1] + l*w*h


#--------------------- tests -------------------------#

def test_fetch_data():
    data = fetch_data('../sample_data/day02.txt')
    assert next(data) == [2, 3, 4]

def test_wrap():
    assert wrap(2, 3, 4) == 58
    assert wrap(1, 1, 10) == 43

def test_total_wrapping():
    data = fetch_data('../sample_data/day02.txt')
    assert sum(wrap(*present) for present in data) == (58 + 43)

def test_ribbon():
    assert ribbon(2, 3, 4) == 34


#-----------------------------------------------------#

if __name__ == "__main__":
    data = fetch_data('../data/day02.txt')
    print(sum(ribbon(*present) for present in data))
