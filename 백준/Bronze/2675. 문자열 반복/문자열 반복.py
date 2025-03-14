import sys

T = int(input())

for _ in range(T):
    R, string = sys.stdin.readline().split()
    stringlist = [char for char in string]
    ans = ""

    for i in range(len(stringlist)):
        for _ in range(int(R)):
            ans += str(stringlist[i])

    print(ans)