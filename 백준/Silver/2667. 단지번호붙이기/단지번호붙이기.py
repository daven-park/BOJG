import sys

"""
문제 설명 :
1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 
철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다
"""

def dfs(x, y):
    global maps
    visited[x][y] = True
    house = 1
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx >= N or ny >= N or visited[nx][ny]:
            continue
        if maps[nx][ny] == 0:
            continue
        house += dfs(nx, ny)
    return house

input = sys.stdin.readline

N = int(input())

maps = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
houses = []
danji = 0
for i in range(N):
    for j in range(N):
        if visited[i][j] or maps[i][j] == 0: continue
        houses.append(dfs(i, j))
        danji += 1

result = []
result.append(str(danji))
houses.sort()

for house in houses:
    result.append(str(house))
    
sys.stdout.write("\n".join(result))
sys.stdout.close()