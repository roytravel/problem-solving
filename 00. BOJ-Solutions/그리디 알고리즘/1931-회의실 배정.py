# -*- coding:utf-8 -*-
import sys

N = int(input())
meetings = []
removes = []
cases = []

for _ in range(N):
    meetings.append(list(map(int, input().split())))

print (meetings)
    
# 시간이 작은 순서대로 정렬
meetings.sort(key = lambda x:x[0])
print (meetings)

# 시작 시간이 같다면 소요시간 작은 순서대로. 작은 것을 솎아내는 로직
for i in range(len(meetings)-1):
    before = meetings[i][0]
    print (i, meetings[i])
    if meetings[i+1][0] == before:
        before_diff = meetings[i][1] - meetings[i][0]
        next_diff = meetings[i+1][1] - meetings[i][0]
        if before_diff <= next_diff:
            removes.append(meetings[i+1])
        elif before_diff > next_diff:
            removes.append(meetings[i])

print (removes)
for i in removes:
    meetings.remove(i)
print (meetings)

cnt = 0
case = []
# 끝나는 시간 바로 다음 시작되는 순서를 찾고, 소요시간 작은 순서대로
for i in range(len(meetings)):
    case.append(meetings[i])
    