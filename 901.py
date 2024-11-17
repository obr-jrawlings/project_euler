import math
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
num_simulations = 1000
increments = 0.1
depth = np.arange(1, 15, increments).tolist()[1:]
costs = []
dict_cost = {}

for d in depth:

    for _ in range(num_simulations):
        _d = d
        prbsuc = 1 - math.exp(-_d)
        cost = 0
        while True:
            if np.random.rand() < prbsuc:
                break
            else:
                cost += _d
                _d = _d + increments
                prbsuc = 1 - math.exp(-_d)
        if cost == 0:
            cost = _d
        else:
            cost = cost + _d
        costs.append(cost)
    dict_cost[d] = costs
    costs = []

"""
for key, value in dict_cost.items():
    print(
        f"Key: {key} -> Value Type: {type(value)}, Example Value: {value[:3] if isinstance(value, list) else value}"
    )
"""
a = []
for key, value in dict_cost.items():
    print(key)
    a.append(key - np.average(value))
plt.plot(a)
plt.show()
