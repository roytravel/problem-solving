def flippingBits(n):
    return 4294967295 - n
# def flippingBits(n):
#     array = ""
#     while True:
#         n, r = divmod(n, 2)
#         array += str(r)
#         if n == 1:
#             array += str(n)
#             break

#     array = array[::-1]
#     answer = ""
#     for n in array:
#         if n == "0":
#             answer += "1"
#         else:
#             answer += "0"

#     print (answer)
#     answer = int(answer, base=2)
#     return answer

if __name__ == '__main__':
    q = int(input().strip())
    for q_itr in range(q):
        n = int(input().strip())
        result = flippingBits(n)
        print (result)