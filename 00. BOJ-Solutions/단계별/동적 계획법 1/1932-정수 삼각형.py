import sys

def get_max_score(triangles):
    for i in range(len(triangles)):
        for j in range(len(triangles[i])):
            # 1. 현재 깊이에서 가장 큰 수와 인덱스 구하기 --> sum에 큰 수 더해주기
            # 2. 인덱스 기반 다음 깊이에서 큰 수 선정 하고 인덱스 구하기 --> sum에 큰 수 더해주기



input = sys.stdin.readline
n = int(input())
triangles = []

for _ in range(n):
    triangles.append(list(map(int, input().split())))


get_max_score(triangles)