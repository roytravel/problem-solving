import sys
input = sys.stdin.readline

villiage = []
all_people = 0

N = int(input())

for i in range(N):
    n_viliage, people = map(int, input().split())
    villiage.append([n_viliage, people])
    all_people += people

villiage.sort(key= lambda x: x[0])

count = 0
for i in range(N):
    count += villiage[i] [1]
    if count >= all_people/2:
        print (villiage[i][0])
        break

import sys
input = sys.stdin.readline

N = int(input())

village = [0] * (N + 1)
people = [0] * (N + 1)

min_values = [0] * (N +1)

for i in range(1, N+1):
    x, a = map(int, input().split())
    village[i] = x
    people[i] = a

for i in range(1, N+1):
    value = 0
    for j in range(1, N+1):
        value += abs(village[j] - i) * people[j]
    
    min_values[i] = value

del min_values[0]
index = min_values.index(min(min_values))
print (village[index+1])