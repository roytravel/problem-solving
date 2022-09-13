import sys
input = sys.stdin.readline
N = int(input())
M = int(input())
S = input().strip()

count, answer = 0, 0
stack = []

for i in range(M):
    if S[i] == "I":
        stack.append(i)

for i in range(1, len(stack)):
    if stack[i] - stack[i-1] == 2:
        count += 1
    else:
        count = 0   
    if count >= N:
        answer += 1
print (answer)


# solution 1
# import sys
# input = sys.stdin.readline
# N = int(input())
# M = int(input())
# S = input().strip()

# answer, count, i = 0, 0, 0

# while i < M-1:
#     if S[i:i+3] == "IOI":
#         count += 1
#         i += 2
#         if count == N:
#             count -= 1
#             answer += 1
#     else:
#         i += 1
#         count = 0

# print (answer)


# partially correct
# import sys
# input = sys.stdin.readline
# N = int(input())
# M = int(input())
# S = input().strip()
# count = 0
# target = "IO" * N + "I"
# length = len(target)
# for i in range(len(S)-length):
#     if S[i:i+length] == target:
#         count +=1
# print(count)