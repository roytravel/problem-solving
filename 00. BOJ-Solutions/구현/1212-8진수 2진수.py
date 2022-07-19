import sys
input = sys.stdin.readline
N = input()
if len(str(N)) > 334334:
    exit(0)
print (bin(int(N, base=8))[2:])

# Failed
# def oct_to_dec(N):
#     count = 0
#     dec = 0
#     for i in str(N)[::-1]:
#         dec += int(i) * pow(8, count)
#         count += 1
#     return dec

# def dec_to_bin(dec):
#     bin = []
#     while dec:
#         dec, R = divmod(dec, 2)
#         bin.append(R)
#     return bin[::-1]

# dec = oct_to_dec(N)
# bin = dec_to_bin(dec)
# for i in bin:
#     print (i, end='')