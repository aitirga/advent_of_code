import re
def process_data(line: str):
    game_idx = re.search('Game (\d+)', line)
    game_dict = {
        'id': int(game_idx.group(1)),
        'cases': []
    }
    game_cases = line.split(';')
    for game_case in game_cases:
        game_dict['cases'].append({})

        blue_cases = re.search(("(\d+) blue"), game_case)
        green_cases = re.search(("(\d+) green"), game_case)
        red_cases = re.search(("(\d+) red"), game_case)

        if blue_cases:
            game_dict['cases'][-1]['blue'] = int(blue_cases.group(1))
        if green_cases:
            game_dict['cases'][-1]['green'] = int(green_cases.group(1))
        if red_cases:
            game_dict['cases'][-1]['red'] = int(red_cases.group(1))

    return game_dict



if __name__ == '__main__':
    data = []
    with open('input_2.txt', 'r') as f:
        lines = [f.strip() for f in f.readlines()]

    game_info = []
    for line in lines:
        game_info.append(process_data(line))

    # Problem 2: Find the minimum amount of blocks needed to play each game
    sum_of_powers = 0
    for game in game_info:
        min_red_blocks = 0
        min_green_blocks = 0
        min_blue_blocks = 0
        for case in game['cases']:
            cur_red_blocks = 0
            cur_green_blocks = 0
            cur_blue_blocks = 0
            if 'red' in case.keys():
                cur_red_blocks += case['red']
                if cur_red_blocks > min_red_blocks:
                    min_red_blocks = cur_red_blocks
            if 'green' in case.keys():
                cur_green_blocks += case['green']
                if cur_green_blocks > min_green_blocks:
                    min_green_blocks = cur_green_blocks
            if 'blue' in case.keys():
                cur_blue_blocks += case['blue']
                if cur_blue_blocks > min_blue_blocks:
                    min_blue_blocks = cur_blue_blocks
        power = min_blue_blocks * min_green_blocks * min_red_blocks
        sum_of_powers += power

    print(sum_of_powers)


