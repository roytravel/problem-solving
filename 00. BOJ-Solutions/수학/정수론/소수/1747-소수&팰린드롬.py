import sys
input = sys.stdin.readline
N = int(input())
MAX = 1000000

def make_sieve() -> list:
    table = [False, False] + [True] * (MAX-1)
    prime = []
    for i in range(2, MAX+1):
        if table[i]:
            prime.append(i)
            for j in range(i+i, MAX+1, i):
                table[j] = False
    return prime

def is_palindrome(num: int) -> bool:
    if num == int(str(num)[::-1]):
        return True
    return False

prime = make_sieve()
result = 0
for i in range(N, MAX+1):
    if is_palindrome(i):
        if i in prime:
            result = i
            break

if not result:
    print(1003001)
else:
    print (result)