# -*- coding:utf-8 -*-
import sys

N = int(input())
meetings = []
removes = []
cases = []

for _ in range(N):
    meetings.append(list(map(int, input().split())))

print (meetings)
    
# �ð��� ���� ������� ����
meetings.sort(key = lambda x:x[0])
print (meetings)

# ���� �ð��� ���ٸ� �ҿ�ð� ���� �������. ���� ���� �ԾƳ��� ����
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
# ������ �ð� �ٷ� ���� ���۵Ǵ� ������ ã��, �ҿ�ð� ���� �������
for i in range(len(meetings)):
    case.append(meetings[i])
    