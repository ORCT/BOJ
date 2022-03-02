#Input : case number, numerator, denominator
#Output : number n that related in inappropriate range inputted fraction
#What I have to do?: make lists of range elements, and sort
def make_elements_of_range(n):
    n = 10
    elements=[0,1]
    for i in range(n):
        element=0 + 1/(i)


case_num=int(input())
for i in range(case_num):
    a,b=map(int, input().split())
    fraction=a/b