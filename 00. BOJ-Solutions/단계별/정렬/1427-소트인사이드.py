import sys
input = sys.stdin.readline

N = input().strip('\n')
numbers = sorted(N, reverse=True)
numbers = int("".join(numbers))
print (numbers)