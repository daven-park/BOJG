import sys

N, S = map(int, input().split())

arr = list(map(int, input().split()))
ans = 0

def func(current, total):
    global ans
    if current == N:
        if total == S:
            ans += 1
        return

    func(current + 1, total)
    func(current + 1, total + arr[current])

func(0, 0)
if S == 0: ans -= 1
print(ans)
