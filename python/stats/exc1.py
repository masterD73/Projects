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
# q1 - 0.5
import os

import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import beta, binom
import pandas as pd
import os


def main():
    file = os.getcwd() + '\\data.csv'
    p = 0.5
    heads = [True] * 5
    [a, b] = [30, 20]
    alpha = a + 1
    beta = b + 1
    variance = (alpha * beta) / ((alpha + beta) ** 2 * (alpha + beta + 1))
    data = pd.read_csv(file)
    mean = data.binomial.mean()
    p = data['binomial'].sum() / mean
    print(100 * p)
    plt.show()


if __name__ == '__main__':
    main()

data[ 'binomial'].max()