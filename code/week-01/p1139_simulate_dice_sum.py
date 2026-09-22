"""
deep-ml #1139 Simulate Two-Dice Sum Distribution (Easy, Probability)
Суть: построить распределение вероятностей дискретной величины.
Статус: сдана 21-09-26.
"""


import numpy as np


def simulate_dice_sum(num_rolls, seed=0):
    rng = np.random.RandomState(seed)

    dice1 = rng.randint(1, 7, size=num_rolls)
    dice2 = rng.randint(1, 7, size=num_rolls)

    sums = dice1 + dice2

    emp_freq = np.bincount(sums)[2:] / num_rolls

    s = np.arange(start=2, stop=13)

    theor_freq = (6 - np.abs(s-7)) / 36

    return emp_freq, theor_freq
