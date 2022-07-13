import sys
from itertools import permutations
from functools import reduce
input = sys.stdin.readline

def get_min_diff():
    if len(S) == N and len(B) == N:
        for i in range(1, N+1):
            result_s = permutations(S, i)
            result_b = permutations(B, i)

            for s in result_s:
                sss.append(reduce(lambda x, y: x*y, s))
            
            for b in result_b:
                bbb.append(sum(b))

            for j in range(len(sss)):
                ans.append(abs(sss[j] - bbb[j]))
        return
    
    for i in range(len(gradient)):
        if not visited[i]:
            visited[i] = True
            S.append(gradient[i][0])
            B.append(gradient[i][1])
            get_min_diff()
            S.pop()
            B.pop()
            visited[i] = False
            
N = int(input())
gradient = []
visited = [False] * N
S, B = [], []
sss, bbb, ans = [], [], []
for _ in range(N):
    gradient.append(list(map(int, input().split())))
get_min_diff()
print (min(ans))