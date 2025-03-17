import sys

N, r, c = map(int, input().split())

def z_func(N, r, c):
    if N == 0:
        return 0
    half = 2 ** (N - 1)
    if r < half and c < half:
        return z_func(N - 1, r, c)
    elif r < half <= c:
        return half * half + z_func(N - 1, r, c - half)
    elif c < half <= r:
        return 2 * half * half + z_func(N - 1, r - half, c)
    elif r >= half and c >= half:
        return 3 * half * half + z_func(N - 1, r - half, c - half)

print(z_func(N, r, c))