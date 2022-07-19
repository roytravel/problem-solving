import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
sum_A = 1
sum_B = 1
for i in A:
    sum_A *= i

for i in B:
    sum_B *= i

def GCD(A, B):
    while B:
        A, B = B, A % B
    return A

value = GCD(sum_A, sum_B)
if len(str(value)) > 9:
    print (str(value)[-9:])
else:
    print(value)