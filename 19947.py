'''import math

h,y = map(int, input().split())
t = [0 for _ in range(11)]
t[0] = h
for i in range(1,11):
    t[i] = math.floor(t[i-1]*1.05)

for i in range(3,11):
    t[i] = max(math.floor(t[i-3]*1.2),t[i])
    # t[i+2] = t[i]
    # t[i+1] = t[i]
    
for i in range(5,11):
    t[i] = max(math.floor(t[i-5]*1.35),t[i])
#     for j in range(5):
#         t[i+j][2] = t[i][2]
print(t[y])'''

import math

def sol(i):
    if i==11:
        return
    if i<3:
        t[i] = max(math.floor(t[i-1]*1.05),t[i])
        sol(i+1)
    elif i>=3 and i<5:
        t[i] = max(math.floor(t[i-1]*1.05),math.floor(t[i-3]*1.2),t[i])
        sol(i+1)
    else:
        t[i] = max(math.floor(t[i-1]*1.05),math.floor(t[i-3]*1.2),math.floor(t[i-5]*1.35),t[i])
        sol(i+1)
        
h,y = map(int, input().split())
t = [0 for _ in range(11)]
t[0]=h
sol(1)
print(t[y])