# https://adventofcode.com/2015/day/7
import re
import operator
import numpy as np
from functools import cache


class Circuit:
    bitwise = { 'AND': operator.and_, 'OR': operator.or_, 'LSHIFT': operator.lshift, 'RSHIFT': operator.rshift }

    def bitwise_not(x):
        return ~np.uint16(x)

    def __init__(self):
        self.wires = {}
    
    def load(self, instructions):
        for i in instructions:
            input, target = i.split(' -> ')
            self.wires[target] = input.split()

    @cache
    def _get_val(self, s):
        if s.isdigit():
            return int(s)
        else:
            return self.evaluate(s)

    def evaluate(self, target):
        input = self.wires[target]
        if len(input) == 1:
            return self._get_val(input[0])
        
        if len(input) == 2:
            op = Circuit.bitwise_not
            a = self._get_val(input[1])
            return op(a)

        if len(input) == 3:
            a = self._get_val(input[0])
            op = Circuit.bitwise[input[1]]
            b = self._get_val(input[2])
            return op(a, b)


def fetch_data(path):
    with open(path, 'r') as f:
        for ln in f:
            yield ln.rstrip()

#--------------------- tests -------------------------#

def test_circuit():
    instructions = fetch_data('../sample_data/day07.txt')
    circuit = Circuit()
    circuit.load(instructions)
    assert circuit.evaluate('x') == 123
    assert circuit.evaluate('e') == 507
    
#-----------------------------------------------------#

if __name__ == "__main__":
    instructions = fetch_data('../data/day07.txt')
    circuit = Circuit()
    circuit.load(instructions)
    print(circuit.evaluate('a'))
    # Ran this for part 1, then edited input file to use this answer in part 2.