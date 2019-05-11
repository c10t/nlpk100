import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

RESOURCE = './resources/q75.txt'

with Path(RESOURCE).open(encoding='utf-8') as f:
    probs = []
    for line in f:
        ans, pred, prob = line.strip().split('\t')
        is_pos = float(prob) if pred == '+1' else 1.0 - float(prob)
        probs.append((ans, is_pos))

threshold = 0.0


def precision(probs, threshold):
    tp, fp, tn, fn = 0, 0, 0, 0
    for ans, prob in probs:
        if ans == '+1' and prob > threshold:
            tp += 1
        if ans == '+1' and prob <= threshold:
            fn += 1
        if ans == '-1' and prob > threshold:
            fp += 1
        if ans == '-1' and prob <= threshold:
            tn += 1
    precision = tp / (tp + fp + 0.000000001)
    return precision


def recall(probs, threshold):
    tp, fp, tn, fn = 0, 0, 0, 0
    for ans, prob in probs:
        if ans == '+1' and prob > threshold:
            tp += 1
        if ans == '+1' and prob <= threshold:
            fn += 1
        if ans == '-1' and prob > threshold:
            fp += 1
        if ans == '-1' and prob <= threshold:
            tn += 1
    recall = tp / (tp + fn + 0.000000001)
    return recall


# %matplotlib inline
x = np.linspace(0.0, 0.99, 100)

plt.plot(x, [precision(probs, xk) for xk in x])
plt.plot(x, [recall(probs, xk) for xk in x])
plt.grid(True)
