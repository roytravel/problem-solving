"""
Reference
- https://devlibrary00108.tistory.com/619
- https://ddiyeon.tistory.com/55
- https://dalseoin.tistory.com/entry/백준-파이썬-21317-징검다리-건너기
"""

# import sys
# input = sys.stdin.readline
# N = int(input())
# dp = [1e9] * N
# dp[0] = 0
# energy = []

# for i in range(N-1):
#     small, big = map(int, input().split())
#     energy.append([small, big])
#     if i+1 < N:
#         dp[i+1] = min(dp[i+1], dp[i]+small)
#     if i+2 < N:
#         dp[i+2] = min(dp[i+2], dp[i]+big)
    
# K = int(input())

# _min = dp[-1]

# for i in range(3, N):
#     e, dp1, dp2 = dp[i-3] + K, 1e9, 1e9
#     for j in range(i, N-1):
#         if i+1 <= N:
#             dp1 = min(dp1, e+energy[j][0])
#         if i+2 <= N:
#             dp2 = min(dp2, e+energy[j][1])
        
#         e, dp1, dp2 = dp1, dp2, 1e9
#     _min = min(_min, e)
# print (_min)

# import sys
# input = sys.stdin.readline

# def dfs(current, energy, key):
#     global min_energy 
#     if energy >= min_energy:
#         return
#     if current == N:
#         min_energy = min(min_energy, energy)
#         return
#     if current+1 <= N:
#         dfs(current+1, energy+small[current], key)
#     if current+2 <= N:
#         dfs(current+2, energy+big[current], key)
#     if current+3 <= N and key:
#         dfs(current+3, energy+K, 0)

# N = int(input())
# big = [0]
# small = [0]

# for _ in range(N-1):
#     s, b = map(int, input().split())
#     small.append(s)
#     big.append(b)

# K = int(input())
# min_energy = float('inf')
# dfs(1, 0, 1)
# print (min_energy)


import sys
input = sys.stdin.readline
N = int(input())
energy = []
for _ in range(N-1):
    energy.append(list(map(int, input().split())))

energy = [0] + energy
K = int(input())
array = []
def dfs(idx, sum_energy, super_jump):
    if idx == N:  # return after getting energy that takes until last stone to array.
        array.append(sum_energy)
        return
    elif idx > N:  # return if it over last stone.
        return
    if super_jump == False: # check whether super-jump is used or not.
        dfs(idx+3, sum_energy+K, True)

    dfs(idx+1, sum_energy+energy[idx][0], super_jump)  # small jump
    dfs(idx+2, sum_energy+energy[idx][1], super_jump)  # big jump

dfs(1, 0, False)
print(min(array))  # minimum energy to go N