import sys
from itertools import combinations

def library() -> int:
    cnt = 0
    for i in range(1, len(array)):
        combination = combinations(array, i)
        for elements in combination:
            if sum(elements) == S:
                cnt += 1
    return cnt


def dfs(idx, _sum):
    if idx >= N:
        return

    _sum += array[idx]

    if _sum == S:
        global cnt
        cnt +=1
    
    # 백트래킹
    dfs(idx + 1, _sum - array[idx]) # 현재 array[idx]를 선택하지 않은 경우의 가지
    dfs(idx + 1, _sum) # 현재 array[idx]를 선택한 경우의 가지


def dfs2(idx, _sum):
    global cnt
    if _sum == S:
        cnt +=1

        if idx == N or array[idx] > 0:
            return

    for i in range(idx, N):
        dfs2(i+1, _sum+array[i])


def dfs3(idx, graph, _sum):
    global cnt
    if _sum == S:
        cnt +=1
    
    for j in range(idx+1, N):
        dfs3(j, graph, _sum + graph[j])


def dfs4(idx, depth):
    global cnt
    if (idx >= N):
        if (S == depth):
            cnt +=1
            return
    else:
        dfs4(idx+1, depth+array[idx])
        dfs4(idx+1, depth)


def dfs5(idx, _sum):
    if idx >= N:
        return

    if _sum + array[idx] == S:
        global cnt
        cnt +=1
    
    dfs(idx+1, _sum)
    dfs(idx+1, _sum + array[idx])


def dfs6(_idx, _sum):
    _num = 0					# 합이 s인 부분수열의 개수
    if _idx == N:				# arr 벗어남
        return 0
    if _sum + array[_idx] == S:			# 이번 숫자를 더했을 때 s와 같다면
        _num += 1				# _num을 1 높임

    # 백트래킹
    _num += dfs6(_idx + 1, _sum)			# 이번 숫자 포함 X
    _num += dfs6(_idx + 1, _sum + array[_idx])	# 이번 숫자 포함 O

    return _num	


def powerset(array):
    arr_size = len(array)
    result = []
    for i in range(2 ** arr_size):
        check = bin(i)[2:].zfill(arr_size)
        subset = []
        for j in range(arr_size):
            if (check[j] == '1'):
                subset.append(array[j])
        result.append(subset)
    return result


def bitmask():
    pass


if __name__ == "__main__":

    N, S = list(map(int, sys.stdin.readline().split()))
    array = list(map(int, sys.stdin.readline().split()))
    cnt = 0

    # 조건 불일치 시 프로그램 종료 
    if len(array) != N:
        exit()

    # 1. Solution 1: using library
    # cnt = library()
    # print (cnt)

    # 2. Solution 2: using dfs with backtracking
    # Reference: 
    dfs(0, 0)
    print (cnt)

    # 3. Solution 3: using dfs with backtracking
    # Reference: https://deveun.tistory.com/entry/Python백준-1182부분수열의-합
    # dfs2(0, 0)
    # cnt = cnt - 1 if S == 0 else cnt
    # print (cnt)


    # 4. Solution 4: using dfs with backtracking
    # Reference: https://jellysong.tistory.com/80
    # for i in range(0, N):
    #     dfs3(i, array, array[i])
    
    # print (cnt)


    # 5. Solution 5: using dfs with backtracking
    # Reference: https://dongsik93.github.io/algorithm/2019/11/13/algorithm-boj-1182/
    # dfs4(0, 0)

    # if S:
    #     print (cnt)
    # else:
    #     print (cnt -1)

    # 6. Solution 6: using powerset
    # Reference: https://dongsik93.github.io/algorithm/2019/11/13/algorithm-boj-1182/
    # arr = powerset(array)
    # for i in range(len(arr)):
    #     if sum(arr[i]) == S:
    #         print (arr[i])

    # 7. Solution 7: using dfs with backtracking
    # Reference: https://velog.io/@junho918/Algorithm-백준-1182-부분수열의-합-python
    # dfs(0, 0)
    # print (cnt)

    # 8. Solution 8: using dfs with backtracking
    # Reference: https://velog.io/@deannn/BOJ-%EB%B0%B1%EC%A4%80-1182%EB%B2%88-%EB%B6%80%EB%B6%84%EC%88%98%EC%97%B4%EC%9D%98-%ED%95%A9-Python
    # print (dfs6(0 ,0))