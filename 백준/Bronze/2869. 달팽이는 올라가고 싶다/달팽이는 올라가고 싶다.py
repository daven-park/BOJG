import sys

A, B, V = map(int, input().split())

time = 1

if (V - A) % (A - B) == 0:
    time += (V - A) // (A - B)
else:
    time += ((V - A) // (A - B)) + 1
    
if A >= V: time = 1

print(time)