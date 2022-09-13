import sys
input = sys.stdin.readline

def get_max_profit(start):
    global profits, days, poss_profits
    if start > N:
        return

    for i in range(start, len(consulting)):
        day, profit = consulting[i]
        if i + day <= N:
            profits.append(profit)
            days.append(day)
            get_max_profit(day+i)
            profits.pop()
            days.pop()
    
    poss_profits.append(sum(profits))

N = int(input())
consulting = []
poss_profits = []
for _ in range(N):
    consulting.append(list(map(int, input().split())))

days, profits = [], []
get_max_profit(0)
print(max(poss_profits))