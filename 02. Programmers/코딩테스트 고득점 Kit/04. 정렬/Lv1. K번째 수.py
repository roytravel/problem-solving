def solution(array, commands):
    answer = []
    for i in commands:
        start = i[0] -1
        end = i[1] -1
        k = i[2] -1
        arr = list(sorted(array[start:end+1]))
        answer.append(arr[k])
    return answer