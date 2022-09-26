N = int(input())
for i in range(1, N+1):
    print (" "* (N-i) + "*" * (2*i-1))

# Right but it has to change a print format 
# import sys
# input = sys.stdin.readline
# N = int(input())
# star = "*"
# for i in range(1, N+1):
#     if i == 1:
#         space = N - i
#         print (" " * space + star + " " * space)
#     else:
#         star = star + "**"
#         space = N - i
#         print (" " * space + star + " " * space)