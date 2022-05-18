x = input()
cnt = 0
a = 0
while int(x)>=10:
    for i in x:
        a += int(i)
    x = str(a)
    cnt += 1
    a = 0
print(cnt)
if int(x)%3 ==0: 
      print("YES")
else:
       print("NO")