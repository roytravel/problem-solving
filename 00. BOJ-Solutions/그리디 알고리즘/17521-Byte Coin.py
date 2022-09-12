import sys
input = sys.stdin.readline

n, W = map(int, input().split())
price = []
stock = 0
for _ in range(n):
    price.append(int(input()))

if n == 1:
    print (W)
    exit()

for day in range(len(price)-1):
    if price[day] < price[day+1]:
        Q, W = divmod(W, price[day])
        stock += Q
    else:
        W += stock * price[day]
        stock = 0
    
W += stock * price[-1]
print (W)