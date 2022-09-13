N = int(input())
count = 1
house = 1
while N > house:
    house += 6 * count
    count += 1
print (count)