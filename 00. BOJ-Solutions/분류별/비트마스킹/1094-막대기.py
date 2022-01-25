import sys
input = sys.stdin.readline

def get_binary(X):
    if X == 0:
        return 

    Q, R = divmod(X, 2)
    binary.append(R)
    get_binary(Q)
    binary.reverse()

X = int(input())
binary = []
get_binary(X)
print (sum(binary))