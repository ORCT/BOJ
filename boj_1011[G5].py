import sys
T = int(input())
for i in range(T):
    x,y = map(int,sys.stdin.readline().split())
    max_distance=0
    while 1:
        max_distance+=1
        if y-x>=max_distance**2 and y-x<(max_distance+1)**2:
            break
    if y-x == max_distance**2:
        print(max_distance*2-1)
    else:
        if y-x>max_distance*2 and y-x<=max_distance**2+max_distance:
            print(max_distance*2)
        elif y-x>=(max_distance+1)**2-max_distance and y-x<(max_distance+1)**2:
            print((max_distance+1)*2-1)