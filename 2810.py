n = int(input())
s = input()
ans = 1
cnt = 0
for i in range(n):
    if s[i] == 'L':
        cnt += 1
    if cnt % 2 == 0:
        ans += 1
        
print(min(ans, len(s)))