import sys
ssr=sys.stdin.readline

line = list(map(int, ssr().split()))
line1 = sorted(line)
if line == line1:
    print('ascending')
else:
    if line == line1[::-1]:
        print('descending')
    elif line != line1:
        print('mixed')