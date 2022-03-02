N = int(input())
subject_num=list(map(int,input().split()))
subject_num.sort()
new_num_list=[]
for i in range(N):
    num=subject_num[i]/subject_num[N-1]*100
    new_num_list.append(num)
print(sum(new_num_list)/len(new_num_list))