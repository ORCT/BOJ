s = input()
S = s.upper()
check_list=[]
alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(len(alphabet)):
    num_of_alphabet=S.count(alphabet[i])
    check_list.append(num_of_alphabet)
#for i in range(len(S)):
#    num_of_alphabet=S.count(S[i])
#    check_list.append(num_of_alphabet)
check_num=max(check_list)
S_check = []
for i in range(len(check_list)):
    if check_num==check_list[i]:
        S_check.append(alphabet[i])
if S_check.count(S_check[0])==len(S_check):
    print(S_check[0])
else:
    print('?')
#print(check_num)
#print(check_list)
#print(S_check)
#print(S.count('I'))