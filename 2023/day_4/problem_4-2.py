import re

def preprocess_game(lines):
    winning_numbers = []
    my_numbers = []
    for line in lines:
        split_line = line.split(':')[1]
        winning_numbers_str = split_line.split('|')[0]
        my_numbers_str = split_line.split('|')[1]
        # Split with whitespaces
        cur_winning_numbers = winning_numbers_str.split()
        cur_winning_numbers = [int(n) for n in cur_winning_numbers]
        cur_my_numbers = my_numbers_str.split()
        cur_my_numbers = [int(n) for n in cur_my_numbers]
        winning_numbers.append(cur_winning_numbers)
        my_numbers.append(cur_my_numbers)

    return winning_numbers, my_numbers


def process_case(winning_numbers, my_numbers, idx, cards):
    winning_list = winning_numbers[idx]
    my_list = my_numbers[idx]
    n_matches = 0
    cur_card_items = cards[idx]
    for d in winning_list:
        n_matches += int(d in my_list)
    # print(f"Case {idx}: {n_matches} matches")
    values_to_get = [idx + i for i in range(1, n_matches + 1)]
    for card in values_to_get:
        cards[card] += cur_card_items
    return cards

if __name__ == '__main__':
    with open('./input_4.txt', 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    total = 0
    winning_numbers, my_numbers = preprocess_game(lines)
    cards = [1 for _ in range(len(winning_numbers))]
    for case_idx in range(len(winning_numbers)):
        cards = process_case(winning_numbers, my_numbers, case_idx, cards)
    print(sum(cards))

