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
import random


def monty_hall_test(tests: int = 100) -> tuple[float, float]:
    correct, wrong = 1, 0
    won_no_change, won_change = 0, 0
    for i in range(tests):
        doors = [wrong] * 3
        doors[random.randint(0, 2)] = correct
        player_choice = random.randint(0, 2)
        if doors[player_choice] == correct:
            won_no_change += 1
        doors.pop(player_choice)
        doors.remove(wrong)
        if doors[0] == correct:
            won_change += 1
    return won_change / tests, won_no_change / tests


def main():
    tests_num = 1000000
    print(monty_hall_test(tests_num))
    print('Done.')


if __name__ == '__main__':
    main()
