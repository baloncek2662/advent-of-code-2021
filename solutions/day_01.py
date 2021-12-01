import time
from utils import get_input

def part_0(input):
    count = 0
    for i in range(1, len(input)):
        if input[i] > input[i-1]:
            count += 1
    return count

def part_1(input):
    count = 0
    for i in range(1, len(input) - 2):
        if input[i] + input[i+1] + input[i+2] > input[i-1] + input[i] + input[i+1]:
            count += 1
    return count


if __name__ == "__main__":
    start_time = time.time()
    input = [int(el) for el in get_input()]
    print(part_0(input))
    print(part_1(input))
    print(f'\nExecution time: {time.time() - start_time} s')