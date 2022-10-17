import sys
input = sys.stdin.readline

N, L, W, H = map(int, input().split())
start, end = 0, max(L, W, H)

for _ in range(100000):
    mid = (start + end) / 2
    count = (L//mid) * (W//mid) * (H//mid)
    if count >= N:
        start = mid
    else:
        end = mid
print('%.10f' % start)

# import sys
# input = sys.stdin.readline

# def binary_search(MAX):
#     start, end = 0, MAX
#     answer = sys.maxsize
#     while start<=end:
#         mid = (start + end) / 2
#         if pow(mid, 3) > MAX:
#             end = mid - 1
#         else:
#             start = mid + 1
#             answer = mid
#     return answer


# N, L, W, H = map(int, input().split())
# MAX = (L * W * H) // N
# MIN = min(L, W, H)
# answer = binary_search(MAX)
# print (answer, MIN)