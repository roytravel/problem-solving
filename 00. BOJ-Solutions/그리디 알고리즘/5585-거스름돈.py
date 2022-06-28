price = int(input())
coins = [500, 100, 50, 10, 5, 1]
change = (1000 - price)
count = 0
for coin in coins:
    Q, R = divmod(change, coin)
    count = count + Q
    change = R
    if R == 0:
        break
print (count)