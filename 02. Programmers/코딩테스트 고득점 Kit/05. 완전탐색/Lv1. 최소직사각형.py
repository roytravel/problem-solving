def solution(sizes):
    for i in range(len(sizes)):
        width = sizes[i][0]
        height = sizes[i][1]
        if width > height:
            continue
        else:
            sizes[i][0] = height
            sizes[i][1] = width
        
    width_max = 0
    height_max = 0
    for i in range(len(sizes)):
        if sizes[i][0] > width_max:
            width_max = sizes[i][0]
        if sizes[i][1] > height_max:
            height_max = sizes[i][1]
            
    return width_max * height_max