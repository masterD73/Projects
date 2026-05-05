# -------------------------
# title: Is it Checkmate?
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

KING_W, KING_B, ROOK_W = 2, 3, 5
EMPTY_POSITION = 1


def b_i(location):
    axis_h = -int(location[1])
    axis_v = ord(location[0]) - 97
    return axis_h, axis_v


def chess_board(positions):
    chessboard = np.ones((8, 8), int)
    for position in positions:
        if chessboard[b_i(position[1])] != EMPTY_POSITION:
            raise IndexError("Position already full.")
        chessboard[b_i(position[1])] = position[0]
    return chessboard


def check_axis(chessboard, axis):
    king_b_position = np.where(chessboard == KING_B)
    match axis:
        case 0:
            table = chessboard[:, king_b_position[1]]
        case 1:
            table = chessboard[king_b_position[0], :]
        case _:
            raise ValueError("Selected axis not allowed.")

    check = False
    for elem in table:
        if elem == KING_W:
            break
        for e in table:
            if e == KING_W:
                check = False
            else:
                if e == KING_B:
                    break
    return check


def mult_king(chessboard, king=KING_B):
    block = False
    king_index = np.where(chessboard % king == 0)
    for r in king_index[0] + [-1, 0, 1]:
        if r >= chessboard.shape[0] or r < 0:
            continue
        for c in king_index[1] + [-1, 0, 1]:
            if c >= chessboard.shape[0] or c < 0 or np.all((r, c) == king_index):
                continue
            chessboard[r, c] *= king
    # if (chessboard.shape[0] > king_index[0] + 1 and
    #         chessboard.shape[1] > king_index[1] + 1):
    #     if chessboard[king_index[0] + 1, king_index[1] + 1] == 1:
    #         block = True
    # if 0 <= king_index[0] - 1 and 0 <= king_index[1] - 1:
    #     if chessboard[king_index[0] - 1, king_index[1] - 1] == 1:
    #         block = True
    # if 0 <= king_index[0] - 1 and chessboard.shape[1] > king_index[1] + 1:
    #     if chessboard[king_index[0] - 1, king_index[1] + 1] == 1:
    #         block = True
    # if chessboard.shape[0] > king_index[0] + 1 and 0 <= king_index[1] - 1:
    #     if chessboard[king_index[0] + 1, king_index[1] - 1] == 1:
    #         block = True
    return block


def rook(chessboard):
    rook_index = np.where(chessboard == ROOK_W)


def is_mate(chessboard):
    return mult_king(chessboard) and check_axis(chessboard, 0) and check_axis(chessboard, 1)


def main():
    positions = [(KING_B, "a1"), (ROOK_W, "a8"), (ROOK_W, "b8"), (KING_W, "d3")]
    chessboard = chess_board(positions)

    mult_king(chessboard, KING_B), mult_king(chessboard, KING_W), mult_king(chessboard, ROOK_W)
    print(chessboard)
    # if is_mate(chessboard):
    #     print("Result is checkmate.")
    # else:
    #     print("Result is not checkmate.")


if __name__ == '__main__':
    main()
    print("Done.")

positions = [(KING_B, "a1"), (ROOK_W, "a8"), (ROOK_W, "b8"), (KING_W, "d3")]
chessboard = chess_board(positions)
result = [elem for elem in np.where(chessboard % ROOK_W == 0)]
for elem in result:
    chessboard[elem[0], :] = ROOK_W
    chessboard[:, elem[0]] = ROOK_W
