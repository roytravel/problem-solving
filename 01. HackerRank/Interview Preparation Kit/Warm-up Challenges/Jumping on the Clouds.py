import os

def jumpingOnClouds(c):
    jump = 0
    count = 0
    while True:
        if jump + 2 <= n - 1:
            jump += 2
            if c[jump] == 1:
                jump -= 1
                count += 1
            else:
                count += 1
        elif jump + 1 <= n - 1:
            jump += 1
            if c[jump] == 1:
                jump -= 1
                count += 1
            else:
                count += 1
        
        else:
            break
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()