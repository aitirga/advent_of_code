import pandas as pd


class BoatModel:
    def __init__(self, time: float, distance: float):
        self.time = time
        self.distance = distance


def diggest_data(filename: str):
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
    times = lines[0].split(':')[1].split()
    times = [float(t) for t in times]
    distances = lines[1].split(':')[1].split()
    distances = [float(d) for d in distances]
    data = pd.DataFrame({'time': times, 'distance': distances})
    return data


def find_possible_ways(time: float, max_distance: float):
    speeds = [i for i in range(int(time) + 1)]
    better_cases = 0
    for speed in speeds:
        distance = speed * (time - speed)
        if distance > max_distance:
            better_cases += 1
    return better_cases


if __name__ == '__main__':
    import numpy as np
    data = diggest_data('./input_6.txt')
    better_cases = []
    for case in data.values:
        better_cases.append(find_possible_ways(case[0], case[1]))
    print(np.prod(better_cases))
