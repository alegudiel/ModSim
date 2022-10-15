from sys import maxsize
from itertools import permutations
import numpy as np
import matplotlib.pyplot as plt
import copy
N = 8
V = 8
distance = np.random.rand(N, N)
distance = (distance + distance.T) / 2.0
ind_diag = range(N)
distance[ind_diag, ind_diag] = 0
distance = [[0,5,9999,6,9999,4,9999,7],
 [5,0,2,4,3,9999,9999,9999],[9999,2,0,1,9999,9999,9999,9999],
 [6,4,1,0,7,9999,9999,9999],[9999,3,9999,7,0,9999,6,4],
 [4,9999,9999,9999,9999,0,3,9999],[9999,9999,9999,9999,6,3,0,2],
 [7,9999,9999,9999,4,9999,2,0]]
graph = distance
 
def travellingSalesmanProblem(graph, s):
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight = 0
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)
    return min_path
def cal_dist(distance, L):
    d = 0
    for i in range(len(L)):
        d = d + distance[L[i % N]][L[(i + 1) % N]]
    return d

T = float(pow(2, -8))

ITER = 10000
L = np.arange(N)
print(L)
print(cal_dist(distance, L))
dist_all = []
for i in range(ITER):
    a = np.random.randint(1, N - 1)
    d_t = cal_dist(distance, L)
    dist_all.append(d_t)
    L_tmp = copy.copy(L)
    L_tmp[[a, (a + 1)%N]] = L_tmp[[(a + 1)%N, a]]
    delta_d = cal_dist(distance, L_tmp) - d_t
    p = min(1, np.exp(-1 * delta_d / T))
    u = np.random.rand()
    if u < p:
        L = L_tmp

# print(cal_dist(distance, L))
# plt.plot(dist_all)
