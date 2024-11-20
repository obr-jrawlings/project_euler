import numpy as np
import matplotlib.pyplot as plt


def objective(t):
    n = len(t)
    cost = t[0]
    for i in range(1, n):
        cost += np.exp(-t[i - 1]) * t[i]
    return cost


lists = []
for x in range(2, 25):
    lists.append(objective(list(range(x))))
print(lists)
plt.plot(lists)
plt.show()
