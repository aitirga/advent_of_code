import re
import numpy as np
def is_part_of_the_engine(case: dict, full_engine: list):
    """Check if the given case is part of the engine"""
    line_idx = case['line_idx']
    start = case['start']
    end = case['end']
    value = case['value']
    cases_to_check = [
        (line_idx, start - 1),
        (line_idx, end),
        *[(line_idx - 1, i) for i in range(start - 1, end + 1)],
        *[(line_idx + 1, i) for i in range(start - 1, end + 1)],
    ]
    check_values = []
    for case_to_check in cases_to_check:
        try:
            if case_to_check[0] < 0 or case_to_check[1] < 0:
                continue
            check_value = full_engine[case_to_check[0]][case_to_check[1]]
            check_values.append(check_value)
        except:
            pass
    # Check there is something different than '.' or number
    check_values = [v for v in check_values if v != '.' and not v.isdigit()]
    if len(check_values) > 0:
        return True
    else:
        return False


def is_gear(case: dict, digits: list):
    """Check if the given case is part of the engine"""
    cur_digits = digits.copy()
    line_idx = case['line_idx']
    pos = case['pos']
    cases_to_check = [
        (line_idx, pos - 1),
        (line_idx, pos + 1),
        *[(line_idx - 1, i) for i in range(pos - 1, pos + 2)],
        *[(line_idx + 1, i) for i in range(pos - 1, pos + 2)],
    ]
    print(cases_to_check)

    adj_digits = []
    for case in cases_to_check:
        if case[0] < 0 or case[1] < 0:
            continue
        print(case)
        for digit_idx, digit in enumerate(cur_digits):
            if digit['line_idx'] == case[0] and digit['start'] <= case[1] <= digit['end'] - 1:
                print(case[1])
                print(digit['start'], digit['end'])
                adj_digits.append(digit['value'])
                # Delete the digit from the list in position digit_idx
                cur_digits.pop(digit_idx)
    # adj_digits = list(set(adj_digits))
    if len(adj_digits) == 2:
        return np.prod(adj_digits)



if __name__ == '__main__':
    with open('input_3.txt', 'r') as f:
        data = [f.strip() for f in f.readlines()]

    detected = []
    detected_gears = []
    for line_idx, line in enumerate(data):
        # Find start and end points in the string
        pattern = r'(\d+)'
        matches = re.finditer(pattern, line)
        for match in matches:
            start = match.start()
            end = match.end()
            value = int(match.group(0))
            detected.append({
                'line_idx': line_idx,
                'start': start,
                'end': end,
                'value': value,
            })

        gear_pattern = r'(\*)'
        gear_matches = re.finditer(gear_pattern, line)
        for match in gear_matches:
            start = match.start()
            end = match.end()
            detected_gears.append({
                'line_idx': line_idx,
                'pos': start,
            })

    total_value = 0
    for case in detected_gears:
        value = is_gear(case, detected)
        if value is not None:
            total_value += value
    print(total_value)




