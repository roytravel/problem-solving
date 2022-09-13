import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap, max_heap = [], []
    visited = [False] * k

    for i in range(k):
        command, num = input().split()
        num = int(num)
        if command == "I":
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
            visited[i] = True
        
        elif command == "D":
            if num == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)

            elif num == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if not min_heap or not max_heap:
        print ("EMPTY")
    else:
        print (-max_heap[0][0], min_heap[0][0])


# Time over
# import sys
# import heapq
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     k = int(input())
#     heap = []
#     for __ in range(k):
#         command, value = input().split()
#         if command == "I":
#             heapq.heappush(heap, value)

#         elif command == "D":
#             if not heap:
#                 continue

#             if value == "1":
#                 heapq._heapify_max(heap)
#                 heapq.heappop(heap)

#             elif value == "-1":
#                 heapq.heapify(heap)
#                 heapq.heappop(heap)
    
#     if not heap:
#         print ("EMPTY")
#     else:
#         heapq.heapify(heap)
#         small = heapq.heappop(heap)

#         heapq._heapify_max(heap)
#         big = heapq.heappop(heap)
#         print (big, small)