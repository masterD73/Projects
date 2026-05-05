import numpy as np


def knacker(val, wt):
    w = len(wt)
    n = len(val)
    dp = np.zeros((n + 1, w + 1))
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j < wt[i - 1]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(int(val[i - 1] + dp[i - i][j - wt[i - 1]]), int(dp[i - 1][j]))
    return int(dp[-1][-1])


def main():
    val = [10, 40, 30, 50]
    wt = [5, 4, 6, 3]
    assert knacker(val, wt) == 50


if __name__ == '__main__':
    main()
    print("Done.")
