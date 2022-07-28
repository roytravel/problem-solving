import sys
import heapq
input = sys.stdin.readline
N = int(input())
result = 0
array = [int(input()) for _ in range(N)]
heapq.heapify(array)

while len(array) != 1:
    num1 = heapq.heappop(array)
    num2 = heapq.heappop(array)
    _sum = num1 + num2
    result += _sum
    heapq.heappush(array, _sum)

print (result)