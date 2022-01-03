import sys
from collections import deque

def push(X) -> None:
    stack.appendleft(X)


def pop() -> None:
    if not stack:
        print (-1)
    else:
        print (stack.popleft())


def size() -> None:
    print (len(stack))


def empty() -> None:
    if not len(stack):
        print (1)
    else:
        print (0)


def top() -> None:
    if not stack:
        print (-1)
    else:
        print (stack[0])
    

if __name__ == "__main__":
    N = int(input())
    stack = deque()

    command_dict = {
        'push': push,
        'pop' : pop,
        'size' : size,
        'empty': empty,
        'top': top
    }
    
    for _ in range(N):
        command = sys.stdin.readline().split()
        if len(command) > 1:
            command_dict[command[0]](int(command[1]))
        else:
            command_dict[command[0]]()
