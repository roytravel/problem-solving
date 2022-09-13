import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split()) # number of jewelry, number of bag
jewelry, bags = [], []
answer = 0

for _ in range(N): # Get mass and value using priority queue.
    heapq.heappush(jewelry, list(map(int, input().split())))

for _ in range(K): # Get weight of bag that can contain jewelry.
    bags.append(int(input()))
bags.sort()

temp = []
for bag in bags:
    #print ('Before ', temp, '    ', jewelry)
    while jewelry and bag >= jewelry[0][0]:
        heapq.heappush(temp, -heapq.heappop(jewelry)[1])
        #print ('Mid ', temp, '  ', jewelry)
    #print ('After ', temp, '     ', jewelry)
    if temp:
        answer = answer - heapq.heappop(temp)
    #print (temp, answer)
    elif not jewelry:
        break
    #print (temp)
print (answer)


# Test case is ok but it shows run-time error
# import sys
# input = sys.stdin.readline

# N , K = map(int, input().split()) # number of jewerly, number of bag
# jewelry, bag = [], []
# answer = 0

# for _ in range(N): # Take input as a Mass and Value
#     M, V = map(int, input().split())
#     jewelry.append([M, V])

# for _ in range(K): # Take input as a weight that can contain jewelry
#     W = int(input())
#     bag.append(W)

# jewelry.sort(key=lambda x:x[1], reverse=True)
# bag.sort()

# b, j = 0, 0
# while b < len(bag):
#     if bag[b] >= jewelry[j][0]:
#         answer += jewelry[j][1]
#         b += 1
#         j += 1
#     else:
#         j += 1
# print (answer)