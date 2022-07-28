import sys
input = sys.stdin.readline
N, K = map(int, input().split())
array = list(map(int, input().split()))
left, right = 0, 0
count = [0] * (max(array)+1)
answer = 0
while right < N:
    if count[array[right]] < K:
        count[array[right]] += 1
        right +=1
    else:
        count[array[left]] -= 1
        left += 1
    answer = (max(answer, right-left))
print (answer)

# time over
# import sys
# input = sys.stdin.readline
# N, K = map(int, input().split())
# count = [0] * (N+1)
# array = list(map(int, input().split()))

# cnt = []
# for i in array:
#     count[i] += 1
#     if max(count) > K:
#         cnt.append(sum(count)-1)
#         count = [0] * (N+1)
#         count[i] += 1
#         continue

#     if i == array[-1]:
#         cnt.append(sum(count))

# print (max(cnt))