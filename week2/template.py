import matplotlib.pyplot as plt
import numpy as np

p_h=0.7
iterations=1 # number of iterations for policy iteration(obviously more than 1)

"""
Initialize parameters
discount_factor=1
value_estimates = np.zeros(101) 
value_estimates[100] = 1  # terminal state value
policy = np.ones(100, dtype=int)  # initial policy: bet 1, ensure integer type
policy[0] = 0  # state 0 is terminal, no bet
"""

for iteration in range(iterations):
    pass
    #step 1 :evaluation of policy:inital policy is to bet 1
     #step 2: new policy = greedy (value function with previous policy)
     
# Plotting the value function for some iterations to visualize convergence
# Plot final policy