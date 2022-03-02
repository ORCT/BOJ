import sys
ssr = sys.stdin.readline

num = list(map(int, ssr().split()))
ans = 0
for i in range(5):
    ans += num[i]**2
print(ans%10)