"""
This is problem 1 of the advent of code 2022 (https://adventofcode.com/2020/day/1)
"""
import numpy as np

if __name__ == '__main__':
    # Read the input file
    blocks = []
    with open('./input_1.dat', 'r') as f:
        subblock = []
        for line in f.readlines():
            line = line.strip()
            if line != '':
                subblock.append(float(line))
            else:
                blocks.append(sum(subblock))
                subblock = []
    blocks = np.array(blocks)
    print(blocks.max())

    # Part 2: top 3 elves calories
    blocks_ordered = sorted(blocks, reverse=True)
    print(sum(blocks_ordered[:3]))

