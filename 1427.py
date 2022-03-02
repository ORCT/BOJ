s = input()
n = [int(i) for i in s]
n.sort(reverse= True)
for i in range(len(n)):
    print(n[i],end='')