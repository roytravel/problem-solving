import sys
import heapq
input = sys.stdin.readline

N = int(input())
lectures = []

for _ in range(N):
    start, end = list(map(int, input().split()))
    lectures.append([start, end])

lectures.sort(key = lambda x:x[0])
heap = []

heapq.heappush(heap, lectures[0][1])
for i in range(1, N):
    if heap[0] > lectures[i][0]:
        heapq.heappush(heap, lectures[i][1])
    else: # heap[0] <= lectures[i][0]
        heapq.heappop(heap)
        heapq.heappush(heap, lectures[i][1])

print (len(heap))