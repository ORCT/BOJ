import sys
import math
limit = 123456
eratos = [1] * (2 * limit + 1)
eratos[0] = 0
eratos[1] = 0
for i in range(2, int(math.sqrt(len(eratos)))):
    if eratos[i]:
        for j in range(i + i, len(eratos), i):
            eratos[j] = 0
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        print(sum(eratos[n+1:(2*n)+1]))