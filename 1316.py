import sys
n = int(input())
S_element = []
group = 0
for i in range(n):
    S=sys.stdin.readline()
    S_element = list(set(S))
    check = 0 
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            check_S = S[i+1:]
            if check_S.count(S[i])>0:
                check += 1
    if check == 0:
        group +=1
print(group)