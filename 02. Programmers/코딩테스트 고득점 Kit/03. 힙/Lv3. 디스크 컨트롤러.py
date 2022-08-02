import heapq
def solution(jobs):
    answer = 0
    start = -1
    now = 0
    i = 0
    length = len(jobs)
    heap = []
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= now:
                heapq.heappush(heap, ([job[1], job[0]]))
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            i += 1
        else:
            now +=1
    return answer // length


# def solution(jobs):
#     answer = 0
#     start = 0
#     length = len(jobs)
#     jobs.sort(key=lambda x:x[1])    
#     while jobs:
#         for i in range(len(jobs)):
#             if jobs[i][0] <= start:
#                 start += jobs[i][1]
#                 answer += start - jobs[i][0]
#                 jobs.pop(i)
#                 break
#             if i == len(jobs) - 1:
#                 start += 1
#     return answer // length

print(solution([[0, 3], [1, 9], [2, 6]]))