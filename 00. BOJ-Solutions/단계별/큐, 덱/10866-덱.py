class Deque(object):
    def __init__(self):
        self.deque = []

    def push_front(self, X):
        self.deque.insert(0, int(X))
        print (int(X))

    def push_back(self, X):
        self.deque.append(int(X))
        print (int(X))

    def pop_front(self):
        if len(self.deque) >= 1:
            print (self.deque.pop(0))
        else:
            print (-1)

    def pop_back(self):
        if len(self.deque) >= 1:
            print (self.deque.pop())
        else:
            print (-1)

    def size(self):
        print (len(self.deque))


    def empty(self):
        if len(self.deque) == 0:
            print (1)
        else:
            print (0)

    def front(self):
        if len(self.deque) >= 1:
            print (self.deque[0])
        else:
            print (-1)

    def back(self):
        if len(self.deque) >= 1:
            print (self.deque[-1])
        else:
            print (-1)

if __name__ == "__main__":
    N = int(input())
    deque = Deque()

    cmd_map = {
        'push_front': deque.push_front,
        'push_back': deque.push_back,
        'pop_front': deque.pop_front,
        'pop_back': deque.pop_back,
        'size': deque.size,
        'empty': deque.empty,
        'front': deque.front,
        'back': deque.back
    }

    for i in range(N):
        statement = input().split()

        if len(statement) == 1:
            cmd = statement[0]
            cmd_map[cmd]()
        
        else:
            cmd, value = statement
            cmd_map[cmd](value)

        # result = deque.cmd(value)
        # print (result)
