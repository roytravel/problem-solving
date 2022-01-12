# coding:utf-8
# Solution 1
def is_adjacent(row):
    for x in range(row):
        # 열이 같음 or 대각선이 같음
        if (queen[x] == queen[row]) or (abs(queen[x] - queen[row]) == abs(row - x)):
            return False
    return True

def dfs1(row):
    if row == N:
        global count
        count = count +1
        return
        
    else:
        for i in range(N):
            queen[row] = i
            if is_adjacent(row):
                dfs1(row+1)

# Solution 2
def dfs2(row):
    count = 0

    if row == N:
        return 1

    for col in range(N):
        queen[row] = col 

        for x in range(row):
            if queen[x] == queen[row]: # 열 체크
                break

            if abs(queen[x] -  queen[row]) == (row-x): # 대각선 체크
                break          
        else:
            count += dfs2(row+1)

    return count


def dfs3(row):
    if row == N:
        global count
        count +=1
        return

    else:
        for col in range(N):
            if visited[col]:
                continue

            queen[row] = col
            
            if is_adjacent(row):
                visited[col] = True
                dfs3(row + 1)
                visited[col] = False


if __name__ == "__main__":
    N = int(input())
    queen = [0] * N
    visited = [False] * N
    count = 0
    dfs3(0)
    print (count)