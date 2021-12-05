import time
from utils import get_input

def part_0(input):
    coordinates = get_coordinates(input)
    grid_len = get_grid_len(coordinates)
    grid = [[0] * grid_len for _ in range(grid_len)]
    for line in coordinates:
        # vertical line
        if line[0] == line[2]:
            if line[1] > line[3]:
                line[3] += line[1]
                line[1] = line[3] - line[1]
                line[3] -= line[1]
            for row in range(line[1], line[3]+1):
                grid[row][line[0]] += 1
        # horizontal line
        elif line[1] == line[3]:
            # swap if second is larger than 1st
            if line[0] > line[2]:
                line[2] += line[0]
                line[0] = line[2] - line[0]
                line[2] -= line[0]
            for col in range(line[0], line[2]+1):
                grid[line[1]][col] += 1
    res = 0
    for row in grid:
        for col in row:
            if col > 1:
                res += 1
    return res

def part_1(input):
    coordinates = get_coordinates(input)
    grid_len = get_grid_len(coordinates)
    grid = [[0] * grid_len for _ in range(grid_len)]
    for line in coordinates:
        # vertical line
        if line[0] == line[2]:
            if line[1] > line[3]:
                swap_line(line)
            for row in range(line[1], line[3]+1):
                grid[row][line[0]] += 1
        # horizontal line
        elif line[1] == line[3]:
            # swap if second is larger than 1st
            if line[0] > line[2]:
                swap_line(line)
            for col in range(line[0], line[2]+1):
                grid[line[1]][col] += 1
        # diagonal line
        else:
            steps = abs(line[2]-line[0])+1
            if line[0] < line[2] and line[1] < line[3]:
                for i in range(0, steps):
                    grid[line[1]+i][line[0]+i] += 1
            elif line[0] < line[2] and line[1] > line[3]:
                for i in range(0, steps):
                    grid[line[1]-i][line[0]+i] += 1
            elif line[0] > line[2] and line[1] < line[3]:
                for i in range(0, steps):
                    grid[line[1]+i][line[0]-i] += 1
            elif line[0] > line[2] and line[1] > line[3]:
                for i in range(0, steps):
                    grid[line[1]-i][line[0]-i] += 1
    res = 0
    for row in grid:
        for col in row:
            if col > 1:
                res += 1
    return res


def get_coordinates(input):
    # coordinates:
    # [0]...x_start [1]...y_start
    # [2]...x_end   [3]...y_end
    coordinates = []
    for line in input:
        von, zu = [el.split(',') for el in line.split(' -> ')]
        von = [int(el) for el in von]
        zu = [int(el) for el in zu]
        coordinates.append(von + zu)
    return coordinates

def get_grid_len(coordinates):
    max_len = 0
    for l in coordinates:
        l = [el for el in l]
        if max(l) > max_len:
            max_len = max(l)
    return max_len + 1

def swap_line(line):
    line[2] += line[0]
    line[0] = line[2] - line[0]
    line[2] -= line[0]
    line[3] += line[1]
    line[1] = line[3] - line[1]
    line[3] -= line[1]
    return line

if __name__ == "__main__":
    start_time = time.time()
    print(part_0(get_input()))
    print(part_1(get_input()))
    print(f'\nExecution time: {time.time() - start_time} s')