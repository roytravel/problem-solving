import sys
input = sys.stdin.readline

unique_nums = list(map(int, input().split()))
verify_num = 0

for i in unique_nums:
    verify_num += pow(i, 2)

print (verify_num % 10)