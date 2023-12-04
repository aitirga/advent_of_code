import re

if __name__ == '__main__':
    lines = []
    with open('input_1.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    # Find first number and last number on a string using re
    sum = 0
    for line in lines:
        first_number = int(re.search(r'\d', line).group())
        last_number = int(re.search(r'\d', line[::-1]).group())
        number = first_number * 10 + last_number
        sum += number
    print(sum)

