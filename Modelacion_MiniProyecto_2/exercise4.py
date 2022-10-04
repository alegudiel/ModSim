'''
Code obtained from: 
https://www.geeksforgeeks.org/monte-carlo-integration-in-python/
https://towardsdatascience.com/how-to-create-a-monte-carlo-simulation-using-python-c24634a0978a
'''
# importing the modules
import numpy as np
import random
import matplotlib.pyplot as plt
import math

# limits of integration
limitA = 0
limitB = 1
# number of iterations
N = 100

# function 
def f(x):
	return np.exp(-x**2)

# function integral
def integrateF(x):
    return 2 * math.exp(-math.pow(1/x - 1, 2)) / math.pow(x, 2)


while N <= 100000:
    #array of zeros of length N
    ar = np.zeros(N)

    # iterating over each Value of ar and filling it
    # with a random value between the limits a and b
    for i in range(len(ar)):
        ar[i] = random.uniform(limitA,limitB)

    # variable to store sum of the functions of different
    # values of x
    integral = 0.0

    # iterates and sums up values of different functions of x
    for i in ar:
        integral += integrateF(i)

    # we get the answer by the formula derived adobe
    answer = (limitB-limitA)/float(N)*integral

    # show the answer in 100, 10,000 y 100,000 iterations.
    if N == 100:
        N = 10000
        print("N = 100 --> Monte Carlo Integration = ", answer, "\n")
    elif N == 10000:
        N = 100000
        print("N = 10,000 --> Monte Carlo Integration = ", answer, "\n")
    elif N == 100000:
        N += 1
        print("N = 100,000 --> Monte Carlo Integration = ", answer, "\n")
    