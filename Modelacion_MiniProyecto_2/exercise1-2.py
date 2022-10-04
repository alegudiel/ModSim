import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import random
# a
# pb1 = 0.25
# pb2 = 0.55
# pb3 = 0.20

# b
# pb1 = 0.15
# pb2 = 0.67
# pb3 = 0.17

# c
pb1 = 0.33
pb2 = 0.66
pb3 = 0.1

pt = (1,0)

def f1(pt):
    return (pt[0] * 0.5, pt[1] * 0.5)

def f2(pt):
    return ((pt[0] * 0.5) + 0.5, pt[1] * 0.5)

def f3(pt):
    return ((pt[0] * 0.5) + 0.25, (pt[1] * 0.5) + 0.5)
points_x = []
points_y = []

for i in range(100000):
    X = random.random()

    if (X < pb1): # Prob entre 0 y 0.2 20%
        pt = f1(pt)
    elif (X >= pb1 and X < pb2): # Prob entre 0.2 y 0.5 30% 
        pt = f2(pt)
    elif (X >= pb2): # Prob entre 0.5 y 1 50% 
        pt = f3(pt)
    points_x.append(pt[0])
    points_y.append(pt[1])

plt.scatter(points_x, points_y, [0.1])
plt.show()