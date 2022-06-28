import sys
import math
input = sys.stdin.readline

N = int(input())
DP = [0] * (N + 1)
DP[0] = 0
DP[1] = 1

for i in range(2, N+1):
    _min = 1e9
    for j in range(1, int(math.sqrt(i)) +1):
        _min = min(_min, DP[i - (j ** 2)])
    DP[i] = _min + 1

print (DP[N])

# cnt = 0
# while (N != 0):
#     sqrt = int(math.sqrt(N))
#     origin = sqrt ** 2
#     N = N - origin
#     cnt += 1
#     print (sqrt, origin, N, cnt)