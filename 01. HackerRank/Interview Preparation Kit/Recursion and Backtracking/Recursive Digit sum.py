# Solution 
def superDigit(n, k):
    result = sum(list(map(int, str(n)))) * k
    while result>=10: 
        result = sum(list(map(int, str(result))))
    return result

# Time limit: 1/12, Run-time error: 3/12, Succes: 8/12
def superDigit(n, k):
    if len(n) == 1:
        return n
    
    string = n * k
    digit = 0
    
    for s in string:
        digit += int(s)
    
    return superDigit(str(digit), 1)

# Time limit: 1/12, Run-time error: 3/12, Succes: 8/12
def superDigit(n, k):
    if len(str(n)) == 1:
        return n
    
    string = str(n) * k
    digit = 0
    
    for s in string:
        digit += int(s)
    
    return superDigit(digit, 1)

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])
    result = superDigit(n, k)
    print (result)