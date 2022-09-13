import sys
input = sys.stdin.readline

N, M = map(int, input().split())
dictionary = dict()

for i in range(1, N+1):
    name = input().rstrip()
    dictionary[name] = i  
    dictionary[i] = name

for _ in range(M):
    query = input().rstrip()
    if query.isdigit():
        print(dictionary[int(query)])
    else:
        print (dictionary[query])