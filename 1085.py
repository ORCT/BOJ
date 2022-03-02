x,y,w,h = map(int, input().split())
a = w-x
b = h-y
list = [x,y,a,b]
print(sorted(list)[0])