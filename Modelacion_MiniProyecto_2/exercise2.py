import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import random

pb1 = 0.85
pb2 = 0.07
pb3 = 0.07
pb4 = 0.01

pt = (1,0)

def f1(pt):
    return (
        (pt[0] * 0.85 + pt[1]*0.04), 
        (pt[0]*-0.04 + pt[1] * 0.85 + 1.6)
        )

def f2(pt):
    return (
        ((pt[0] * -0.15) + (pt[1]*0.28)), 
        ((pt[0]*0.26) + (pt[1] * 0.24 + 0.44))
        )

def f3(pt):
    return (
        ((pt[0] * 0.2) + (pt[1]*-0.26)), 
        (pt[0]*0.23 + pt[1] * 0.22 + 1.6)
        )

def f4(pt):
    return (
        (0, 0), 
        (pt[0]*0 + pt[1] * 0.16)
        )

points_x = []
points_y = []

for i in range(100000):
    X = random.random()

    if (X < pb1): 
        pt = f1(pt)
    elif (X >= pb1 and X <= (pb1 + pb2)): 
        pt = f2(pt)
    elif (X <= (pb1 + pb2 + pb3)): 
        pt = f3(pt)
    elif (X > (pb1 + pb2 + pb3 + pb4)): 
        pt = f4(pt)
    points_x.append(pt[0])
    points_y.append(pt[1])

plt.scatter(points_x, points_y, [0.1], color='green')
plt.show()