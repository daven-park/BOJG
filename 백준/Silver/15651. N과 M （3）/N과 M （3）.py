import sys

N, M = map(int, input().split())

arr = []

isUsed = [False] * 10
def func(k : int):
    if k == M:
        print(" ".join(map(str, arr[:M])))
        return

    for i in range(1, N + 1):
        # if not isUsed[i]:
        #     isUsed[i] = True
            arr.append(i)
            func(k + 1)
            arr.pop()
            # isUsed[i] = False
func(0)