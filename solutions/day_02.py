import time
from utils import get_input

def part_0(input):
    position = [0, 0]
    for line in input:
        direction, value = line.split()
        operator, index = 1, 0
        if direction == 'up':
            operator = -1
        elif direction != 'forward':
            index = 1
        position[index] += operator * int(value)
    return position[0] * position[1]

def part_1(input):
    position = [0, 0]
    aim = 0
    for line in input:
        direction, value = line.split()
        value = int(value)
        if direction == 'up':
            aim -= value
        elif direction == 'down':
            aim += value
        else:
            position[0] += value
            position[1] += value * aim
    return position[0] * position[1]


if __name__ == "__main__":
    start_time = time.time()
    input = get_input()
    print(part_0(input))
    print(part_1(input))
    print(f'\nExecution time: {time.time() - start_time} s')