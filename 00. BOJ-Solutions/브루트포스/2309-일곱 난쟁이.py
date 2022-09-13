import sys
input = sys.stdin.readline

def get_dwarfs():
    if len(picked) == 7 and sum(picked) == 100:
        picked.sort()
        for i in picked:
            print (i)
        exit() 
    
    for i in range(len(heights)):
        if heights[i] not in picked:
            picked.append(heights[i])
            get_dwarfs()
            picked.pop()
            
heights = []
picked = []
for _ in range(9):
    heights.append(int(input()))
get_dwarfs()