from collections import deque
import sys
ssr = sys.stdin.readline

n, k = map(int, ssr().split())
s = deque([i for i in range(1, n+1)])
print('<', end='')
while s:
   for i in range(k - 1):
       s.append(s.popleft())
   print(s.popleft(), end='')
   if s:
       print(', ', end='')
print('>')