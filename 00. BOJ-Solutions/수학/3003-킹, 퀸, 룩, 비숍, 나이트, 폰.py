import sys
input = sys.stdin.readline

a, b, c, d, e, f = 1, 1, 2, 2, 2, 8
king, queen, rook, bishop, knight, pawn = list(map(int, input().split()))
print (a-king, b-queen, c-rook, d-bishop, e-knight, f-pawn)