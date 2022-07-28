import sys
input = sys.stdin.readline
N = int(input())
vote = []
for _ in range(N):
    vote.append(int(input()))

cute = vote.count(1)
uncute = vote.count(0)

if cute > uncute:
    print ("Junhee is cute!")
elif cute < uncute:
    print ("Junhee is not cute!")