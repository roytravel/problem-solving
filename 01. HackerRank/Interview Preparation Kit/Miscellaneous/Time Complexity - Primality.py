import math 

def primality(n):
    if n == 1:
        return "Not prime"
    
    elif n == 2:
        return "Prime"

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return "Not prime"
    return "Prime"

if __name__ == '__main__':
    p = int(input().strip())
    for p_itr in range(p):
        n = int(input().strip())
        result = primality(n)
        print (result)