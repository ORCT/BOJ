import sys
ssr = sys.stdin.readline

def dec_to_bin(n):
    if n//2 == 0:
        print(n%2,end='')
        return
    dec_to_bin(n//2)
    print(n%2,end='')
    
n = int(ssr())
dec_to_bin(n)