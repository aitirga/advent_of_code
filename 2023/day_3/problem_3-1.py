import re

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




if __name__ == '__main__':
    with open('input_3.txt', 'r') as f:
        data = [f.strip() for f in f.readlines()]

    detected = []
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

    total_value = 0
    for case in detected:
        value = case['value']
        part = is_part_of_the_engine(case, data)
        if part:
            total_value += value
    print(total_value)




