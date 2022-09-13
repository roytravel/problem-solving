# first try
# import sys
# input = sys.stdin.readline

# loss = []
# N = int(input())
# loss = list(map(int, input().split()))
# loss.sort()

# buffer = []

# if len(loss) % 2 == 0:
#     for i in range(len(loss)):
#         value = loss[i] + loss[len(loss)-i-1]
#         buffer.append(value)
#     print (min(buffer))
    
# else:
#     for i in range(len(loss)):
#         value = loss[i] + loss[len(loss)-i-1]
#         buffer.append(value)
#     print (min(min(buffer), loss[-1]))

# second try
# import sys
# input = sys.stdin.readline

# loss = []
# N = int(input())
# loss = list(map(int, input().split()))
# loss.sort()

# M = sys.maxsize
# if N % 2 == 0:
#     for i in range(N//2):
#         M = min(loss[i] + loss[N-i-1], M)
# else:
#     for i in range(N//2):
#         M = min(loss[i] + loss[N-i-2], M)

# print (M)

# solution
import sys
input = sys.stdin.readline

loss = []
N = int(input())
loss = list(map(int, input().split()))
loss.sort()

if N % 2 == 0:
    M = 0
    for i in range(N//2):
        M = max(loss[i] + loss[N-i-1], M)
else:
    M = loss[N-1]
    for i in range(N//2):
        M = max(loss[i] + loss[N-i-2], M)

print (M)