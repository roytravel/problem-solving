# import sys
# input = sys.stdin.readline

# N = int(input())
# road_length = list(map(int, input().split()))
# oil_price = list(map(int, input().split()))

# road_total_length = sum(road_length)
# total_price = 0

# for i in range(len(oil_price)-1):
#     min_value = min(oil_price)
#     max_value = max(oil_price)

#     if oil_price[i] == min_value:
#         total_price += road_total_length * oil_price[i]
#         break

#     elif oil_price[i] == max_value:
#         total_price += oil_price[i] * road_length[i]
    
#     else:
#         if oil_price[i] >= oil_price[i+1]:
#             total_price += oil_price[i] * road_length[i]

#         elif oil_price[i] < oil_price[i+1]:
#             total_price += oil_price[i+1] * road_length[i+1]
    
#     oil_price.pop(i)

# print (total_price)

import sys
input = sys.stdin.readline

N = int(input())
road_len = list(map(int, input().split()))
oil_cost = list(map(int, input().split()))
total_cost = 0

total_cost += (road_len[0] * oil_cost[0])
min_price = oil_cost[0]

for i in range(1, N-1):
    if min_price > oil_cost[i]:
        min_price = oil_cost[i]

    total_cost += (min_price * road_len[i])

print (total_cost)