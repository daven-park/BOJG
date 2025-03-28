import heapq
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

pq = []

V, E = map(int, input().split())

parent = [0] * (V + 1)

for i in range(V + 1):
    parent[i] = i
for i in range(E):
    s, e, w = map(int, input().split())
    heapq.heappush(pq, (w, s, e))
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


result = 0
useEdges = 0
while useEdges < V - 1:
    w, s, e = heapq.heappop(pq)
    if find(s) != find(e):
        union(s, e)
        result += w
        useEdges += 1

print(result)
