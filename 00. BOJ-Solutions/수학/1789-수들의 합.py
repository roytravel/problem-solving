import sys
input = sys.stdin.readline

S = int(input())
N = 0
result = 0

for i in range(1, S+1):
    result += i # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + ...
    N += 1
    if result > S:
        N -= 1
        break
print (N)

# memory over
# import sys
# input = sys.stdin.readline
# S = int(input())
# box = [0] * (S+1)
# count = 1
# std = 0
# for i in range(1, S+1):
#     if std - count == 1:
#         count += 1
#         std = 0
#     box[i] = count
#     std += 1
# print (box[S])