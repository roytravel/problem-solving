import sys
input = sys.stdin.readline
N = int(input())
villiage = []
peoples = 0
for _ in range(N):
    idx, people = map(int, input().split())
    villiage.append([idx, people])
    peoples += people

villiage.sort(key= lambda x:x[0])
count = 0
for i in range(N):
    count += villiage[i][1]
    if count > peoples // 2:
        print (villiage[i][0])
        break