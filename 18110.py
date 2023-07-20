import sys
ssr = sys.stdin.readline

n = int(ssr())
scores = [int(ssr()) for _ in range(n)]
scores.sort()
if n == 0:
    print(0)
elif n < 4:
    print(round(sum(scores)/len(scores) + 1e-7))
else:
    cut = round(n*15/100 + 1e-7)
    print(round(sum(scores[cut:-cut])/len(scores[cut:-cut]) + 1e-7))


'''
f-string 도 오사오입을 따른다
print(sum([8, 8, 17, 22][1:-1]))
print(25/2)
print(f'{23/2:.0f}')
print(f'{2.5:.0f}')
print(f'{2.25:.1f}')
'''