s = input()
check = 1
num = ''
ans = []
for i in s:
    if i == '-': 
        ans.append(check*int(num))
        num=''
        check = -1
    elif i == '+':
        ans.append(check*int(num))
        num=''
    else:
        num += i
ans.append(check*int(num))
# print(ans)
print(sum(ans))