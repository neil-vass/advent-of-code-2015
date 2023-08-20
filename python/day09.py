# https://adventofcode.com/2015/day/9
import re
import itertools

def fetch_data(path):
    with open(path, 'r') as f:
        for ln in f:
            m = re.match(r'(\w+) to (\w+) = (\d+)', ln)
            yield m[1], m[2], int(m[3])

class RoutePlanner:
    def __init__(self, data):
        self.cities = set()
        self.distances = {}
        for a, b, dist in data:
            self.cities.add(a)
            self.cities.add(b)
            self.distances[(a,b)] = dist
            self.distances[(b,a)] = dist
    
    def choose_route(self, criteria):
        shortest_so_far = None
        for route in itertools.permutations(self.cities):
            dist = 0
            for i in range(len(route) -1):
                dist += self.distances[(route[i], route[i+1])]
            if shortest_so_far is None:
                shortest_so_far = dist
            else:
                shortest_so_far = criteria(shortest_so_far, dist)
        return shortest_so_far


#--------------------- tests -------------------------#

def test_basics():
    data = fetch_data('sample_data/day09.txt')
    assert next(data) == ('London', 'Dublin', 464)

def test_shortest():
    data = fetch_data('sample_data/day09.txt')
    planner = RoutePlanner(data)
    assert planner.choose_route(min) == 605

def test_longest():
    data = fetch_data('sample_data/day09.txt')
    planner = RoutePlanner(data)
    assert planner.choose_route(max) == 982

#-----------------------------------------------------#

if __name__ == "__main__":
    data = fetch_data('data/day09.txt')
    planner = RoutePlanner(data)
    print(planner.choose_route(max))
