import sys
input = sys.stdin.readline
N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
ships = list(map(int, input().split()))
cranes.sort(reverse=True)
ships.sort(reverse=True)
count = 0

if ships[0] > cranes[0]:
    print (-1)
    exit()
else:
    while ships:
        for crane in cranes:
            for ship in ships:
                if crane >= ship:
                    ships.remove(ship)
                    break
        count += 1
    print (count)
