import time
from utils import get_input
from copy import deepcopy

def part_0(input):
    for i in range(0, 80):
        for j in range(0, len(input)):
            input[j] -= 1
            if input[j] < 0:
                input[j] = 6
                input.append(8)
    return len(input)


def part_1(input):
    fish_per_day = [0] * 9
    for i in input:
        fish_per_day[i] += 1
    for i in range(0, 256):
        new_fish_per_day = [0] * 9
        # shift left for days 0-7
        for j in range(1, 9):
            new_fish_per_day[j-1] = fish_per_day[j]
        # shift from day 0 to day 6 and add 1 new fish to day 8
        new_fish_per_day[6] += fish_per_day[0]
        new_fish_per_day[8] += fish_per_day[0]

        fish_per_day = new_fish_per_day

    return sum(fish_per_day)


if __name__ == "__main__":
    start_time = time.time()
    input = [int(el) for el in get_input()[0].split(',')]
    print(part_0(deepcopy(input)))
    print(part_1(input))
    print(f'\nExecution time: {time.time() - start_time} s')