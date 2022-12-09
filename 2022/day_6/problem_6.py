import numpy as np


def read_data(data_path):
    with open(data_path, 'r') as f:
        lines = f.readlines()
    return lines[0]

def process_data(data: str, n_batch = 4) -> int:
    batches = [data[i:i + n_batch] for i in range(len(data) - n_batch + 1)]
    for batch_id, batch in enumerate(batches):
        batch_set = set(batch)
        if len(batch_set) == n_batch:
            return batch_id + n_batch


if __name__ == '__main__':
    data: str = read_data('./input_6.dat')
    solution = process_data(data)
    solution_batch = process_data(data, n_batch=14)

