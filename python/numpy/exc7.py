# -------------------------
# title: Broadcasting
# -------------------------
# -------------------------
# Description:
# Various exercises on
# broadcasting principles.
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: Netta Savin.
# AI2 InfinityLabs.
# ----------------------------
import numpy as np


def transpose_mats(mats):
    return mats.transpose(0, 2, 1)


def broadcast_mat_mult(mats, vector):
    return vector @ mats


def dot_mats(mats, vector):
    return np.dot(mats, vector)


def norm_vectors(vectors, precision=10):
    if precision is not None:
        return (((vectors ** 2) @ np.ones(vectors.shape[-1])) ** 0.5).round(int(precision))
    return ((vectors ** 2) @ np.ones(vectors.shape[-1])) ** 0.5


def normalize_vector(vector):
    return vector / (((vector ** 2) @ np.ones(vector.shape[-1])) ** 0.5)


def softmax_mats(mats):
    return np.exp(mats) / (np.exp(mats) @ np.ones((mats.shape[-1], 1)))


def main():
    test_vector1, test_vector2 = np.array([1, 2, -3]), np.array([5, 2, 1])
    vector = np.array(test_vector2)
    mat1 = np.array([test_vector1, test_vector1])
    mat2 = np.array([test_vector2, test_vector1])
    mats = np.array([mat1, mat2])

    assert norm_vectors(normalize_vector(vector)) == 1
    assert np.all(dot_mats(mats, vector) == np.array([[6, 6],
                                                      [30, 6]]))
    assert np.all(transpose_mats(mats) == np.array([[[1, 1],
                                                     [2, 2],
                                                     [-3, -3]],
                                                    [[5, 1],
                                                     [2, 2],
                                                     [1, -3]]]))


if __name__ == '__main__':
    main()
    print("Done.")
