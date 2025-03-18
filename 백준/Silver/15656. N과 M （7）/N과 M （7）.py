import sys

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
selected = []
isUsed = [False] * 10
def func(k : int, start : int):
    if k == M:
        print(" ".join(map(str, selected)))
        return

    for i in range(0, N):
            selected.append(arr[i])
            func(k + 1, i)
            selected.pop()

func(0, 0)