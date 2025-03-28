import sys

input = sys.stdin.readline

N, M = map(int, input().split())

parent = [0] * (N + 1)

for i in range(1, N + 1):
    parent[i] = i

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for _ in range(M):
    s, e = map(int, input().split())
    if find(s) != find(e):
        union(s, e)

for i in range(1, N + 1):
    find(i)

print(len(set(parent[1:])))