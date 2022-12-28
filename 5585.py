price = int(input())
change = 1000 - price
ans = 0
coin = [500, 100, 50, 10, 5, 1]
for i in coin:
    coin_num = change // i
    change -= i*coin_num
    ans += coin_num
print(ans)