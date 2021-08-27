a,b = input().split()
a = list(a)
a.reverse()
b = list(b)
b.reverse()
a = int(''.join(a))
b = int(''.join(b))
if a>b:
    print(a)
else:
    print(b)