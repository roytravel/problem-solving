import sys
from collections import Counter
input = sys.stdin.readline

def get_most_freq_value(nums):
    cnt = Counter(nums).most_common()
    if len(nums) > 1:
        if cnt[0][1] == cnt[1][1]:
            return cnt[1][0]
        else:
            return cnt[0][0]
    else:
        return cnt[0][0]

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
nums.sort()
print (round(sum(nums)/len(nums))) # 산술평균
print (nums[int(len(nums)/2)]) # 중앙값
print (get_most_freq_value(nums)) # 최빈값
print (max(nums) - min(nums)) # 범위