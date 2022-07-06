import sys
input = sys.stdin.readline

N = int(input())
honey = list(map(int, input().split()))
answer = 0

# honey, beehive, honey
answer = sum(honey[1:N-1]) + max(honey[1:N-1])

# beehive, honey, honey
left = left_total = sum(honey[1:N])
left_max = right_max = 0

for i in range(1, N-1):
    left_total = left_total - (2 * honey[i])
    if left_max < left_total:
        left_max = left_total
    
    left_total = left_total + honey[i]

# # honey, honey, beehive
right = right_total = sum(honey[0:N-1])
for i in range(N-2, -1, -1):
    right_total = right_total - (2 * honey[i])
    if right_max < right_total:
        right_max = right_total
    
    right_total = right_total + honey[i]

print (max(answer, left_max + left, right_max + right))