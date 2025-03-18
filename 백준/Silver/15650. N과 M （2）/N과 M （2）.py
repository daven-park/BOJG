import sys

N, M = map(int, input().split())

arr = []

isUsed = [False] * 10
def func(k : int, start: int):
    if k == M:
        print(" ".join(map(str, arr[:M])))

    for i in range(start, N + 1):
            arr.append(i)
            func(k + 1, i + 1)
            arr.pop()
func(0, 1)