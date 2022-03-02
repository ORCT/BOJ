S = input()
S_num=0
for i in range(len(S)):
    if S[i]=='A' or S[i]=='B' or S[i]=='C':
        S_num+=3
    elif S[i]=='D' or S[i]=='E' or S[i]=='F':
        S_num+=4
    elif S[i]=='G' or S[i]=='H' or S[i]=='I':
        S_num+=5
    elif S[i]=='J' or S[i]=='K' or S[i]=='L':
        S_num+=6
    elif S[i]=='M' or S[i]=='N' or S[i]=='O':
        S_num+=7
    elif S[i]=='P' or S[i]=='Q' or S[i]=='R' or S[i]=='S':
        S_num+=8
    elif S[i]=='T' or S[i]=='U' or S[i]=='V':
        S_num+=9
    elif S[i]=='W' or S[i]=='X' or S[i]=='Y' or S[i]=='Z':
        S_num+=10
    elif S[i]=='*' or S[i]=='#':
        S_num+=11
print(S_num)