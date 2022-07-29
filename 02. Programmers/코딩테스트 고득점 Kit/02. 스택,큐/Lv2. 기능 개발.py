def solution(progresses, speeds):
    answer = []
    temp = 0
    flag = False
    while True:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        count = 0
        for idx, func in enumerate(progresses):
            if func >= 100:
                count +=1
                if idx == len(progresses)-1:
                    flag = True
            else:
                break   
        if count > 0 and count-temp != 0:
            answer.append(count-temp)
            temp = count
            
        if flag:
            break
            
    return answer