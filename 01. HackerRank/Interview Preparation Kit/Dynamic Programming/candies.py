

def candies(n, arr):
    candy = [1] * n
    for i in range(n-1):
        if arr[i+1] > arr[i]:
            candy[i+1] = candy[i] + 1
    
    for i in range(n-1, 0, -1):
        if arr[i-1] > arr[i] and candy[i] >= candy[i-1]: # 줄어들 때 
            candy[i-1] = candy[i] + 1

    print (candy)
    return sum(candy)



# wrong
# def candies(n, arr):
#     dp = [0] * (n)
#     if arr[0] < arr[1]:
#         dp[0], dp[1] = 1, 2
#     else:
#         dp[0], dp[1] = 2, 1
        
#     for i in range(2, len(arr)):
#         if arr[i] > arr[i-1]:
#             dp[i] = dp[i-1] + 1
#         else:
#             if i == len(arr)-1:
#                 dp[i] = 1
#             else:
#                 if dp[i-1] != 2:
#                     dp[i] = 2
#                 else:
#                     dp[i] = dp[i-1] -1
                
    print (dp)
    return sum(dp)

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)
    print (result)