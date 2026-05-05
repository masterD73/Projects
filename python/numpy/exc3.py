# -------------------------
# title: Matrix Centering
# -------------------------
# -------------------------
# Description:
# Cropping an image to the
# desired ratio.
# -------------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: Netta Savin.
# AI2 InfinityLabs.
# ----------------------------
import numpy as np
from matplotlib import image, pyplot as plt


def center_matrix(arr, crop=0.25):
    if crop >= 0.5:
        raise ValueError("Cropping value of both sides cannot reach 50% or more.")
    rows = int(arr.shape[0] // (1 / crop))
    print(rows)
    cols = int(arr.shape[1] // (1 / crop))
    return arr[rows:-rows, cols:-cols]


image = image.imread('lion-zion.jpeg')
middle = center_matrix(np.array(image), 0.25)
plt.imshow(middle)
plt.show()
