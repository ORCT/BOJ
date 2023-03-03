n = int(input())
t = [0 for _ in range(91)]
t[1] = 1
for i in range(2, 91):
    t[i] = 1 + sum(t[:i-1])
print(t[n])