import sys

def check_group_word(word):
    cache = []
    for i in word:
        if i in cache:
            if i == cache[-1]:
                pass
            else:
                return False
        else:
            cache.append(i)
    return True

if __name__ == "__main__":
    input = sys.stdin.readline
    N = int(input())
    cnt = 0
    for _ in range(N):
        word = input()
        bool = check_group_word(word)
        if bool:
            cnt +=1

    print (cnt)