import sys
import heapq
input = sys.stdin.readline

N = int(input())
meeting = []
for _ in range(N):
    meeting.append(list(map(int, input().split())))

meeting.sort(key= lambda x: x[0])
room = [0]
count = 1
for start, end in meeting:
    if start >= room[0]:
        heapq.heappop(room)
    else:
        count +=1
    heapq.heappush(room, end) 
print (count)