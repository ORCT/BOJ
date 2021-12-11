import sys
ssr = sys.stdin.readline

n = int(ssr())
word = set()
for i in range(n):
    word.add(ssr().rstrip())
word = list(word)
word.sort(key = lambda x : (len(x),x))
print('\n'.join(word))