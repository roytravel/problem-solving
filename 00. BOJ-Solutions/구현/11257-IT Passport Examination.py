# coding:utf-8
import sys
input = sys.stdin.readline
N = int(input())
for _ in range(N):
    num, A, B, C = list(map(int, input().split()))
    if A+B+C>= 55 and A>=11 and B>=8 and C>=12:
        print (num, A+B+C, "PASS")
    else:
        print (num, A+B+C, "FAIL")