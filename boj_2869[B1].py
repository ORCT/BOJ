A, B, V = map(int, input().split())
n=int(V/(A-B)-A)
while True:
    if (A-B)*n+A>=V:
      print(n+1)
      break
    else:
        n += 1