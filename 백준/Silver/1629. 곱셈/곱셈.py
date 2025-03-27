import sys

input = sys.stdin.readline

A, B, C = map(int, input().split())

def solve(A, B, C):
    if B == 1:
        return A % C
    half = solve(A, B // 2, C)
    if B % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * A) % C

print(solve(A, B, C))