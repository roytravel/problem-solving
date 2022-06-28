import os
import copy

def sockMerchant(n, ar):
    result = 0
    copy_ar = copy.deepcopy(ar)
    unique = list(set(copy_ar))
    
    for i in unique:
        cnt = ar.count(i)
        if cnt % 2 == 0:
            result += cnt // 2
        
        elif cnt > 2:
            result += cnt // 2
            
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()