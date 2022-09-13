import sys
input = sys.stdin.readline

N = int(input())

product = []
for _ in range(N):
    product.append(int(input()))

product.sort(reverse=True)

cost = 0
buffer = []
for i in range(len(product)):
    buffer.append(product[i])
    if len(buffer) == 3:
        cost += buffer[0] + buffer[1]
        buffer = []
    
    if i == len(product)-1:
        cost += sum(buffer)

print (cost)
    

