def dec_to_bin(N):
    global binary
    if N == 0:
        return
    
    Q, R = divmod(N, 2)
    binary.append(str(R))
    dec_to_bin(Q)
    
N = int(input())
binary = []
dec_to_bin(N)
print ("".join(list(reversed(binary))), end='')