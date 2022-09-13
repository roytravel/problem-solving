import sys
from itertools import combinations
input = sys.stdin.readline

N, M = list(map(int, input().split()))

city_matrix = []

for _ in range(N):
    city_matrix.append(list(map(int, input().split())))

houses = []
chickens = []
chicken_dists = []

for i in range(N):
    for j in range(N):
        if city_matrix[i][j] == 1:
            houses.append([i+1, j+1])
        
        if city_matrix[i][j] == 2:
            chickens.append([i+1, j+1])


chicken = list(combinations(chickens, M))

for i in range(len(chicken[0])):
    print (chicken[0][i])
    dist = []
    for j in range(len(houses)):
        dist.append(abs(chicken[0][i][0] - houses[j][0]) + abs(chicken[0][i][1] - houses[j][1]))
        print (dist)
    chicken_dists.append(min(dist))
    print (chicken_dists)
    
print (chicken_dists)
print (sum(chicken_dists))