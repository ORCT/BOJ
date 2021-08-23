import sys

S=sys.stdin.readline()
q=int(sys.stdin.readline())

for i in range(q):
    line=sys.stdin.readline().split()
    alpha=line[0]
    l=int(line[1])
    r=int(line[2])
    count=0
    for i in range(l,r+1):
        if alpha==S[i]:
            count=count+1
    print(count)