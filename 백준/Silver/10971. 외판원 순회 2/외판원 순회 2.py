import sys

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]

ans = 10**9
# 전체 순회를 했을 때 경로의 최댓값을 정답과 비교해서 교환한다.
# 도시 i, j는 i에서 j로 가는데 드는 비용
# 출발해 N개의 도시를 모두 거쳐 다시 원래의 도시로 돌아오는 순회 여행 경로를 계획
def dfs(start, now, cost, visited):
    global ans
    if all(visited):    
        if maps[now][start] != 0:             
            ans = min(ans, cost + maps[now][start])
        return

    for i in range(N):
        if not visited[i] and maps[now][i] != 0:
            visited[i] = True
            dfs(start, i, cost + maps[now][i], visited)
            visited[i] = False

for i in range(N):
    visited = [False] * N
    visited[i] = True
    dfs(i, i, 0, visited)

print(ans)