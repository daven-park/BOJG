import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque([num for num in range(1, N + 1)])
picked = []
cnt = 0
while queue:
    if cnt == K - 1:
        picked.append(queue.popleft())
        cnt = 0
    else:
        queue.append(queue.popleft())
        cnt += 1

print("<" + ", ".join(map(str, picked)) + ">")

sys.stdout.close()
