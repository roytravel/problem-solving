for _ in range(30000):
    length = list(map(int, input().split()))
    length = sorted(length, reverse=True)

    if pow(length[0], 2) == 0 and length[1] == 0 and length[2] == 0:
        break

    if pow(length[0], 2) == pow(length[1], 2) + pow(length[2], 2):
        print ("right")
    else:
        print ("wrong")