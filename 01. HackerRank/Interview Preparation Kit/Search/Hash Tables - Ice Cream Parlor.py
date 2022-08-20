def whatFlavors(cost, money):
    costs = {}
    for idx, c in enumerate(cost, start=1):
        if money - c in costs:
            print (costs[money-c], idx)
        else:
            costs[c] = idx


# Time over
# def whatFlavors(cost, money, n):
#     answer = []
#     comb = combinations(cost, 2)
#     for res in comb:
#         if sum(res) == money:
#             a = cost.index(res[0])
#             b = cost.index(res[1])
#             if a == b:
#                 cost[a] = -1
#                 b = cost.index(res[1])
#             answer.append(a+1, b+1)
#             break

#     for i in answer:
#         print (i, end=' ')
#     print()

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        money = int(input().strip())
        n = int(input().strip())
        cost = list(map(int, input().rstrip().split()))
        whatFlavors(cost, money)
