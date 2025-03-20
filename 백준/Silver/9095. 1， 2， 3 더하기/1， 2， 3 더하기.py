import sys

#정수 4를 1, 2, 3의 합으로 나타내는 방법은 총 7가지가 있다. 합을 나타낼 때는 수를 1개 이상 사용해야 한다.

T = int(input())

arr = [1, 2, 3]
for t in range(T):
    N = int(input())
    ans = 0
    def func(k, selected, count):
        global ans
        if k == count:
            if sum(selected) == N:
                ans += 1
            return
        for i in range(0, len(arr)):
            func(k + 1, selected + [arr[i]], count)

    for i in range(1, N + 1):
        func(0, [], i)

    print(ans)