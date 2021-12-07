import time
from utils import get_input
from copy import deepcopy
import sys

def part_0(input):
    min_fuel = sys.maxsize
    for pos in range(0, len(input)):
        fuel = 0
        for el in input:
            fuel += abs(el - pos)
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel

def part_1(input):
    min_fuel = sys.maxsize
    for pos in range(0, len(input)):
        fuel = 0
        for el in input:
            fuel += sum(range(0, abs(el - pos)+1))
        if fuel < min_fuel:
            min_fuel = fuel
    return min_fuel


if __name__ == "__main__":
    start_time = time.time()
    input = [int(el) for el in get_input()[0].split(',')]
    print(part_0(deepcopy(input)))
    print(part_1(input))
    print(f'\nExecution time: {time.time() - start_time} s')