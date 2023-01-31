# https://adventofcode.com/2015/day/6
import numpy as np

def fetch_data(path):
    with open(path, 'r') as f:
        for ln in f:
            yield ln

class Grid:
    def __init__(self):
        self.lights = np.zeros((1000, 1000), dtype=bool)

    def lit(self):
        return np.count_nonzero(self.lights)
        
#--------------------- tests -------------------------#

def test_grid():
    grid = Grid()
    assert grid.lit() == 0

#-----------------------------------------------------#

if __name__ == "__main__":
    data = fetch_data('data/day06.txt')
    print('Hello, World!')