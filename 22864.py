a, b, c, m = map(int, input().split())

work = 0
tired = 0

for _ in range(24):
    if tired + a > m:
        tired = 0 if tired < c else tired - c
    else:
        tired += a
        work += b

print(work)