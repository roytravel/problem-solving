import sys
input = sys.stdin.readline
N, K = map(int, input().split())
coin = []
for _ in range(N):
    coin.append(int(input()))

coin.sort(reverse=True)
dp = [0] * N
for i in range(len(coin)):
    if K % coin[i] == 0: # �ִ밪���� coin�� �������� ���� ���� �ִ밪�� ��
        dp[i] = max(dp[i], K // coin[i])
    else: #�ִ밪���� coin�� �������� �ʴ� ���� ���� �� �ִ� �ִ� ũ�⸸ŭ ������ �ٿ���������
        Q, R = divmod(K, coin[i])
        if R in coin:
            
