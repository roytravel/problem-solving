import sys
import heapq
input = sys.stdin.readline
N = int(input())
min_heap, max_heap = [], []

for _ in range(N):
    num = int(input())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)
    
    if len(max_heap) >=1 and len(min_heap) >= 1 and max_heap[0] * -1 > min_heap[0]:
        max_value = heapq.heappop(max_heap) * -1
        min_value = heapq.heappop(min_heap)

        heapq.heappush(max_heap, min_value * -1)
        heapq.heappush(min_heap, max_value)
    print(max_heap[0] * -1)

# import sys
# import heapq
# input = sys.stdin.readline

# N = int(input())
# heap = []
# for i in range(N):
#     num = int(input())
#     heapq.heappush(heap, num)
#     print (num, heap)
#     if len(heap) < 3:
#         print("a:", (heap[0]))
#     else:
#         k = ((len(heap) +1) //2)
#         heap_copy = heap.copy()
#         for _ in range(k-1):
#             heapq.heappop(heap_copy)
#         print("a:", heapq.heappop(heap_copy))