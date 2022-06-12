# import sys
# input = sys.stdin.readline

# n = int(input())
# h = []
# for _ in range(n):
#     order = int(input())
#     if order > 0:
#         h.append(order)
#     else:
#         if len(h)==0:
#             print(0)
#         else:
#             a = min(h)
#             print(a)
#             h.remove(a)
import heapq
import sys
input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    order = int(input())
    if order > 0:
        heapq.heappush(h,order)
    else:
        if len(h)==0:
            print(0)
        else:
            print(heapq.heappop(h))