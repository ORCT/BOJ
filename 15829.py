'''
import string

char = string.ascii_lowercase
r = int(input())
s = input()
result = 0
for i in range(r):
    result += ((char.index(s[i])+1) * (31**i))
print(result%1234567891)
'''
import string

low = string.ascii_lowercase
char = {}
for i in range(len(low)):
    char[low[i]] = i+1
n = int(input())
s = input()
result = 0
a=0
for i in s:
    result += char[i]*(31**a)
    a+=1
print(result%1234567891)
