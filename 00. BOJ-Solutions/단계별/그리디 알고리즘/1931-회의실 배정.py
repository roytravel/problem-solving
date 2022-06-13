# import sys
# input = sys.stdin.readline
# meetings = []

# # 회의 수 & 회의 최대 개수 입력
# N = int(input())
# for _ in range(N):
#     meetings.append(list(map(int, input().split())))

# # 시작 시간 순으로 정렬
# meetings.sort(key=lambda x:x[0])
# #print (meetings)

# # 중복 제외
# # meetings = dict.fromkeys(meetings)
# # print (meetings)

# # 시작 시간이 같다면 긴 것 제외
# remove_target = []
# for i in range(len(meetings)-1):
#     current_start = meetings[i][0]
#     next_start = meetings[i+1][0]
#     if current_start == next_start:
#         current_end = meetings[i][1]
#         next_end = meetings[i][1]
#         if current_end - current_start <= next_end - next_start:
#             remove_target.append(meetings[i+1])
#         else:
#             remove_target.append(meetings[i])

# for target in remove_target:
#     meetings.remove(target)

# #print (meetings)
# # 다음 것이 이전의 끝시간보다 작으면서, 차가 이전것보다 작다면, 이전 것은 제외하기

# remove_target2 = []
# for i in range(len(meetings)-1):
#     current = meetings[i]
#     _next = meetings[i+1]
    
#     if current[1] <= _next[0]:
#         continue

#     if current[1] > _next[0]:
#         curr_diff = current[1] - current[0] 
#         next_diff = _next[1] - _next[0]

#         if next_diff < curr_diff:
#             remove_target2.append(meetings[i])

# for target in remove_target2:
#     meetings.remove(target)

# #print (meetings)
# remove_target3 = []
# for i in range(len(meetings)-1):
#     current = meetings[i]
#     _next = meetings[i+1]
#     if _next[0] < current[1]:
#         remove_target3.append(_next)

# for target in remove_target3:
#     meetings.remove(target)

# #print (meetings)
# print (len(meetings))

import sys
input = sys.stdin.readline
N = int(input())

meetings = []
for i in range(N):
    meetings.append(list(map(int, input().split())))

meetings.sort(key = lambda x:(x[1], x[0]))

cnt = 1
end_time = meetings[0][1]
for i in range(1, N):
    if meetings[i][0] >= end_time:
        cnt = cnt + 1
        end_time = meetings[i][1]
print (cnt)