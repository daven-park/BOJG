import sys

class MaxHeap:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)
        self.bubbleUp()

    def pop(self):
        if len(self.items) == 0:
            return None
        minvalue = self.items[0]
        self.items[0] = self.items[self.size() - 1]
        self.items.pop()
        self.bubbleDown()
        return minvalue

    def bubbleUp(self):
        idx = self.size() - 1
        while idx > 0:
            parent_idx = (idx - 1) // 2
            if self.items[parent_idx] <= self.items[idx]: break
            self.items[idx], self.items[parent_idx] = self.items[parent_idx], self.items[idx]
            idx = parent_idx

    def bubbleDown(self):
        idx = 0
        while idx * 2 + 1 < self.size():
            left_child = idx * 2 + 1
            right_child = idx * 2 + 2
            smaller_child = right_child if right_child < self.size() and self.items[right_child] < self.items[left_child] else left_child

            if self.items[idx] <= self.items[smaller_child]: break;

            self.items[idx], self.items[smaller_child] = self.items[smaller_child], self.items[idx]
            idx = smaller_child


N = int(input())
input = sys.stdin.readline
result = []
maxheap = MaxHeap()
for i in range(N):
    num = int(input())
    if num == 0:    # 출력
        if maxheap.size() != 0:
            result.append(str(-1 * maxheap.pop()))
        else:
            result.append(str(0))
    else:
        maxheap.push(-1 * num)

print('\n'.join(result))