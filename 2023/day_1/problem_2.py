if __name__ == '__main__':
    lines = []
    with open('input_1.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]

    # Find first number and last number on a string using re
    sum = 0
    num_dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }
    sum = 0
    idx = 0
    # lines = ['oneightwone']
    for line in lines:
        read_chars = ''
        numbers = []
        for char in line:
            read_chars += char
            for key in num_dict.keys():
                if key in read_chars:
                    num = num_dict[key]
                    numbers.append(num)
                    read_chars = read_chars[-1:]
        sum += numbers[0] * 10 + numbers[-1]
    print(sum)



