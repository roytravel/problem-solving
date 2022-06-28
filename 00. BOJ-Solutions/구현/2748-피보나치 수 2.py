import sys
input = sys.stdin.readline

fibo_nums = [0, 1]
for i in range(90):
    fibo_nums.append(sum([fibo_nums[-1], fibo_nums[-2]]))
    
n = int(input())
print (fibo_nums[n])