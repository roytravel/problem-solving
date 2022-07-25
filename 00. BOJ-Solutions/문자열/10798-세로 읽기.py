words = [input() for i in range(5)]
[print(words[i][j], end='') if j < len(words[i]) else None for j in range(15) for i in range(5)]

# words = [input() for i in range(5)]
# for j in range(15):
#     for i in range(5):
#         if j < len(words[i]):
#             print(words[i][j], end='')