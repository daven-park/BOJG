import sys
from collections import defaultdict, deque

input = sys.stdin.readline

T = int(input())
for tc in range(T):
    graph = defaultdict(list)

    V, E = map(int, input().split())
    for i in range(E):
        s, e = map(int, input().split())
        graph[s].append(e)
        graph[e].append(s)

    visited = [0] * (V + 1)
    answer = "YES"    # 이분 그래프 불가능하면 True

    def bfs(node):
        global answer
        queue = deque()
        queue.append(node)
        visited[node] = 1

        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if visited[neighbor] == visited[current]:  # 인접한 노드가 현재 노드와 같은 색이면 이분 x
                    answer = "NO"
                    return
                if visited[neighbor] == 0:
                    queue.append(neighbor)
                    visited[neighbor] = visited[current] * -1


    for i in range(1, V + 1):
        if answer == "NO":
            break
        if visited[i] == 0:
            bfs(i)
    print(answer)