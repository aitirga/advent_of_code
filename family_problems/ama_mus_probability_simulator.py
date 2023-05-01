import random
import rich
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_ama_aita_prob(filename: str):
    data = pd.read_csv(filename)
    ama_points = data['ama']
    aita_points = data['aita']
    whole_points = ama_points + aita_points
    return np.mean(ama_points / whole_points), np.mean(aita_points / whole_points)


def sim_mus(target_points):
    points_ama = 0
    points_aita = 0
    while points_aita < target_points and points_ama < target_points:
        if random.random() < prob_ama_mus:
            points_ama += 1
        else:
            points_aita += 1
    return points_ama, points_aita

def sim_mus_whole(n_sim, at_least_points):
    ama_wins = 0
    aita_wins = 0

    while n_sim < n_max:
        points_ama, points_aita = sim_mus(target_mus)
        if points_ama >= at_least_points:
            ama_wins += 1
        if points_aita >= at_least_points:
            aita_wins += 1
        n_sim += 1
    return ama_wins/n_sim, aita_wins/n_sim


if __name__ == '__main__':
    prob_ama_mus, prob_aita_mus = get_ama_aita_prob('./mus_statistics.txt')
    print(f'Probabilidad ama: {prob_ama_mus * 100} %, probabilidad aita: {prob_aita_mus * 100} %')
    target_mus = 22
    n_max = 20000

    n_sim = 0
    ama_wins = 0
    aita_wins = 0
    prob_ama = [sim_mus_whole(n_sim, at_least_points)[0] * 100 for at_least_points in range(1, target_mus + 1)]
    prob_aita = [sim_mus_whole(n_sim, at_least_points)[1] * 100 for at_least_points in range(1, target_mus + 1)]
    plt.plot(prob_ama, label='ama')
    plt.plot(prob_aita, label='aita')
    plt.xlabel('Puntos en el MUS [-]')
    plt.ylabel('Probabilidad de ganar [%]')
    plt.title(f'Probabilidad ama: {prob_ama_mus * 100:1.2f} %, probabilidad aita: {prob_aita_mus * 100:1.2f} %')
    # Show the number in the axis of each point: 1, 2, 3, 4, 5...
    # Reescale axis 0.0 to 1.0
    plt.ylim(0, 110)
    plt.xticks(range(0, target_mus))
    plt.legend()
    plt.grid()
    plt.show()

    print(f'Probabilidad de que ama gane con {target_mus} puntos: {sim_mus_whole(n_sim, target_mus)[0] * 100:1.2f} %')
    print(f'Probabilidad de que aita gane con {target_mus} puntos: {sim_mus_whole(n_sim, target_mus)[1] * 100:1.2f} %')






