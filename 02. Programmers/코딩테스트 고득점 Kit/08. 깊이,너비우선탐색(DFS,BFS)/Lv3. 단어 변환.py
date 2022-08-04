from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append([begin, 0])

    while queue:
        begin, cnt = queue.popleft()
        if begin == target:
            return cnt

        for word in words:
            count = 0
            for i in range(len(begin)):
                if begin[i] == word[i]:
                    count += 1

            if count == 2:
                queue.append([word, cnt+1])
    return 0

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])) # 4
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])) # 0