import numpy as np


def read_data(filename):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    data = []
    for line in lines:
        line_split = line.split()
        line_split = [int(l) for l in line_split]
        data.append(line_split)
    return data


def process_sequence(sequence, data=[]):
    sequence_array = np.array(sequence)
    data.append(sequence_array)
    sequence_diff = np.diff(sequence_array)
    # If all elements are 0, return data
    if np.all(sequence_diff == 0):
        return data
    else:
        return process_sequence(sequence_diff, data)


def extrapolate_sequence(sequence_array: np.ndarray):
    value = 0
    for seq in sequence_array[::-1]:
        value += seq[-1]
    return value

def extrapolate_sequence_backwards(sequence_array: np.ndarray):
    value = 0
    mem = sequence_array[-1][0]
    for seq in sequence_array[-2::-1]:
        # print(mem)
        # print(seq)
        mem = seq[0] - mem
        # print(mem)
        # print('---')
        # mem = seq[0]
    return mem


if __name__ == '__main__':
    data = read_data('./input_9.txt')
    final_value = 0
    final_value_backwards = 0
    for sequence in data:
        processed_seq = process_sequence(sequence, data=[])
        extrapolation = extrapolate_sequence(processed_seq)
        extrapolation_backwards = extrapolate_sequence_backwards(processed_seq)
        final_value += extrapolation
        final_value_backwards += extrapolation_backwards
    print(final_value)
    print(final_value_backwards)
