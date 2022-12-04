import numpy as np
# get lowercase and uppercase letters
import string

def process_bag(bag, priority_dict: dict):
    bag_string = bag[0]
    # Divide the bag string in two
    left_side = bag_string[:round(len(bag_string) / 2)]
    right_side = bag_string[round(len(bag_string) / 2):]
    # Find common items between the two bags
    common_items = set(left_side).intersection(set(right_side))
    common_items_priority = [priority_dict[item] for item in common_items]
    # Find the highest priority item
    highest_priority_item = max(common_items_priority)

    return highest_priority_item

def process_bag_batch(bag_batch, priority_dict: dict):
    bag_1 = bag_batch[0][0]
    bag_2 = bag_batch[1][0]
    bag_3 = bag_batch[2][0]
    # Perform a triple intersection
    intersected_bag = set(bag_1).intersection(set(bag_2)).intersection(set(bag_3))
    common_item_priority = [priority_dict[item] for item in intersected_bag]
    common_item_priority_max = max(common_item_priority)
    return common_item_priority_max



if __name__ == '__main__':
    # Process input file
    data = []
    with open('./input_3.dat', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.strip().split())
    # Get lowercase string letters
    letters = string.ascii_letters
    point_dict = {letter: i + 1 for i in range(len(letters)) for letter in letters[i]}
    points = 0
    for item in data:
        # print(process_bag(item, point_dict))
        points += process_bag(item, point_dict)
    points = 0
    batch_size = 3
    data_batched = [data[i:i + batch_size] for i in range(0, len(data), batch_size)]
    for batch in data_batched:
        points += process_bag_batch(batch, point_dict)















