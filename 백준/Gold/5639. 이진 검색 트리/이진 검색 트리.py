import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

def postorder(_lst):
    if len(_lst) == 0:
        return

    l_subtree, r_subtree = [], []
    mid = _lst[0]
    for i in range(1, len(_lst)):
        if _lst[i] > mid:
            l_subtree = _lst[1:i]
            r_subtree = _lst[i:]
            break
    else:
        l_subtree = _lst[1:]

    postorder(l_subtree)
    postorder(r_subtree)
    print(mid)

postorder(preorder)