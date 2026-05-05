# -------------------------
# title: Data Regression
# -------------------------
# -------------------------
# Description:
# Plotting data and
# linear regression line.
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: Netta Savin.
# AI2 InfinityLabs.
# ----------------------------
import numpy as np
from matplotlib import pyplot as plt


def random_matrix(n: int, m: int) -> np.array:
    np.random.seed(0)
    return np.concatenate((np.random.rand(n, m), np.ones([n, 1])), 1)


def main():
    magnitude = 100
    tolerance = 10e-8
    sample_size = 500
    low_bound, high_bound = -30, 100

    x = np.linspace(low_bound, high_bound, sample_size)
    noise = (np.random.randn(sample_size) * magnitude)
    y = x ** 2 + noise
    x_data = np.column_stack((np.ones((sample_size, 1)), x))
    alpha, beta = (np.linalg.inv(x_data.T @ x_data) @ x_data.T @ y)
    slope = ((x - x.mean()) * (y - y.mean())).sum() / (x.var() * sample_size)
    constant = y.mean() - (x * slope).mean()
    y_hat = x_data @ (alpha, beta)
    plt.plot(y)
    plt.plot(y_hat)
    plt.plot(constant + x * slope)
    plt.show()
    assert alpha + tolerance > constant > alpha - tolerance
    assert beta + tolerance > slope > beta - tolerance


if __name__ == '__main__':
    main()
    print("Done.")
