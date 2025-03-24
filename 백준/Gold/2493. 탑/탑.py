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

"""
문제 설명 :
첫째 줄에 탑의 수를 나타내는 정수 N이 주어진다. 
N은 1 이상 500,000 이하이다. 둘째 줄에는 N개의 탑들의 높이가 직선상에 놓인 순서대로 하나의 빈칸을 사이에 두고 주어진다.
 탑들의 높이는 1 이상 100,000,000 이하의 정수이다.
"""

input = sys.stdin.readline

N = int(input())

towerheights = list(map(int, input().split()))

stack = Stack()
m = len(towerheights)
signals = [0] * (N + 1)

for index, current_height in enumerate(towerheights[::-1]):
    tower_number = m - index
    if stack.empty():     #비어있으면 그냥 추가
        stack.push((tower_number, current_height))
    else:
        # top보다 큰 수가 들어오면 pop하고 뺸 값의 신호 인덱스 추가 후 현재 타워 push
        if stack.top()[1] < current_height:
            while not stack.empty() and stack.top()[1] < current_height:
                tower = stack.pop()
                signals[tower[0]] = tower_number
            stack.push((tower_number, current_height))
        else:
            stack.push((tower_number, current_height))
result = [signals[num] for num in range(1, N + 1)]
sys.stdout.write(" ".join(map(str, result)))
sys.stdout.close()