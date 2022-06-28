import sys

def do_deduction(S, T):
    while True:
        if len(S) == len(T):
            if S == T:
                print (1)
            else:
                print (0)
            return
        
        if T[-1] == "A":
            T = T[:-1]
        else:
            T = T[:-1][::-1]

if __name__ == "__main__":
    input = sys.stdin.readline
    S = input().strip()
    T = input().strip()
    do_deduction(S, T)