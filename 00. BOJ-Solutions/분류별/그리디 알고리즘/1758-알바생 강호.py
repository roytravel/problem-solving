import sys
input = sys.stdin.readline

N = int(input())

tips = []
for _ in range(N):
    tips.append(int(input()))

tips.sort(reverse=True)

pay = 0
for i in range(len(tips)):
    value = tips[i] - (i+1 - 1)
    if value > 0:
        pay += value
print (pay)