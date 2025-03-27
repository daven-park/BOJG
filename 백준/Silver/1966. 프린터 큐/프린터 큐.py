import heapq
import sys
from collections import deque

input = sys.stdin.readline

# 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면,
# 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.

tc = int(input())

for t in range(tc):
    N, M = map(int, input().split()) # N = 문서의 개수, M = M번째에 위치한 인쇄물
    queue = deque()
    nums = list(map(int, input().split()))
    priority = []
    for i in range(N):
        queue.append([nums[i], i])
        heapq.heappush(priority, -nums[i])
    cnt = 0
    while queue:
        current = queue[0]
        if current[0] == -priority[0]:  # 큐의 맨앞이 우선도가 가장 높은 값일때
            if current[1] == M:         # 찾고있는 인덱스의 문서가 맞으면
                print(cnt + 1)
                break
            queue.popleft()
            heapq.heappop(priority)
            cnt += 1
        else:                           # 우선도가 가장 높은 값이 아니라면 나올때까지 뒤로 보낸다
            queue.append(queue.popleft())