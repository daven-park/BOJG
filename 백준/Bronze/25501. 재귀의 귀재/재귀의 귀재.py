import sys
from collections import deque


T = int(input())

def recursion(S, left, right):
    global ans
    ans += 1
    if left >= right: return 1
    elif S[left] != S[right]: return 0
    else: return recursion(S, left + 1, right - 1)

def isPalindrome(S):
    return recursion(S, 0, len(S) - 1)

for i in range(T):
    ans = 0
    print(isPalindrome(input().strip()), ans)