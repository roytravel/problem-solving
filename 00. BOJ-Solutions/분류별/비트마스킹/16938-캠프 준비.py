import sys
from itertools import combinations

# def get_combinations(start, depth):
#     if depth == len(picked):
#         result.append(picked)
#         return

#     for i in range(start, len(level)):
#         if not visited[i]:
#             visited[i] = True
#             picked.append(level[i])
#             get_combinations(i+1, depth)
#             picked.pop()
#             visited[i]= False
    
#     return result

# visited = [False] * N
# picked = []
# result = []

if __name__ == "__main__":
    input = sys.stdin.readline
    N, L ,R, X = list(map(int, input().split()))
    level = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N+1):
        result = list(combinations(level, i))
        for r in result:
            if sum(r) >= L and sum(r) <= R:
                if max(r)-min(r) >= X:
                    cnt +=1
    print (cnt)


