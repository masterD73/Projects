# -------------------------
# title: Standardize Matrix
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: Netta Savin.
# AI2 InfinityLabs.
# ----------------------------
import pandas as pd
import numpy as np


def standardize(mat, ax=0):
    return (mat - np.nanmean(mat, axis=ax, keepdims=True)) / np.nanstd(mat, axis=ax, keepdims=True)


def main():
    print(np.array(pd.read_csv('data.csv')))
    print(np.array(pd.read_csv('incomplete_data.csv')))


if __name__ == '__main__':
    main()
    print("Done.")
