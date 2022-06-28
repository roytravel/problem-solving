import sys
input = sys.stdin.readline

N = int(input())

drink = []
drink = list(map(int, input().split()))

drink.sort(reverse=True)

quantity = drink[0]
for i in range(1, N):
    quantity += drink[i] / 2

print (quantity)