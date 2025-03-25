import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

maps = [[0 for _ in range(N + 1)]for _ in range(N + 1)]
K = int(input())
apples = set()
for _ in range(K):
    x, y = map(int, input().split())
    apples.add((x, y))


L = int(input())
head_turn = deque([])
for i in range(L):  # C = L은 왼쪽으로 D는 오른쪽으로 돌린다. X = X초 후에 실행
    x, c = map(str, input().split())
    head_turn.append((int(x), c))

time = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
snake = deque()
snake.append((1, 1))
current_dir = 0

while True:
    # 방향 변환 시간과 같으면 변환
    if head_turn and time == head_turn[0][0]:
        _, turn_dir = head_turn.popleft()
        current_dir = (current_dir - 1) % 4 if turn_dir == 'L' else (current_dir + 1) % 4

    curX, curY = snake[-1]   # 뱀의 머리

    # 머리를 이동시킨다
    nx = curX + dx[current_dir]
    ny = curY + dy[current_dir]
    # 벽에 부딪히면 끝난다.
    if nx <= 0 or ny <= 0 or nx > N or ny > N: break

    # 내 몸에 부딪히면 끝난다
    if (nx, ny) in snake: break

    snake.append((nx, ny))

    # 사과가 있는 경우: 사과 제거 후 꼬리는 그대로 유지 (뱀 길이 증가)
    if (nx, ny) in apples:
        apples.remove((nx, ny))
    else:
        # 사과가 없으면 꼬리 제거 (뱀 길이 유지)
        snake.popleft()
    time += 1

print(time + 1)