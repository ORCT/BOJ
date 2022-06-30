n = int(input())
m = list(map(int, input().split()))
state = 0
ans = 0
for i in m:
    if i == state:
        ans += 1
        state += 1
        if state == 3:
            state = 0
print(ans)