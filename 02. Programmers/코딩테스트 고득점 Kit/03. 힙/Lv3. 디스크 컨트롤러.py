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
#             if start < job[0] <= time: # ���� �������� ó���� �� �ִ� �۾��� heap�� ����
#                 heapq.heappush(heap, [job[1], job[0]])
#         if len(heap) > 0: # ó���� �۾��� �ִ� ���
#             j = heapq.heappop(heap)
#             start = time
#             time += j[0] # �۾��ҿ�ð� ���� (���� ���� �� �ҿ� �ð��� �����̹Ƿ�)
#             answer += time - j[1] # �۾���û�ð����� ����ð����� �ð����
#             i += 1
#         else: # ó���� �۾��� ���� ��� ���� �ð��� �Ѿ
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