N, M = list(map(int, input().split()))
numbers = list(map(int, input().split()))
max = 0
for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)):
        for k in range(j+1, len(numbers)):
            temp = numbers[i] + numbers[j] + numbers[k]
            if temp > max and temp <=M:
                max = temp
print (max)