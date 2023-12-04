import re
def process_data(line: str):
    print(line)
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

    # Problem 1: Check if the combinations are possible with these number of blocks
    red_blocks = 12
    green_blocks = 13
    blue_blocks = 14
    possible_games = 0

    for game in game_info:
        possible = True
        for case in game['cases']:
            cur_red_blocks = 0
            cur_green_blocks = 0
            cur_blue_blocks = 0
            if 'red' in case.keys():
                cur_red_blocks += case['red']
            if 'green' in case.keys():
                cur_green_blocks += case['green']
            if 'blue' in case.keys():
                cur_blue_blocks += case['blue']
            print(cur_red_blocks, cur_green_blocks, cur_blue_blocks)
            if cur_red_blocks > red_blocks:
                possible = False
            if cur_blue_blocks > blue_blocks:
                possible = False
            if cur_green_blocks > green_blocks:
                possible = False
        if possible:
            possible_games += game['id']

    print(possible_games)


