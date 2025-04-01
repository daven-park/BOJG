import sys
from collections import deque

input = sys.stdin.readline

# 빈곳 '.' 물 '*' 돌 'X' 비버굴 'D' 고슴도치 'S'

# 매 분마다 4방 이동

# 물이 있는 칸 매 분마다 채워짐

# 물과 고슴도치는 돌 통과 못함
# 고슴도치는 물로 이동 불가
# 물도 비버 소굴 이동 불가

R, C = map(int, input().split())

forest = [[char for char in input().strip()] for _ in range(R)]

dest = None
start = None
water_start = []
flood = [[-1] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if forest[i][j] == 'D':
            dest = (i, j)
        if forest[i][j] == 'S':
            start = (i, j)
        if forest[i][j] == '*':
            water_start.append((i, j, 0))
            flood[i][j] = 0

def flooding():
    queue = deque(water_start)
    while queue:
        curX, curY, time = queue.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = dx + curX
            ny = dy + curY
            if nx < 0 or ny < 0 or nx >= R or ny >= C: continue # 범위 체크
            if flood[nx][ny] != -1: continue    # 방문 체크
            if forest[nx][ny] == 'X' or forest[nx][ny] == 'D': continue # 돌, 비버굴 체크
            queue.append((nx, ny, time + 1))
            flood[nx][ny] = time + 1

ans = "KAKTUS"
visited = [[False] * C for _ in range(R)]
def hedgehog_move():
    global ans
    queue = deque()
    x, y = start
    queue.append((x, y, 0))
    visited[x][y] = True
    while queue:
        curX, curY, time = queue.popleft()
        if curX == dest[0] and curY == dest[1]: # 목적지 도착하면 정답에 입력
            ans = str(time)
            return
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = dx + curX
            ny = dy + curY
            if nx < 0 or ny < 0 or nx >= R or ny >= C: continue
            if visited[nx][ny]: continue
            if forest[nx][ny] == 'X' or forest[nx][ny] == '*':continue
            if flood[nx][ny] <= time + 1 and flood[nx][ny] != -1 : continue
            queue.append((nx, ny, time + 1))
            visited[nx][ny] = True

flooding()
hedgehog_move()
print(ans)