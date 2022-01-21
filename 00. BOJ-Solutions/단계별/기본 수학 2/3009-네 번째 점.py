import sys
from collections import Counter
input = sys.stdin.readline

def get_square_coordinate(coordinates):
    X, Y = [], []
    for xy in coordinates:
        X.append(xy[0])
        Y.append(xy[1])

    cnt_x = Counter(X).most_common()
    cnt_y = Counter(Y).most_common()
    return cnt_x[-1][0], cnt_y[-1][0]
    
coordinates = []
for _ in range(3):
    coordinates.append(list(map(int, input().split())))

x, y = get_square_coordinate(coordinates)
print (x, y)