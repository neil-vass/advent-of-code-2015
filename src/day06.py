# https://adventofcode.com/2015/day/6
import numpy as np
from collections import namedtuple
import re

Instruction = namedtuple("Instruction", "action x1 y1 x2 y2")

class Grid:
    def __init__(self):
        self.lights = np.zeros((1000, 1000), dtype=int)

    def lit(self):
        return np.count_nonzero(self.lights)
    
    def brightness(self):
        return np.sum(self.lights)

    def run(self, instruction):
        match instruction.action:
            case 'turn on':
                self.lights[instruction.x1:instruction.x2+1, instruction.y1:instruction.y2+1] = True
            case 'turn off':
                self.lights[instruction.x1:instruction.x2+1, instruction.y1:instruction.y2+1] = False
            case 'toggle':
                self.lights[instruction.x1:instruction.x2+1, instruction.y1:instruction.y2+1] = np.logical_not(
                    self.lights[instruction.x1:instruction.x2+1, instruction.y1:instruction.y2+1])

    def run_v2(self, instruction):
        match instruction.action:
            case 'turn on':
                self.lights[instruction.x1:instruction.x2+1, instruction.y1:instruction.y2+1] += 1
            case 'turn off':
                self.lights[instruction.x1:instruction.x2+1, instruction.y1:instruction.y2+1] = \
                    np.maximum(0, self.lights[instruction.x1:instruction.x2+1, instruction.y1:instruction.y2+1] -1)
            case 'toggle':
                self.lights[instruction.x1:instruction.x2+1, instruction.y1:instruction.y2+1] += 2

def fetch_data(path):
    with open(path, 'r') as f:
        for ln in f:
            m = re.match(r'(.+) (\d+),(\d+) through (\d+),(\d+)', ln)
            yield Instruction(m[1], int(m[2]), int(m[3]), int(m[4]), int(m[5]))


#--------------------- tests -------------------------#

def test_fetch_data():
    data = fetch_data('../sample_data/day06.txt')
    assert next(data) == Instruction('turn on', 0,0, 999,999)

def test_run_instructions():
    instruction = fetch_data('../sample_data/day06.txt')
    grid = Grid()
    assert grid.lit() == 0

    # Turn on all
    grid.run(next(instruction))
    assert grid.lit() == 1000000

    # Toggle first line
    grid.run(next(instruction))
    assert grid.lit() == 999000

    # Turn off 4
    grid.run(next(instruction))
    assert grid.lit() == 998996

def test_run_instructions():
    instruction = fetch_data('../sample_data/day06.txt')
    grid = Grid()
    assert grid.brightness() == 0
    grid.run_v2(Instruction('turn on', 0,0, 0,0))
    assert grid.brightness() == 1
    grid.run_v2(Instruction('toggle', 0,0, 999,999))
    assert grid.brightness() == 2000001

#-----------------------------------------------------#

if __name__ == "__main__":
    grid = Grid()
    for instruction in fetch_data('../data/day06.txt'):
        grid.run_v2(instruction)

    print(grid.brightness())
    # 14747699 is too low