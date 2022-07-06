import os

def luckBalance(k, contests):
    luck = 0
    count = 0
    contests.sort(key=lambda x: (x[0], x[1]), reverse=True)
    
    for game in contests:
        score, important = game
        if k == count and important == 1:
            luck -= score
        else:
            if important:
                count +=1
                luck += score
            else:
                luck += score
    return luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))
    result = luckBalance(k, contests)
    fptr.write(str(result) + '\n')
    fptr.close()
