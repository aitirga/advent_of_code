# Modifying the script to correctly parse the 'seeds' section
steps = ['seed-to-soil map',
         'soil-to-fertilizer map',
         'fertilizer-to-water map',
         'water-to-light map',
         'light-to-temperature map',
         'temperature-to-humidity map',
         'humidity-to-location map'
         ]


def parse_section(section_str):
    """Parse a section of the data file into a list of tuples."""
    lines = section_str.strip().split('\n')
    return [tuple(map(int, line.split())) for line in lines]


def extract_data(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    # Splitting the file content into different sections
    sections = content.split('\n\n')

    # Parsing each section
    data = {}
    for section in sections:
        title, *values = section.split(':')
        if title.strip() == 'seeds':
            # Special handling for seeds as they are not in the same format as other maps
            data[title.strip()] = list(map(int, ':'.join(values).split()))
        else:
            data[title.strip()] = parse_section(':'.join(values))

    return data


def process_step(step, target, data):
    step_data = data[step]
    # print(step_data)
    print('---NEW STEP---')
    # print(f'Processing step {step} with target {target}')
    for destination_start, source_start, steps in step_data:
        print(f'destination_start: {destination_start}, source_start: {source_start}, steps: {steps}')
        if source_start <= target < source_start + steps:
            new_target = (target - source_start) + destination_start
            print(f'New target: {new_target}')
            return new_target
    print(f'New target: {target}')
    return target


def process_seed(seed, data):
    new_seed = seed
    for step in steps:
        new_seed = process_step(step, new_seed, data)
    return new_seed




if __name__ == '__main__':
    extracted_data_fixed = extract_data('./input_5_test.txt')
    data = []
    print(extracted_data_fixed)
    for seed in extracted_data_fixed['seeds']:
        final_seed = process_seed(seed, extracted_data_fixed)
        data.append(final_seed)
    print(min(data))

