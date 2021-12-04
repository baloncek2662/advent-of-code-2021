import time
import copy
from utils import get_input

def part_0(input):
    ones_count = get_ones_count(input)
    gamma_rate = ['0'] * len(input[0])
    epsilon_rate = ['0'] * len(input[0])
    for i in range(0, len(input[0])):
        if ones_count[i] > len(input) / 2:
            gamma_rate[i] = '1'
        else:
            epsilon_rate[i] = '1'
    return int(''.join(gamma_rate), 2) * int(''.join(epsilon_rate), 2)


def part_1(input):
    oxygen_rating = copy.deepcopy(input)
    co2_rating = copy.deepcopy(input)
    pos = 0
    while len(oxygen_rating) > 1:
        new_oxygen_rating = []
        ones_count = get_ones_count(oxygen_rating)
        one_is_most_common = ones_count[pos] >= len(oxygen_rating) / 2
        for line in oxygen_rating:
            if line[pos] == "1" and one_is_most_common:
                new_oxygen_rating.append(line)
            elif line[pos] == "0" and not one_is_most_common:
                new_oxygen_rating.append(line)
        oxygen_rating = new_oxygen_rating
        pos += 1

    pos = 0
    while len(co2_rating) > 1:
        new_co2_rating = []
        ones_count = get_ones_count(co2_rating)
        one_is_most_common = ones_count[pos] >= len(co2_rating) / 2
        for line in co2_rating:
            if line[pos] == "1" and not one_is_most_common:
                new_co2_rating.append(line)
            elif line[pos] == "0" and one_is_most_common:
                new_co2_rating.append(line)
        co2_rating = new_co2_rating
        pos += 1
    return int(''.join(oxygen_rating), 2) * int(''.join(co2_rating), 2)

def get_ones_count(input):
    input_line_len = len(input[0])
    ones_count = [0] * input_line_len
    for line in input:
        for i in range(0, input_line_len):
            if line[i] == '1':
                ones_count[i] += 1
    return ones_count


if __name__ == '__main__':
    start_time = time.time()
    input = get_input()
    print(part_0(input))
    print(part_1(input))
    print(f'\nExecution time: {time.time() - start_time} s')