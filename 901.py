import math
import numpy as np

# Simulation parameters
# num_simulations = 1000

increments = 0.1
depth = np.arange(0, 4, increments).tolist()[1:]
costs = []

for d in depth:
    prbsuc = 1 - math.exp(-d)
    cost = 0
    depth = d

    while True:
        if np.random.rand() < prbsuc:
            break
        else:
            cost += d
            d = d + increments
            prbsuc = 1 - math.exp(-d)
    if cost == 0:
        cost = d

    print(
        f"Water found at a depth equal to {round(d,1)} metres, from a starting depth of {round(depth, 1)} metres, this well cost {round(cost, 1)} units"
    )


"""

    cost = 0
    d = d

    while True:
        if np.random.rand() < prb:
            cost += d
            d = d + increments
            prb = 1 - math.exp(-d)
            print(prb)
        else:
            print("Water found")
            break

    costs.append(cost)

print(costs)
"""

"""
# Binary search range for d
lower_bound = 0.1
upper_bound = 4
best_d = None
min_average_attempts = float("inf")

while upper_bound - lower_bound > tolerance:
    midpoint_d = (lower_bound + upper_bound) / 2
    costs = []  # Reset the costs for this value of d

    # Run simulations for the midpoint_d
    for _ in range(num_simulations):
        d = midpoint_d
        prb = 1 - math.exp(-d)
        cost = 0

        while True:
            # Check if we "hit" the outcome 1 with the current probability
            if np.random.rand() < prb:
                costs.append(cost)
                break
            else:
                cost += d
                d += increments
                prb = 1 - math.exp(-d)

    # Calculate average attempts for this midpoint_d
    average_attempts = np.mean(costs)

    # Update the best d if this is the lowest average attempts seen so far
    if average_attempts < min_average_attempts:
        min_average_attempts = average_attempts
        best_d = midpoint_d
        # Adjust search bounds to hone in on minimum
        upper_bound = midpoint_d
    else:
        # If this midpoint is not optimal, adjust the bounds to test the other half
        lower_bound = midpoint_d

# Output the best d and its average attempts with high precision
print(f"Optimal initial d: {best_d:.8f}")
print(f"Minimum average attempts: {min_average_attempts}")
"""
