# wrong answer
# equation = input().split("-")
# _sum = 0
# for i in equation:
#     if "+" in i:
#         result = i.split("+")
#         for i in range(len(result)):
#             result[i] = int(result[i])
#         _sum = sum(result)

# for i in equation:
#     if "+" not in i:
#         _sum = int(i) - _sum
# print (_sum)

equation = input().split("-")
answer = 0
for i in equation[0].split("+"):
    answer += int(i)
for i in equation[1:]:
    for j in i.split("+"):
        answer -= int(j)
print(answer)