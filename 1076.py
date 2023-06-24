'''t = {'black':'0',
     'brown':'1',
     'red':'2',
     'orange':'3',
     'yellow':'4',
     'green':'5',
     'blue':'6',
     'violet':'7',
     'grey':'8',
     'white':'9'}

print(int(t[input()]+t[input()]+'0'*int(t[input()])))'''

t = {'black':0,
     'brown':1,
     'red':2,
     'orange':3,
     'yellow':4,
     'green':5,
     'blue':6,
     'violet':7,
     'grey':8,
     'white':9}

print((t[input()]*10+t[input()])*(10**t[input()]))