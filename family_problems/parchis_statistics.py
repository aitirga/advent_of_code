import pandas as pd
import numpy as np

from rich import print
import matplotlib.pyplot as plt



def get_ama_aita_prob(filename: str):
    data = pd.read_csv(filename)
    ama_points = data['ama']
    aita_points = data['aita']
    whole_points = ama_points + aita_points
    return np.mean(ama_points / whole_points), np.mean(aita_points / whole_points)

def get_number_of_matches_won(filename: str):
    data = pd.read_csv(filename)
    ama_wins = 0
    aita_wins = 0
    for line in data.iterrows():
        if line[1]['ama'] == 2:
            ama_wins += 1
        else:
            aita_wins += 1
    return ama_wins, aita_wins

def get_number_of_zeros(filename: str):
    data = pd.read_csv(filename)
    ama_wins = 0
    aita_wins = 0
    for line in data.iterrows():
        if line[1]['ama'] == 0:
            ama_wins += 1
        else:
            aita_wins += 1
    return ama_wins, aita_wins

if __name__ == '__main__':
    data = pd.read_csv('parchis_statistics.txt')
    prob_ama, prob_aita = get_ama_aita_prob('parchis_statistics.txt')
    # Plot in a nice way using markdown and colors
    print(f"[bold yellow]Probabilidad de ganar ama:[/bold yellow] [bold green]{prob_ama * 100:.2f} %[/bold green]")
    print(f"[bold yellow]Probabilidad de ganar aita:[/bold yellow] [bold green]{prob_aita * 100:.2f} %[/bold green]")
    ama_wins, aita_wins = get_number_of_matches_won('parchis_statistics.txt')
    print(f"[bold yellow]Número de partidas ganadas por ama:[/bold yellow] [bold green]{ama_wins}[/bold green]")
    print(f"[bold yellow]Número de partidas ganadas por aita:[/bold yellow] [bold green]{aita_wins}[/bold green]")
    ama_zeros, aita_zeros = get_number_of_zeros('parchis_statistics.txt')
    # print(f"[bold yellow]Número de partidas ganadas por ama con 0 puntos:[/bold yellow] [bold green]{ama_zeros}[/bold green]")
    # print(f"[bold yellow]Número de partidas ganadas por aita con 0 puntos:[/bold yellow] [bold green]{aita_zeros}[/bold green]")

    # Plot the evolution of winning
    plt.scatter(data.index, data['aita'], label='aita')
    plt.scatter(data.index, data['ama'], label='ama')
    # plt.legend()
    plt.ylim(-5,5)
    plt.show()





