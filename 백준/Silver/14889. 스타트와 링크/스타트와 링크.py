import sys
input = sys.stdin.readline

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

selected = [False] * N
answer = float('inf')

def calc_diff():
    start_team = []
    link_team = []

    for i in range(N):
        if selected[i]:
            start_team.append(i)
        else:
            link_team.append(i)

    start_sum = 0
    link_sum = 0

    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            a, b = start_team[i], start_team[j]
            start_sum += S[a][b] + S[b][a]

            c, d = link_team[i], link_team[j]
            link_sum += S[c][d] + S[d][c]

    return abs(start_sum - link_sum)


def dfs(idx, count):
    global answer
    if count == N // 2:
        answer = min(answer, calc_diff())
        return
    
    if idx >= N: return

    selected[idx] = True
    dfs(idx + 1, count + 1)
    selected[idx] = False
    dfs(idx + 1, count)

dfs(0, 0)
print(answer)