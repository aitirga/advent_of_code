import numpy as np


def read_input(filename):
    data = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.strip().split())
    return data

def process_pairs(data_pair: list):
    # Process data pair
    data_string: str = data_pair[0]
    data_string = data_string.split(',')
    data_string = [piece.split('-') for piece in data_string]
    # convert to int
    data_string = [[int(piece[0]), int(piece[1])] for piece in data_string]
    #
    pair_1_elements = set(i for i in range(data_string[0][0], data_string[0][1] + 1))
    pair_2_elements = set(i for i in range(data_string[1][0], data_string[1][1] + 1))
    if pair_1_elements >= pair_2_elements or pair_2_elements >= pair_1_elements:
        return 1
    else:
        return 0


def process_pairs_overlap(data_pair: list):
    # Process data pair
    data_string: str = data_pair[0]
    data_string = data_string.split(',')
    data_string = [piece.split('-') for piece in data_string]
    # convert to int
    data_string = [[int(piece[0]), int(piece[1])] for piece in data_string]
    #
    pair_1_elements = set(i for i in range(data_string[0][0], data_string[0][1] + 1))
    pair_2_elements = set(i for i in range(data_string[1][0], data_string[1][1] + 1))
    if len(pair_1_elements & pair_2_elements) > 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    # Process input file
    data = read_input('input_4.dat')
    counter = 0
    for data_pair in data:
        counter += process_pairs(data_pair)
    print(counter)

    counter = 0
    for data_pair in data:
        counter += process_pairs_overlap(data_pair)
    print(counter)
















