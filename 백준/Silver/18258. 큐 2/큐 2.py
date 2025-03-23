import sys

class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # head에서 추가하는 함수
    def enqueue(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # tail에서 제거하는 함수
    def dequeue(self):
        if self.head is None:
            return None
        pop_node = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return pop_node.data

    # 제일 앞에 있는 값 확인
    def front(self):
        return self.head.data if self.head else None

    # 제일 뒤에 있는 값 확인
    def back(self):
        return self.tail.data if self.tail else None

    #연결리스트가 비었는지 확인
    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.size

class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def push(self, data):
        self.linkedlist.enqueue(data)

    def pop(self):
        return self.linkedlist.dequeue()

    def is_empty(self):
        return self.linkedlist.is_empty()

    def front(self):
        return self.linkedlist.front()

    def back(self):
        return self.linkedlist.back()

    def __len__(self):
        return len(self.linkedlist)


def operation(commands, queue, result):
    cmd = commands[0]
    data = -1
    if len(commands) == 2:
        data = int(commands[1])

    if cmd == "push":
        queue.push(data)
    elif cmd == "front":
        result.append(str(queue.front() if queue.front() is not None else -1))
    elif cmd == "back":
        result.append(str(queue.back() if queue.back() is not None else -1))
    elif cmd == "size":
        result.append(str(len(queue)))
    elif cmd == "empty":
        result.append(str(1 if queue.is_empty() else 0))
    elif cmd == "pop":
        state = queue.pop()
        if state:
            result.append(str(state))
        else:
            result.append("-1")

input = sys.stdin.readline
result = []

N = int(input())
queue = Queue()
for i in range(N):
    command = list(map(str, input().split()))
    operation(command,queue, result)

sys.stdout.write("\n".join(result))
sys.stdout.close()