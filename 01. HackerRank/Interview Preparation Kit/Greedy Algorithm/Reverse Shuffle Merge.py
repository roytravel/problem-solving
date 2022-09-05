from collections import defaultdict

def reverseShuffleMerge(s):
    result = []
    count = defaultdict(int) # 각 문자열 개수
    used = defaultdict(int) # 정답 후보에 사용된 문자열 개수
    for c in s:
        count[c] += 1

    remain = dict(count) # 남은 문자열 개수 정보
    for c in reversed(s):
        if (count[c] // 2) > used[c]:
            # 스택이 있고, 사용하고 남은것을 더했을 때 count[result[-1]] // 2보다 큰 경우에만
            while result and result[-1] > c and (used[result[-1]] + remain[result[-1]]) > (count[result[-1]] // 2):
                char = result.pop()
                used[char] -= 1
            used[c] += 1
            result.append(c)
        remain[c] -= 1
    return "".join(result)


if __name__ == '__main__':
    s = input()
    result = reverseShuffleMerge(s)
    print (result)