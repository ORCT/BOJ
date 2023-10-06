'''
부분수열 2번인가 3번인가 했는데 또 기억 안나네

바이토닉 : 중간이 제일 크거나, 맨앞이 제일 크거나, 맨 뒤가 제일 크거나가 순서대로 배치

증가 수열 이랑 감소 수열에 대해 배열을 각각 만들고 서로 값을 다 합치면 될 거 같은데

필요한 기능
입력 받기
증가 수열 반환
감소 수열 반환
합치기
출력하기

그럼 이제 증가 수열의 길이를 어떻게 체크할 것이냐
첫번째 원소를 기준값으로 정해
원소를 순서대로 탐색해
만약에 기준값보다 큰 원소가 나오면
기준값을 해당 원소로 갱신하고 카운트를 하나 올려
만약에 이미 값이 있다면 더 큰 값으로 갱신해
그렇게 시작점을 n까지의 원소로 정하는 거지
복잡도는 n(n-1)/2 겠네
이걸 두번 2백만번 도네

뛰어넘을수도 있다는 걸 생각못했네
'''

'''
def increase(array):
    result = [1]
    check = [array[0]]
    for i in range(1, n):
        if len(check) == 1:
            if check[0] > array[i]:
                check[0] = array[i]
            else:
                check.append(array[i])
        else:
            if check[-1] > array[i] > check[-2]:
                check[-1] = array[i]
            elif check[-1] < array[i]:
                check.append(array[i])
        result.append(len(check))
    return result

def decrease(array):
    result = [1]
    check = [array[0]]
    for i in range(1, n):
        if len(check) == 1:
            if check[0] > array[i]:
                check[0] = array[i]
            else:
                check.append(array[i])
        else:
            if check[-1] > array[i] > check[-2]:
                check[-1] = array[i]
            elif check[-1] < array[i]:
                check.append(array[i])
        result.append(len(check))
    return result[::-1]

def add_array(array1, array2):
    result = [0 for _ in range(n)]
    for i in range(n):
        result[i] = array1[i] + array2[i]
    return result

n = int(input())
a = list(map(int, input().split()))
inc_array = increase(a)
dec_array = decrease(a[::-1])
array = add_array(inc_array, dec_array)
ans = 0
for i in array:
    if i > ans:
        ans = i
print(ans-1)
print(inc_array, dec_array, array)
'''

"""
# 1. dp
'''
최장 증거 수열
현재 위치의 원소를 가장 마지막 원소로 하는 배열의 길이를 테이블에 담거나, 기존의 가장 큰 값과 비교해서 더 큰 값을 담는다
예를 들어 1231이 수열이라면
테이블에 1231로 담아도 되고
1233으로 담아도 된다

그래서 그 과정을 적어보자면
원소를 하나 이동할 때 마다 처음부터 다 비교해오면서 현재의 원소보다 작은 수의 최장 수열을 체크하면 될거 같은데

'''

def f(n, arr):
    dp = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]: # 현재 원소가 처음부터 비교해오는 원소보다 크면
                if dp[i] < dp[j]+1:
                    dp[i] = dp[j]+1
    return dp

n = int(input())
a = list(map(int, input().split()))
dp = f(n, a)
dp1 = f(n, a[::-1])[::-1]
ans = [dp[i]+dp1[i]-1 for i in range(n)]
print(dp, dp1)
print(max(ans))
"""

# 2. binary search
'''
위와 비슷한 방법이지만 정렬된 수를 담는 테이블을 사용해서
이진 탐색으로 현재의 원소가 들어갈 자리를 찾으면서 시간복잡도를 줄이는 방법

start = mid+1을 했다면 end를 반환하고, end = mid-1을 했다면 start를 반환해라
그리고 무조건 먼저 조건문에 작성한 쪽을 mid가감 조작을 한다
'''

def bs(subs, cur_num):
    start = 0
    end = len(subs)
    while start < end:
        mid = (start + end)//2
        if cur_num > subs[mid]:
            start = mid+1
        else:
            end = mid
    return end

def lis(arr):
    dp = [1 for _ in range(n)]
    subs = [arr[0]]
    for i in range(1, n):
        if arr[i] > subs[-1]:
            subs.append(arr[i])
        else:
            bs_idx = bs(subs, arr[i])
            subs[bs_idx] = arr[i]
        dp[i] = len(subs)
    return dp

n = int(input())
a = list(map(int, input().split()))
asc = lis(a)
des = lis(a[::-1])[::-1]
ans = [asc[i]+des[i]-1 for i in range(n)]
print(max(ans))