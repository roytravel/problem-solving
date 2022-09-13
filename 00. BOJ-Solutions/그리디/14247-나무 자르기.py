import sys
input = sys.stdin.readline

n = int(input())
height = list(map(int, input().split()))
growth = list(map(int, input().split()))
array = []

for i in range(n):
    array.append([height[i], growth[i]])

array.sort(key=lambda x:x[1])
answer = 0
for i in range(n):
    answer += array[i][0] + array[i][1] * i

print (answer)