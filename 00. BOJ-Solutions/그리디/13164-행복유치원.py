import sys
input = sys.stdin.readline

N, K = map(int, input().split())
people = list(map(int, input().split()))
cost = []
for i in range(N-1):
    cost.append(abs(people[i] - people[i+1]))
cost.sort()
print (sum(cost[:N-K]))