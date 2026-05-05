import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def main():
    arr = np.array([1, 2, 3]).reshape(-1, 1)
    min_max_scalar = MinMaxScaler()
    min_max_scalar.fit_transform(arr)


if __name__ == '__main__':
    main()
    print("Done.")
