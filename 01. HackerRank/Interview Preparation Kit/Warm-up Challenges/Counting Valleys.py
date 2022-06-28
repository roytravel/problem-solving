import os

def countingValleys(steps, path):
    sea_level = 0
    count = 0
    paths = [0]
    for i in range(steps):
        if path[i] == "U":
            sea_level += 1
            paths.append(sea_level)
        elif path[i] == "D":
            sea_level -= 1
            paths.append(sea_level)
            
    for i in range(len(paths)-1):
        if paths[i] == 0:
            if paths[i+1] == -1:
                count += 1
        
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    steps = int(input().strip())
    path = input()
    result = countingValleys(steps, path)
    fptr.write(str(result) + '\n')
    fptr.close()