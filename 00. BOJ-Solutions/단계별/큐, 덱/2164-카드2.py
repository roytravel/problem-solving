from collections import deque

def fail():
    for i in range(N):
        if len(queue) > 1:
            del queue[0]
            temp = queue[0]
            del queue[0]
            queue.append(temp)
        else:
            print (queue[0])

def success(queue):
    for i in range(len(queue)):
        if len(queue) == 1:
            print (queue[0])
            break
        queue.popleft()
        queue.append(queue[0])
        queue.popleft()

if __name__ == "__main__":
    N = int(input())
    queue = deque([i for i in range(1, N + 1)])
    success(queue)