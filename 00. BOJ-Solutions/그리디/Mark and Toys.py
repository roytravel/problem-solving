import os

def maximumToys(prices, k):
    # solution
    prices.sort()
    toy = 0
    for i in prices:
        k = k - i
        if k >= 0:
            toy += 1
        else:
            return toy


    # code that I tried
    count = [0] * (max(prices) + 1)
    for num in prices:
        count[num] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i-1]
    
    result = [0] * len(prices)
    for num in prices:
        idx = count[num]
        result[idx - 1] = num
        count[num] = count[num] - 1
    
    toy = 0
    for i in result:
        k = k - i
        if k >= 0:
            toy += 1
        else:
            return toy

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()