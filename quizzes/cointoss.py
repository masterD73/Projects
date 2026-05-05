# -------------------------
# title: 
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: 
# AI2 InfinityLabs.
# ----------------------------
import numpy as np


def coin_toss_game(gamble: list, runs: int = 1_000) -> float:
    results = []
    for i in range(runs):
        raffle = np.random.randint(2, size=5)
        raf_str = ""
        gamble_str = ""
        for j in raffle:
            raf_str += str(j)
        for k in range(3):
            gamble_str += str(gamble[k])
        if gamble_str in raf_str:
            results.append(1)
        else:
            results.append(0)

    return sum(results) / runs


def winning_pattern(gambles, pattern1=[1, 1, 0]):
    result = []
    games = []
    for gamble in gambles:
        for i in range(1000):
            result.append(coin_toss_game(gamble))
        games.append(result)
        games.append(pattern1)
        results = []
    return games


def main():
    gambles = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 0], [1, 1, 1], [1, 0, 1], [0, 1, 1], [0, 0, 1]]
    results = []
    for i in range(len(gambles)):
        results.append(coin_toss_game(gambles[i], 1_000))
    ls = winning_pattern(gambles)
    print(ls)
    return


if __name__ == '__main__':
    main()
