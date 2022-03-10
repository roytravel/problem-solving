N, K = list(map(int, input().split()))
peoples = [i+1 for i in range(N)]
sequence = []
idx = K - 1

for _ in range(N):
    if idx < len(peoples):
        sequence.append(peoples.pop(idx))
        idx = idx + K - 1
    
    elif idx >= len(peoples):
        idx = idx % len(peoples)
        sequence.append(peoples.pop(idx))
        idx = idx + K - 1

print ("<", ', '.join(str(i) for i in sequence), ">", sep='')