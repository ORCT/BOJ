n = [i for i in range(1,31)]
while 1:
    try:
        n.remove(int(input()))
    except:
        break
print(*n, sep='\n')