t = int(input())
table = [0 for _ in range(12)]
table[1] = 1
table[2] = 2
table[3] = 4
for i in range(4,12):
    table[i] = table[i-1]+table[i-2]+table[i-3]
for _ in range(t):
    a = int(input())
    print(table[a])