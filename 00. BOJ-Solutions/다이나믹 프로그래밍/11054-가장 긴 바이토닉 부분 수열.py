N = int(input())
A = list(map(int, input().split()))
B = A[::-1]
increase = [1 for _ in range(N)]
decrease = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if B[i] > B[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for _ in range(N)]
decrease.reverse()
for i in range(N):
    result[i] = increase[i] + decrease[i]

print (max(result)-1)