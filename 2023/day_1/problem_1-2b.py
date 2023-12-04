import re

if __name__ == '__main__':
    lines = []
    with open('input_1.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    # Find first number and last number on a string using re
    num_dict = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3ree',
        'four': 'f4ur',
        'five': 'f5ve',
        'six': 's6x',
        'seven': 's7ven',
        'eight': 'e8ght',
        'nine': 'n9ne',
    }
    # Replace the letters with numbers
    new_lines = []
    for line in lines:
        for key in num_dict.keys():
            line = line.replace(key, str(num_dict[key]))
        new_lines.append(line)

    total_sum = 0
    for idx, line in enumerate(new_lines):
        first_number = int(re.search(r'\d', line).group())
        last_number = int(re.search(r'\d', line[::-1]).group())
        number = first_number * 10 + last_number
        total_sum += number
    print(total_sum)


