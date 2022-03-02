import sys
import string
ssr = sys.stdin.readline

char = string.ascii_letters+' '+'.'
while 1:
    sentence = ssr().rstrip()
    if sentence=='.':
        break
    for i in char:
        sentence = sentence.replace(i,'')
    check = sentence
    while 1:
        if sentence == '':
            print('yes')
            break
        sentence = sentence.replace('()','')
        sentence = sentence.replace('[]','')
        if sentence == check:
            print('no')
            break
        else:
            check = sentence