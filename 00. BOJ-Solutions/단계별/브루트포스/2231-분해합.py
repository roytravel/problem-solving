def solution(N):
    _sum = 0
    _lists = []
    for i in range(N):
        b = list(map(int, list(str(i))))
        _sum = sum(b)
        if _sum + i == N:
            _lists.append(i)
        else:
            _sum = 0
    return _lists

if __name__ == "__main__":
    N = int(input())
    _lists = solution(N)
    if len(_lists) == 0:
        print (0)
    else:
        print (min(_lists))