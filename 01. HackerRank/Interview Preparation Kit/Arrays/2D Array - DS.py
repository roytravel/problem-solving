import os

def hourglassSum(arr):
    x , y = 6, 6
    sums = []
    for i in range(y-2):
        for j in range(x-2):
            a = arr[i][j]
            b = arr[i][j+1]
            c = arr[i][j+2]
            d = arr[i+1][j+1]
            e = arr[i+2][j]
            f = arr[i+2][j+1]
            g = arr[i+2][j+2]
            sums.append(a+b+c+d+e+f+g)
    return max(sums)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    fptr.write(str(result) + '\n')
    fptr.close()