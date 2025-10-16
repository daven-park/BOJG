import sys

input = sys.stdin.readline

L, C = map(int, input().split())

alpabets = sorted(input().split())

def dfs(start, selected, cnt):
    if len(selected) == L:
        if cnt >= 1 and L - cnt >= 2:
            print("".join(selected))
        return
    for i in range(start, C):
        if C - i < L - len(selected): break
        dfs(i + 1, selected + [alpabets[i]], cnt + (alpabets[i] in set("aeiou")))

dfs(0, [], 0)