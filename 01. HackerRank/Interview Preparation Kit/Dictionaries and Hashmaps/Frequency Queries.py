from collections import defaultdict

def freqQuery(queries):
    answer = []
    freq = defaultdict(int)
    for cmd, value in queries:
        if cmd == 1:
            freq[value] += 1
        elif cmd == 2:
            if value in freq and freq[value] > 0:
                freq[value] -= 1
        else:
            if value in set(freq.values()):
                answer.append(1)
            else:
                answer.append(0)
    return answer


# def freqQuery(queries):
#     answer = []
#     dic = defaultdict(int)
#     for cmd, value in queries:
#         if cmd == 1:
#             dic[value] += 1
#         elif cmd == 2:
#             if dic[value] > 0:
#                 dic[value] -= 1
#         else:
#             if value in set(dic.values()):
#                 answer.append(1)
#                 continue
#             else:
#                 answer.append(0)
#     return answer


# Time over 4 but It solved one more case
# def freqQuery(queries):
#     answer = []
#     dic = defaultdict(int)
#     for cmd, value in queries:
#         if cmd == 1:
#             dic[value] += 1
#         elif cmd == 2:
#             if dic[value] > 0:
#                 dic[value] -= 1
#         elif cmd == 3:
#             if value in set(dic.values()):
#                 answer.append(1)
#                 continue
#             else:
#                 answer.append(0)
#     return answer

# Time over 3
# def freqQuery(queries):
#     answer = []
#     dic = defaultdict(int)
#     for cmd, value in queries:
#         if cmd == 1:
#             dic[value] += 1
#         elif cmd == 2:
#             if dic[value] > 0:
#                 dic[value] -= 1
#         elif cmd == 3:
#             if value in dic.values():
#                 answer.append(1)
#                 continue
#             else:
#                 answer.append(0)
#     return answer


# Time over 2
# def freqQuery(queries):
#     answer = []
#     dic = defaultdict(int)
#     for cmd, value in queries:
#         if cmd == 1:
#             dic[value] += 1
#         elif cmd == 2:
#             if dic[value] > 0:
#                 dic[value] -= 1
#         elif cmd == 3:
#             if value in dic.values():
#                 answer.append(1)
#             else:
#                 answer.append(0)
#     return answer

# Time over 
# def freqQuery(queries):
#     answer = []
#     dic = defaultdict(int)
#     for cmd, value in queries:
#         if cmd == 1:
#             dic[value] += 1
#         elif cmd == 2:
#             if dic[value] > 0:
#                 dic[value] -= 1
#         elif cmd == 3:
#             for v in dic.values():
#                 if value in v:
#                     answer.append(1)
#                     break
#             else:
#                 answer.append(0)
#     return answer

if __name__ == '__main__':
    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print ('\n'.join(map(str, ans)))
    print ('\n')
