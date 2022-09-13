from collections import deque

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    
    array = input().rstrip()[1:-1].split(",")
    queue = deque(array)
    if n == 0:
        queue = deque()

    flag = 0
    
    for cmd in p:
        if cmd == "R":
            flag += 1
        elif cmd == "D":
            if queue:
                if flag % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print ("error")
                break
    else:
        if flag % 2 == 0:
            print ("[" + ",".join(queue)+"]")
        else:
            queue.reverse()
            print("[" + ",".join(queue)+"]")