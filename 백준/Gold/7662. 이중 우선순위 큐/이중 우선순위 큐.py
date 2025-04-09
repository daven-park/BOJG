import heapq
import sys

input = sys.stdin.readline

# k <= 1000000

# I n -- insert n
# D 1 pop max
# D -1 pop min

T = int(input())
for t in range(T):
    K = int(input())
    visited = [False] * ( K + 1)
    maxq = []
    minq = []
    for i in range(K):
        cmd, val = map(str, input().split())
        val = int(val)
        if cmd == "I":
            heapq.heappush(maxq, (-val, i))
            heapq.heappush(minq, (val, i))
            visited[i] = True
        elif cmd == "D":
            # 최솟값 삭제
            if val < 0:
                while minq and not visited[minq[0][1]]:
                    heapq.heappop(minq)
                if minq:
                    _, idx = heapq.heappop(minq)
                    visited[idx] = False
            # 최댓값 삭제
            else:
                while maxq and not visited[maxq[0][1]]:
                    heapq.heappop(maxq)
                if maxq:
                    _, idx = heapq.heappop(maxq)
                    visited[idx] = False

    while maxq and not visited[maxq[0][1]]:
        heapq.heappop(maxq)
    while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)

    if not minq or not maxq:
        print("EMPTY")
    else:
        print(-maxq[0][0], minq[0][0])