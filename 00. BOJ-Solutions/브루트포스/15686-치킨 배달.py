import sys
from itertools import combinations

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def get_chicken_pos() -> list:
    pos = []
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 2:
                pos.append([i+1, j+1])
    return pos

def remove_chicken_house(pos: list) -> int:
    distance = []    
    combination = combinations(pos, M)
    for comb in list(combination):
        dists = 0
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 1:
                    dist = sys.maxsize
                    for c in comb:
                        dist = min(dist, (abs(c[0] - (i+1)) + abs(c[1] - (j+1))))
                    dists += dist
        distance.append(dists)
    return min(distance)
    
if __name__ == "__main__":
    pos = get_chicken_pos()
    dist = remove_chicken_house(pos)
    print (dist)

# Wrong
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# N, M = list(map(int, input().split()))

# city_matrix = []

# for _ in range(N):
#     city_matrix.append(list(map(int, input().split())))

# houses = []
# chickens = []
# chicken_dists = []

# for i in range(N):
#     for j in range(N):
#         if city_matrix[i][j] == 1:
#             houses.append([i+1, j+1])
        
#         if city_matrix[i][j] == 2:
#             chickens.append([i+1, j+1])


# chicken = list(combinations(chickens, M))

# for i in range(len(chicken[0])):
#     print (chicken[0][i])
#     dist = []
#     for j in range(len(houses)):
#         dist.append(abs(chicken[0][i][0] - houses[j][0]) + abs(chicken[0][i][1] - houses[j][1]))
#         print (dist)
#     chicken_dists.append(min(dist))
#     print (chicken_dists)
    
# print (chicken_dists)
# print (sum(chicken_dists))