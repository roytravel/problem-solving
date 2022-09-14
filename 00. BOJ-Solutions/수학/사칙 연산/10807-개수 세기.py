N = int(input())
array = list(map(int, input().split()))
V = int(input())
count = 0
for n in array:
    if n == V:
        count += 1
print(count)