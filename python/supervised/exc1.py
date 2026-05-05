# -------------------------
# title:
# -------------------------
# -------------------------
# Description:
# -------------------------
# ------------------------------
# Author: Daniel Merchav.
# Reviewer: None.
# AI2 InfinityLabs.
# ------------------------------
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import SGDClassifier
from sklearn.dummy import DummyClassifier

k = 5
kf = KFold(n_splits=k, shuffle=True, random_state=42)
model = LinearRegression()
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target
scores = cross_val_score(model, X, y, cv=kf, scoring='r2')
round(np.mean(scores) * 100, 2)


def plot_digit(image_data):
    image = image_data.reshape(28, 28)
    plt.imshow(image, cmap='binary', interpolation='nearest')
    plt.axis('off')


def main():
    mnist = fetch_openml('mnist_784', as_frame=False)
    x, y = mnist.data, mnist.target
    # plot_digit(x[0])
    # plt.show()
    x_train, x_test, y_train, y_test = x[:60000], x[60000:], y[:60000].astype(int), y[60000:].astype(int)
    y_train_5 = (y_train == 5)
    y_test_5 = (y_test == 5)
    sgd_clf = SGDClassifier(random_state=42)

    sgd_clf.fit(x_train, y_train_5)
    sgd_clf.predict([x[0]])
    cross_val_score(sgd_clf, x_train, y_train_5, cv=3, scoring='accuracy')
    dummy_clf = DummyClassifier()
    dummy_clf.fit(x_train, y_train_5)
    cross_val_score(dummy_clf, x_train, y_train_5, cv=3, scoring='accuracy')
    y_trained_pred = cross_val_predict(sgd_clf, x_train, y_train_5, cv=3)
    cm = confusion_matrix(y_train_5, y_trained_pred)
    precision_score(y_train_5, y_trained_pred)
    recall_score(y_train_5, y_trained_pred)
    f1 = 2 * (precision_score(y_train_5, y_trained_pred) * recall_score(y_train_5, y_trained_pred)) / (
            precision_score(y_train_5, y_trained_pred) + recall_score(y_train_5, y_trained_pred))
    print(f1)


if __name__ == '__main__':
    main()
    print("Done.")
