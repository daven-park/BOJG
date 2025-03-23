import sys

class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.size == 0: return -1
        self.size -= 1
        return self.stack.pop()

    def size(self):
        return self.size

    def empty(self):
        return 0 if self.size != 0 else 1

    def top(self):
        if self.size == 0: return -1
        return self.stack[self.size - 1]


def solution(commands, result):
    global stack
    cmd = commands[0]
    if cmd == "push":
        stack.push(commands[1])
    elif cmd == "pop":
        result.append(str(stack.pop()))
    elif cmd == "size":
        result.append(str(stack.size))
    elif cmd == "empty":
        result.append(str(stack.empty()))
    elif cmd == "top":
        result.append(str(stack.top()))


input = sys.stdin.readline
result = []

stack = Stack()

N = int(input())
for _ in range(N):
    commands = list(map(str, input().split()))
    solution(commands, result)


sys.stdout.write("\n".join(result))
sys.stdout.close()