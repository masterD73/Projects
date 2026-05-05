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
import numpy as np

expo = np.array([])
expo = np.append(expo, np.linspace(-30, 100, 500) ** 2 + np.random.rand(-30, 100) ** 2)
print(expo[1])