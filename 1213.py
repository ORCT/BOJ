'''
팰린드롬(회문) : 앞에서 부터 읽는 것과 뒤에서부터 읽는 것이 동일한 말, 구절, 단어 등등

길이가 짝수면 구성 알파벳이 전부 짝수여야하고
길이가 홀수면 구성 알파벳 중 하나만 홀수고 전부 짝수여야함
이게 안되면 sorry 출력하는거로 하고 
가능하면 사전순으로 빠른 말을 출력해야함
딕셔너리에 키별 순서가 있나?
아니면 처음 받는 문자열을 정렬을 해서 확인해야하나

홀수인 친구 기억해뒀다가 기억하면서 당연히 1개 빼고
빠른거부터 출력하는거 반 + 홀수 + 느린거부터 출력하는거 반
'''
from collections import defaultdict

s = input()
odd = 0
alphabets = defaultdict(int)
ans, mid = '', ''
for i in s:
    alphabets[i] += 1
    
if len(s) % 2 == 0:
    for alphabet, cnt in sorted(alphabets.items()):
        ans += alphabet*(cnt//2)
        if cnt % 2 == 1:
            odd += 1
            break
    if odd > 0:
        print("I'm Sorry Hansoo")
    else:
        print(ans+mid+ans[::-1])
else:
    for alphabet, cnt in sorted(alphabets.items()):
        ans += alphabet*(cnt//2)
        if cnt % 2 == 1:
            odd += 1
            mid = alphabet
            if odd == 2:
                break
    if odd > 1:
        print("I'm Sorry Hansoo")
    else:
        print(ans+mid+ans[::-1])
        

# for alphabet, cnt in sorted(alphabets.items()):
#     ans += alphabet * (cnt//2)
#     if cnt % 2 == 1:
#         if mid != '':
#             print("I'm Sorry Hansoo")
#             break
#         else:
#             mid = alphabet
# print(ans + mid + ans[::-1])