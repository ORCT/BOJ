'''n, l, w, h = map(int, input().split())
print(f'{(l * w * h / n) ** (1/3):.9f}')'''

n, l, w, h = map(int, input().split())
top, bot = min(l, w, h), 0
for _ in range(40):
    mid = (top + bot)/2
    if (l//mid)*(w//mid)*(h//mid) >= n:
        bot = mid
    else:
        top = mid
print(f'{top:.10f}')