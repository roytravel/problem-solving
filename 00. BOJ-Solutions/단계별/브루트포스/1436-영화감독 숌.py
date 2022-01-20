import sys
input = sys.stdin.readline

def get_end_num(N):
    cnt = 0
    value = 0
    while True:
        if cnt == N:
            return value
        value +=1
        if "666" in str(value):
            cnt +=1

N = int(input())
value = get_end_num(N)
print (value)