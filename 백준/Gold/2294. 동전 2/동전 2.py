import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

queue = deque()
visited = [False] * (K + 1)
coins = []
for i in range(N):
    num = int(input())
    coins.append(num)
    queue.append((num, 1))

ans = 100001
while queue:
    current, cnt = queue.popleft()
    if current == K:
        ans = min(cnt, ans)
    for coin in coins:
        next_val = coin + current 
        if next_val > K: continue
        if visited[next_val]: continue
        queue.append((coin + current, cnt + 1))
        visited[next_val] = True

if ans == 100001:
    print(-1)
else:
    print(ans)