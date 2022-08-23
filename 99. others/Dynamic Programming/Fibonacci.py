import numpy as np
from collections import defaultdict

class Fibonacci:
    def __init__(self) -> None:
        pass

    def bruteforce(self, N: int) -> int:
        """ recursion with bruteforce """
        if N <= 1:
            return N

        return self.bruteforce(N-1) + self.bruteforce(N-2)

    def memoization(self, N: int) -> int:
        """ Memoization is a top-down way to implement Fibonacci sequence algorithm """
        dp = defaultdict(int)
        if N <= 1:
            return N
        
        if dp[N]:
            return dp[N]
        
        dp[N] = self.memoization(N-1) + self.memoization(N-2)
        return dp[N]

    def tabulation(self, N: int) -> int: # bottom-up
        """ Tabulation is a bottom-up way to implement Fibonacci sequence algorithm """
        dp = defaultdict(int)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, N+1):
            dp[i] = dp[i-2] + dp[i-1]
        
        return dp[N]

    def memory(self, N: int) -> int:
        """ This way is good at memory efficient. Time: O(n), Memory: O(1) """
        x, y = 0, 1
        for _ in range(N):
            x, y = y, x + y
        return x 

    def matrix(self, N: int) -> int:
        """ Time: O(logn) This algortihm is not related to DP but the most efficient way """
        M = np.matrix([[0, 1], [1, 1]])
        vector = np.array([[0], [1]])
        return np.matmul(M ** N, vector)[0]
        

Fib = Fibonacci()
print (Fib.memoization(10))
print (Fib.bruteforce(10))
print (Fib.tabulation(10))
print (Fib.memory(10))
print (Fib.matrix(10))