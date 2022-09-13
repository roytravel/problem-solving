import sys 
input = sys.stdin.readline

N, K = map(int, input().split())
array = list(map(int, input().split()))
array.sort(reverse=True)
print (array[K-1])