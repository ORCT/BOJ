'''
1~n까지의 수를 공백없이 차례대로 썼다
수를 지우긴 했어도 자리를 재배치 하지는 않았다
앞의 수도 수지만 맨 뒤의 수를 가지고 추측을 할 수 있을 것이다
입력은 최대 3000자리다.
3000자리를 전부 9로 줬다고 치면 9, 19, 29, 39, ..., 29999 정도이려나 최대 30000이다 이말이지
그러면 충분히 while로도 풀릴듯

숫자를 하나씩 떼어낸 다음에
바로 뒤의 칸에 나오는 숫자가 최소한 지금의 나보다 커야 한다.
2번 입력을 봤을 때 2, 3, 4, 0, 9, 2 로 나눌 수 있는데 4 다음에 나오는 0은 4보다 큰 수 중에서 가능한 최솟값이므로 10이되고 그 다음의 9는 19 따라서 n의 최솟값은 20이 된다.

예제 6
1111111의 경우 1, 10, 11, 12, 13, 14로 14가 최솟값이다. 이유는 진짜건 아니건 14로 나타낼 수 있기 때문(11에다 1을 2개 써버리면 되니까)
이 부분을 어떻게 체크할 것인가

숫자를 키워가면서 지워버려야하나
while문에서 숫자를 키워가면서 일치하는 숫자가 있으면 지우는 건 어떨까
'''

'''line = [int(digit) for digit in input()]
for i in range(1, len(line)):
    if line[i-1] < line[i]:
        continue
    else:
        check = str(line[i])
        while True:
            line[i] += 1
            if check in str(line[i]) and line[i-1] < line[i]:
                break
print(line[-1])'''

line = input()
ans = 0
while len(line):
    ans += 1
    check = str(ans)
    while len(check) > 0 and len(line) > 0:
        if check[0] == line[0]:
            line = line[1:]
        check = check[1:]
print(ans)