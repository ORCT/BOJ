import sys

n=int(input())
people = {}
for i in range(n):
    value = list(map(int, sys.stdin.readline().split()))
    people[i] = value
for i in range(n):
    cnt = 0
    for j in range(i+1, n):
        if people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            cnt += 1        
    people[i].append(cnt)
value_sequence = []
for i in range(n):
    value_sequence.append(people[i][2])
sorted_value_sequence = sorted(value_sequence)[::-1]
people_sequence = []
for i in range(n):
    people_sequence.append(sorted_value_sequence.index(i)+1)
print(people)
print(value_sequence)
print(sorted_value_sequence)
print(people_sequence)



