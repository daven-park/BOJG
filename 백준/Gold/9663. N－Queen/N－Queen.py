import sys

N = int(input())

ans = 0
pos = [0] * N
flag_a = [False] * N
flag_b = [False] * (2 * N - 1)
flag_c = [False] * (2 * N - 1)

def setQueen(i: int) -> None:
    global ans
    for j in range(N):
        if not flag_a[j] and not flag_b[i + j] and not flag_c[i - j + (N - 1)]:
            pos[i] = j
            if i == N - 1:
                ans += 1
            else:
                flag_a[j] = True
                flag_b[i + j] = True
                flag_c[i - j + (N - 1)] = True
                setQueen(i + 1)
                flag_a[j] = False
                flag_b[i + j] = False
                flag_c[i - j + (N - 1)] = False

setQueen(0)
print(ans)