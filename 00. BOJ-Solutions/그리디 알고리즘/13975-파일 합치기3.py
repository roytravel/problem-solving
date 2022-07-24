import sys
import heapq
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    array = list(map(int, input().split()))
    heapq.heapify(array)
    result = 0
    while len(array) != 1:
        num1 = heapq.heappop(array)
        num2 = heapq.heappop(array)
        _sum = num1 + num2
        result += _sum
        heapq.heappush(array, _sum)

    print (result)