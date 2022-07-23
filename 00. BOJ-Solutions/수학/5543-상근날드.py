# burger, drink = [], []
# [burger.append(int(input())) if i < 3 else drink.append(int(input())) for i in range(5)]
# print (min(burger)+min(drink)-50)
price = [int(input()) for i in range(5)]
print (min(price[:3])+min(price[3:])-50)