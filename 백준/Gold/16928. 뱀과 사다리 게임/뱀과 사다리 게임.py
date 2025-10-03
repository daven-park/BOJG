import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

board = [0] * 101
snake_ladder = defaultdict(int)
for i in range(N + M):
    u, v = map(int, input().split())
    snake_ladder[u] = v

visited = [False] * 101
q = deque()
q.append((1, 0))
visited[1] = True
while q:
    current, dice_count = q.popleft()
    if current == 100:
        print(dice_count)
        break
    for dice in range(1, 7):
        next_pos = current + dice
        if next_pos > 100: continue
        if snake_ladder[next_pos]:
            next_pos = snake_ladder[next_pos]
        if visited[next_pos]: continue
        visited[next_pos] = True
        q.append((next_pos, dice_count + 1))