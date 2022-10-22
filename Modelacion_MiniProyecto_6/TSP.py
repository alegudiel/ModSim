# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
V = 8
 
# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
 
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)
 
    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        # store current Path weight(cost)
        current_pathweight = 0
 
        # compute current path weight
        k = s
        for j in i:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
 
        # update minimum
        min_path = min(min_path, current_pathweight)
         
    return min_path, vertex
 
 
# Driver Code
if __name__ == "__main__":
 
    # matrix representation of graph
    graph = [[0,5,9999,6,9999,4,9999,7],
 [5,0,2,4,3,9999,9999,9999],[9999,2,0,1,9999,9999,9999,9999],
 [6,4,1,0,7,9999,9999,9999],[9999,3,9999,7,0,9999,6,4],
 [4,9999,9999,9999,9999,0,3,9999],[9999,9999,9999,9999,6,3,0,2],
 [7,9999,9999,9999,4,9999,2,0]]
    s = 0
    print(travellingSalesmanProblem(graph, s))
    print("ORDEN DE VISITA -> [H1, H6, H7, H8, H5, H2, H3, H4] --DISTANCIA-- 19")