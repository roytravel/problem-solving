# coding:utf-8
def solution(jobs):
    time, answer = 0, 0
    jobs.sort(key=lambda x:x[1])
    length = len(jobs)
    while jobs:
        for i in range(len(jobs)):
            if jobs[i][0] <= time:
                time += jobs[i][1]
                answer += time - jobs[i][0]
                jobs.pop(i)
                break
            if i == len(jobs)-1:
                time += 1
    return answer // length


# import heapq
# def solution(jobs):
#     answer, time, i = 0, 0, 0
#     start = -1 
#     heap = []
#     while i < len(jobs):
#         for job in jobs:
#             if start < job[0] <= time: # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
#                 heapq.heappush(heap, [job[1], job[0]])
#         if len(heap) > 0: # 처리할 작업이 있는 경우
#             j = heapq.heappop(heap)
#             start = time
#             time += j[0] # 작업소요시간 저장 (힙에 넣을 때 소요 시간이 기준이므로)
#             answer += time - j[1] # 작업요청시간부터 종료시간까지 시간계산
#             i += 1
#         else: # 처리할 작업이 없는 경우 다음 시간을 넘어감
#             time += 1
#     return answer // len(jobs)


# def solution(jobs):
#     answer, start = 0, 0
#     length = len(jobs)
#     jobs.sort(key=lambda x:x[1])    
#     while jobs:
#         for i in range(len(jobs)):
#             if jobs[i][0] <= start:
#                 start += jobs[i][1]
#                 answer += start - jobs[i][0]
#                 jobs.pop(i)
#                 break
#             else:
#                 start += 1
#             # if i == len(jobs)-1:
#             #     start += 1
#     return answer // length

print(solution([[0, 3], [1, 9], [2, 6]]))