import sys
ssr = sys.stdin.readline

n,m = map(int, ssr().split())
wood = list(map(int, ssr().split()))
low = 0
high = max(wood)
while low<=high:
    sum = 0
    mid = (low + high)//2
    for i in wood:
        if i >= mid:
            sum += i - mid
    if m > sum:
        high = mid-1
    else:
        low = mid+1
print(high)