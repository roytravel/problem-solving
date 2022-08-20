def findMedian(count, d):
    cnt = 0
    result = 0
    if d % 2 != 0: # The case when d is odd
        for i in range(len(count)):
            cnt += count[i]
            if cnt > d//2:
                result = i
                break
            
    else: # The case when d is even
        first, second = 0, 0
        for i in range(len(count)):
            cnt += count[i]
            if first == 0 and cnt >= d//2:
                first = i
            if second == 0 and cnt >= d//2 + 1:
                second = i
                break
        result = (first+second) / 2
    return result


def activityNotifications(expenditure, d):
    notification = 0
    count = [0] * (200+1)
    
    for i in range(d):
        count[expenditure[i]] += 1

    for i in range(d, len(expenditure)):
        median = findMedian(count, d)

        if expenditure[i] >= median * 2:
            notification += 1

        count[expenditure[i-d]] -= 1
        count[expenditure[i]] += 1

    return notification
    

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    d = int(first_multiple_input[1])
    expenditure = list(map(int, input().rstrip().split()))
    result = activityNotifications(expenditure, d)
    print (result)
