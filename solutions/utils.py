import os

def get_input(day):
    if len(str(day)) == 1:
        day = f'0{day}'
    input_list = []
    with open(os.path.join(os.path.dirname(__file__)) + f"/../inputs/day_{day}.txt") as file:
        for val in file.read().split():
            input_list.append(int(val))
    return input_list