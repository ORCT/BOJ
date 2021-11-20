#a,b,v = map(int, input().split())
#n = 0
#i = 0
#while 1:
#    i += 1
#    n += a
#    if n >= v:
#        print(i)
#        break
#    else:
#        n -= b
#O(n)
import math
a,b,v = map(int, input().split())
n = math.ceil((v-a)/(a-b))
print(n+1)