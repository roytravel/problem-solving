import sys 

def get_count_one(X):
    while X != 0:
        if X in dp.keys():
            binary.append(dp[X])
            break
        else:
            Q, R = divmod(X, 2)
            binary.append(R)
            X = X // 2
    return binary

if __name__ == "__main__":
    input = sys.stdin.readline
    A, B = list(map(int, input().split()))
    binary = []
    dp = {}
    _sum = 0

    for i in range(A, B+1):
        binary = get_count_one(i)
        _sum += sum(binary)
        dp[i] = sum(binary)
        binary = []
    print (_sum)