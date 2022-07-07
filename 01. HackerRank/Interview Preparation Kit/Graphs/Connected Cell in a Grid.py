import os

def maxRegion(row, col):
    if row >= n or row < 0 or col >= m or col < 0 or grid[row][col] == 0:
        return 0
    
    count = 1
    grid[row][col] = 0
    ds = [[-1, 0], [-1, -1], [0, -1], [1,-1], [1, 0], [1, 1], [0, 1], [-1, 1]]
    for i in ds:
        count += maxRegion(row+i[0], col+i[1])
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    m = int(input().strip())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))
    
    answer = []
    for row in range(n):
        for col in range(m):
            if grid[row][col]:
                answer.append(maxRegion(row, col))
    res = max(answer)
    fptr.write(str(res) + '\n')
    fptr.close()