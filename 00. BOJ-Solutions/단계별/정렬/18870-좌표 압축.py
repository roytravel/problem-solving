import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
nums_bak = sorted(list(set(nums)))
compressed = {}
for i in range(len(nums_bak)): # keypoint
    compressed[nums_bak[i]] = i

for i in nums:
    print(compressed[i], end = " ")