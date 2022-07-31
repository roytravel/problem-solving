import heapq

def solution(operations):
    answer = []
    for operation in operations:
        cmd, num = operation.split()
        num = int(num)
        if cmd == "I":
            heapq.heappush(answer, num)
        
        elif cmd == "D" and not answer:
            continue

        elif cmd == "D" and num == -1:
            _ = heapq.heappop(answer)
        
        elif cmd == "D" and num == 1:
            answer = heapq.nlargest(len(answer), answer)[1:]
            heapq.heapify(answer)
    
    if answer:
        return [max(answer), min(answer)]
    else:
        return [0, 0]
        
# import heapq

# def solution(operations):
#     answer = []
#     for operation in operations:
#         cmd, num = operation.split()
#         num = int(num)
#         if cmd == "I":
#             heapq.heappush(answer, num)
        
#         elif cmd == "D" and not answer:
#             continue

#         elif cmd == "D" and num == -1:
#             _ = heapq.heappop(answer, num)
        
#         elif cmd == "D" and num == 1:
#             _ = heapq.nlargest(num)
    
#     if answer:
#         return [answer[0], answer[-1]]
#     else:
#         return [0, 0]


# # import heapq

# # def solution(operations):
# #     min_heap = []
# #     max_heap = []
# #     for operation in operations:
# #         cmd, num = operation.split()
# #         num = int(num)
# #         if cmd == "I":
# #             heapq.heappush(min_heap, num)
# #             heapq.heappush(max_heap, (-num, num))
            
# #         elif cmd == "D" and len(min_heap)==0:
# #             continue
            
# #         elif cmd == "D" and num == -1:
# #             min_num = heapq.heappop(min_heap)
# #             max_heap.remove((-min_num, min_num))
        
# #         elif cmd == "D" and num == 1:
# #             max_num = heapq.heappop(max_heap)[1]
# #             min_heap.remove(max_num)
            
# #     if min_heap:
# #         return [heapq.heappop(max_heap)[1], heapq.heappop(min_heap)]
# #     else:
# #         return [0, 0]