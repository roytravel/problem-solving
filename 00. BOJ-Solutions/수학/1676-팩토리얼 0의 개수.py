import sys
input = sys.stdin.readline

def factorial(N):
    if N == 0:
        return 1
    if N == 1:
        return N
    return N * factorial(N-1)

N = int(input())
value = str(factorial(N))
cnt = 0
value = list(str(value))[::-1]

for i in range(len(value)):
    if value[i] == '0':
        cnt +=1
    else:
        print (cnt)
        break