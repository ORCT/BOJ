from string import ascii_uppercase

uppers = list(ascii_uppercase)
s = input()
ans = 0
start = 'A'
for i in s:
    start_idx = uppers.index(start)
    next_idx = uppers.index(i)
    if next_idx > start_idx:
        ans += min((next_idx - start_idx), (start_idx + 26 - next_idx))
    else:
        ans += min((start_idx - next_idx), (next_idx + 26 - start_idx))
    start = i
print(ans)