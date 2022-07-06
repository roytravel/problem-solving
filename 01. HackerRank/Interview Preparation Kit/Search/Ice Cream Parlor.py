
def whatFlavors(cost, money):
    # partially correct: time over
    # candidate = []
    # for i in range(len(cost)):
    #     for j in range(i+1, len(cost)):
    #         if cost[i] + cost[j] == money:
    #             candidate.append([i+1, j+1])
    #             break
    
    # candidate.sort(key=lambda x: x[0])
    # print (*min(candidate))

    cost_dict = {}
    for idx, c in enumerate(cost):
        if money - c in cost_dict:
            print(f"{cost_dict[money-c] +1} {idx+1}")
            return
        else:
            cost_dict[c] = idx

if __name__ == '__main__':
    t = int(input().strip())
    for t_itr in range(t):
        money = int(input().strip())
        n = int(input().strip())
        cost = list(map(int, input().rstrip().split()))
        whatFlavors(cost, money)
