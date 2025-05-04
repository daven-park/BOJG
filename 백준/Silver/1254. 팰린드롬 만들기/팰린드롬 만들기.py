import sys

input = sys.stdin.readline

s = input().rstrip()

rev = s[::-1]

def is_palindrome(s):
    return s == s[::-1]

for i in range(len(s)):
    if is_palindrome(s[i:]):
        print(len(s) + i)
        break