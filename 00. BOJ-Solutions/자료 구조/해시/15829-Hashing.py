import sys
input = sys.stdin.readline

L = int(input())
string = input().rstrip()
r, m = 31, 1234567891
hash = {'a':1, 'b':2, 'c':3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10,
        "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19,
        "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}

R = [1, 31]
for i in range(0, 50-2):
    R.append(R[-1]*31)

answer, idx = 0, 0
for s in string:
    answer += hash[s] * R[idx]
    idx += 1

print (answer % m)