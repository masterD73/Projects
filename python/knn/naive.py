# -------------------------
# title: KNN Naive Numpy
# -------------------------
# -------------------------
# Description: 
# -------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: Alexander Volkovich.
# AI2 InfinityLabs.
# ------------------------------
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix


def knn_naive(X_train, X_test, y_train, k):
    y_pred = np.array(
        [np.argmax(np.bincount(y_train[np.argsort(np.sqrt(np.sum((x - X_train) ** 2, axis=1)))[0:k]])) for x in X_test])
    return y_pred


def main():
    iris_data = load_iris()
    x, y = iris_data.data, iris_data.target
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    k = 3
    print(confusion_matrix(y_test, knn_naive(x_train, x_test, y_train, k)))
    print(classification_report(y_test, knn_naive(x_train, x_test, y_train, k)))


if __name__ == '__main__':
    main()
    print("Done.")
