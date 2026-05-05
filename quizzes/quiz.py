# -------------------------
# title: Queens quiz
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Ran & Daniel.
# Reviewer: None
# AI2 InfinityLabs.
# ----------------------------
from collections import namedtuple


def queens(t, n):
    threat = {}
    row_queens = {}
    col_queens = {}
    diag_down_left_queens = {}
    diag_down_right_queens = {}
    queens_threat = [0] * 9

    for elem in t:
        threat[elem] = 0
    for q in t:
        row_queens.setdefault(q[0], []).append(q)
        col_queens.setdefault(q[1], []).append(q)

        if q[0] >= n - q[1]:
            location = (q[0] - (n - 1 - q[1]), n - 1)
        else:
            location = (0, q[0] + q[1])
        diag_down_left_queens.setdefault(location, []).append(q)

        if q[0] > q[1]:
            location = (q[0] - q[1], 0)
        else:
            location = (0, q[1] - q[0])
        diag_down_right_queens.setdefault(location, []).append(q)

    for key in row_queens:
        row_queens[key].sort(key=lambda x: x[1])
        if len(row_queens[key]) > 1:
            threat[row_queens[key][0]] += 1
            threat[row_queens[key][-1]] += 1
            for i in range(1, len(row_queens[key]) - 1):
                threat[row_queens[key][i]] += 2

    for key in col_queens:
        col_queens[key].sort(key=lambda x: x[0])
        if len(col_queens[key]) > 1:
            threat[col_queens[key][0]] += 1
            threat[col_queens[key][-1]] += 1
            for i in range(1, len(col_queens[key]) - 1):
                threat[col_queens[key][i]] += 2

    for key in diag_down_left_queens:
        diag_down_left_queens[key].sort(key=lambda x: x[1])
        if len(diag_down_left_queens[key]) > 1:
            threat[diag_down_left_queens[key][0]] += 1
            threat[diag_down_left_queens[key][-1]] += 1
            for i in range(1, len(diag_down_left_queens[key]) - 1):
                threat[diag_down_left_queens[key][i]] += 2

    for key in diag_down_right_queens:
        diag_down_right_queens[key].sort(key=lambda x: x[1])
        if len(diag_down_right_queens[key]) > 1:
            threat[diag_down_right_queens[key][0]] += 1
            threat[diag_down_right_queens[key][-1]] += 1
            for i in range(1, len(diag_down_right_queens[key]) - 1):
                threat[diag_down_right_queens[key][i]] += 2

    for value in threat.values():
        queens_threat[value] += 1

    return queens_threat


def main():
    # t = [(3, 4), (7, 4), (2, 3), (1, 1), (6, 5), (5, 6), (7, 7), (4, 2), (14, 12), (4, 10), (11, 11)]
    # result = [0, 4, 4, 2, 1, 0, 0, 0, 0]

    board_size, queen_number = input().split(' ')
    queen_list = []
    for i in range(int(queen_number)):
        queen_position_row, queen_position_col = input().split(' ')
        queen_list.append((int(queen_position_row), int(queen_position_col)))

    result = queens(queen_list, int(board_size))
    print(str(result).replace('[', '').replace(']', '').replace(',', ''))


if __name__ == '__main__':
    main()
