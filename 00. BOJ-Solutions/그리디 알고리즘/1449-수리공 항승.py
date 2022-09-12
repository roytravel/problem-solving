import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pipe = list(map(int, input().split()))
pipe.sort()

start, end = pipe[0], pipe[0]+L
count = 1

for i in range(N):
    if start <= pipe[i] < end:
        continue 
    else:
        start, end = pipe[i], pipe[i]+L
        count += 1
print (count)


# Wrong
# import sys
# input = sys.stdin.readline

# N, L = map(int, input().split())
# array = list(map(int, input().split()))
# if L == 1:
#     print(N)
#     exit()

# array.sort()
# distance = []
# tape = 0

# for i in range(0, len(array)-L+1):
#     dist = array[i+1] - array[i]
#     if dist <= L:
#         tape += 1

# print (tape)