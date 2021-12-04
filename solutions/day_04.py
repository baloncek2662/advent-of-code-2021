import time
from utils import get_input
from copy import deepcopy

def part_0(numbers, boards):
    for number in numbers:
        # each board
        for i in range(0, len(boards)):
            # each row
            for j in range(0, len(boards[i])):
                #each row element
                winner_column = True
                for k in range(0, len(boards[i][j])):
                    if boards[i][j][k] == number:
                        boards[i][j][k] = 'x'
                        # check if all elements in column or row are now crossed out
                        for row_index in range(0, len(boards[i])):
                            if boards[i][row_index][k] != 'x':
                                winner_column = False
                                break
                        if winner_column or boards[i][j] == ['x'] * len(boards[i][j]):
                            unmarked_sum = 0
                            for row in boards[i]:
                                for col in row:
                                    if col != 'x':
                                        unmarked_sum += int(col)
                            return unmarked_sum * int(number)
    return -1 # no winner found


def part_1(numbers, boards):
    res = 0
    skip_indexes = []
    for number in numbers:
        # each board
        for i in range(0, len(boards)):
            if i in skip_indexes:
                continue
            # each row
            for j in range(0, len(boards[i])):
                #each row element
                winner_column = True
                for k in range(0, len(boards[i][j])):
                    if boards[i][j][k] == number:
                        boards[i][j][k] = 'x'
                        # check if all elements in column are now crossed out
                        for row_index in range(0, len(boards[i])):
                            if boards[i][row_index][k] != 'x':
                                winner_column = False
                                break
                        if winner_column or boards[i][j] == ['x'] * len(boards[i][j]):
                            unmarked_sum = 0
                            for row in boards[i]:
                                for col in row:
                                    if col != 'x':
                                        unmarked_sum += int(col)
                            res = unmarked_sum * int(number)
                            skip_indexes.append(i)
    return res

def parse_input(input):
    numbers = input[0].split(',')
    boards = []
    board = []
    for i in range(2, len(input)):
        line = input[i]
        if line == '':
            if board != []:
                boards.append(board)
            board = []
            continue
        board.append([el for el in line.split(' ') if el != ''])
    return numbers, boards


if __name__ == "__main__":
    start_time = time.time()
    numbers, boards = parse_input(get_input())
    print(part_0(numbers, deepcopy(boards)))
    print(part_1(numbers, boards))
    print(f'\nExecution time: {time.time() - start_time} s')