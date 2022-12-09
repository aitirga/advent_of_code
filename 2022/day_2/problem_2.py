import numpy as np


def result(v_e: np.ndarray, v_m: np.ndarray, m: np.ndarray) -> np.ndarray:
    return v_e.T @ m @ v_m

def strategy(v_e: np.ndarray, intent: str):
    if intent == 'win':
        v_m = np.roll(v_e, 1)
    elif intent == 'lose':
        v_m = np.roll(v_e, -1)
    else:
        v_m = v_e
    return v_m

if __name__ == '__main__':
    # Process input file
    data = []
    translate_dict_enemy = {'A': [1, 0, 0], 'B': [0, 1, 0], 'C': [0, 0, 1]}
    translate_dict_me = {'X': [1, 0, 0], 'Y': [0, 1, 0], 'Z': [0, 0, 1]}
    scores_type = {'rock': 1, 'paper': 2, 'scissors': 3}
    scores_outcome = {'win': 6, 'draw': 3, 'lose': 0}

    m_background = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
    m_win = np.array([[3, 6, 0], [0, 3, 6], [6, 0, 3]])
    m_game = m_background + m_win

    with open('./input_2.dat', 'r') as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.strip().split())

    points = 0
    for game in data:
        v_e = np.array(translate_dict_enemy[game[0]])
        v_m = np.array(translate_dict_me[game[1]])
        game_result = result(v_e, v_m, m_game)
        points += game_result

    print(points)
    # Part 2
    points = 0
    translate_dict_intent = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}
    for game in data:
        v_e = np.array(translate_dict_enemy[game[0]])
        intent = translate_dict_intent[game[1]]
        v_m = strategy(v_e, intent)
        game_result = result(v_e, v_m, m_game)
        points += game_result
    print(points)



