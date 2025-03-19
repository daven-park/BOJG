import sys

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()
selected = []
visited = [False] * N
def permu(count):
    if count == M:
        print(*selected)
        return
    prev = 0
    for i in range(0, N):
        if not visited[i] and numbers[i] != prev:
            visited[i] = True
            selected.append(numbers[i])
            permu(count + 1)
            visited[i] = False
            selected.pop()
            prev = numbers[i]

permu(0)