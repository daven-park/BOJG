import sys

N, M = map(int, input().split())

numbers = list(map(int, input().split()))
numbers.sort()
selected = []
visited = [False] * N

def combination(count, start):
    if count == M:
        print(*selected)
        return
    prev = None
    for i in range(start, N):
        if not numbers[i] == prev:
            selected.append(numbers[i])
            combination(count + 1, i + 1)
            selected.pop()
            prev = numbers[i]

combination(0, 0)