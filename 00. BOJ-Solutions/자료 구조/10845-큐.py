import sys
input = sys.stdin.readline

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if not self.queue:
            print(-1)
        else:
            num = self.queue[0]
            print (num)
            del self.queue[0]

    def size(self):
        print(len(self.queue))

    def empty(self):
        if not self.queue:
            print(1)
        else:
            print(0)

    def front(self):
        if not self.queue:
            print(-1)
        else:
            print(self.queue[0])

    def back(self):
        if not self.queue:
            print(-1)
        else:
            print(self.queue[-1])

Q = Queue()
N = int(input())
command = {'pop':Q.pop, 'size':Q.size, 'front':Q.front, 'back':Q.back, 'empty':Q.empty}
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        Q.push(cmd[1])
    else:
        command[cmd[0]]()