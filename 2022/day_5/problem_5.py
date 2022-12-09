import numpy as np


def read_data(data_path) -> tuple:
    initial_config = []
    steps = []
    with open(data_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if len(line) == 1:
                continue
            if line[1] == 1:
                continue
            if not 'move' in line:
                processed_line = process_line(line)
                if all([element is None for element in processed_line]):
                    continue
                initial_config.append(processed_line)
            else:
                steps.append(process_step(line))
    # Normalize initial config so each row has the same length
    max_length = max([len(line) for line in initial_config])
    for i in range(len(initial_config)):
        if len(initial_config[i]) < max_length:
            for _ in range(max_length - len(initial_config[i])):
                initial_config[i].append(None)
    initial_config = np.array(initial_config).T
    # Invert initial config
    initial_config = np.flip(initial_config, axis=1)
    # Convert to an ordered list
    initial_config = initial_config.tolist()
    initial_config = [[element for element in row if element is not None] for row in initial_config]
    return initial_config, steps


def process_line(line: str) -> list:
    void_list = []
    is_processed = False
    i = 0
    while not is_processed:
        current_char = line[i]
        if current_char== '[':
            void_list.append(line[i + 1])
            i += 4
        elif current_char == ' ':
            # Check if the next 2 characters are void
            void_list.append(None)
            i += 4
        if i >= len(line):
            is_processed = True
    return void_list


def process_step(line: str) -> dict:
    line = line.split()
    step = {}
    step['number'] = int(line[1])
    step['initial'] = int(line[3])
    step['final'] = int(line[5])
    return step

def move_element(initial_config: list, n: int, initial: int, final: int):
    # print(f'Moving {n} elements from {initial} to {final}')
    # Move elements
    for i in range(n):
        initial_list = initial_config[initial]
        initial_element = initial_list.pop()
        final_list = initial_config[final]
        final_list.append(initial_element)

    return initial_config

def move_element_b(initial_config: list, n: int, initial: int, final: int):
    # print(f'Moving {n} elements from {initial} to {final}')
    # Move elements
    moved_elements = []
    print(n)
    for i in range(n):
        initial_list = initial_config[initial]
        # print(initial_list)
        moved_elements.append(initial_list.pop())
        # Reverse the list
        # moved_elements = moved_elements[::-1]
    print(moved_elements)
    # Reverse the list
    moved_elements = moved_elements[::-1]
    print(moved_elements)
    final_list = initial_config[final]
    final_list += moved_elements
    return initial_config


if __name__ == '__main__':
    # initial_config, steps = read_data('./input_5.dat')
    # print(initial_config)
    # print(steps)
    # for step in steps:
    #     initial_config = move_element(initial_config, step['number'], step['initial'] - 1, step['final'] - 1)
    # final_text = [row[-1] for row in initial_config]
    # print("".join(final_text))

    initial_config, steps = read_data('./input_5.dat')
    for step in steps:
        initial_config = move_element_b(initial_config, step['number'], step['initial'] - 1, step['final'] - 1)
    final_text = [row[-1] for row in initial_config]
    print("".join(final_text))
