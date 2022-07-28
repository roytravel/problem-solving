import sys
input = sys.stdin.readline

def Junhyeon(cash):
    stock = 0
    for i in stock_price:
        if cash >= i:
            stock += cash // i
            cash %= i
    asset = (stock * stock_price[-1]) + cash
    return asset

def Seongmin(cash):
    stock = 0
    for i in range(len(stock_price)-3):
        if stock_price[i] > stock_price[i+1] > stock_price[i+2]:
            stock += cash // stock_price[i+3]
            cash %= stock_price[i+3]

        elif stock_price[i] < stock_price[i+1] < stock_price[i+2]:
            cash += stock * stock_price[i+3]
            stock = 0
    asset = stock * stock_price[-1] + cash
    return asset

cash = int(input())
stock_price = list(map(int, input().split()))

assetJ = Junhyeon(cash)
assetS = Seongmin(cash)

if assetJ > assetS:
    print ("BNP")
elif assetJ < assetS:
    print ("TIMING")
else:
    print ("SAMESAME")