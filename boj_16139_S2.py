import sys

def make_dict(S, al):
    al_dict = {}
    for i in al:
        count = 0
        count_list = []
        for j in S:
            if i == j:
                count += 1
            count_list.append(count)    
        al_dict[i]=count_list
    return al_dict

def count_num_of_alphabet(al_dict, quest_key, quest_left, quest_right):
    low = int(quest_left)
    high = int(quest_right)+1
    answer = al_dict[quest_key][high] - al_dict[quest_key][low]
    return answer

al = 'abcdefghijklmnopqrstuvwxyz'
S=' ' + sys.stdin.readline().rstrip()
q=int(sys.stdin.readline())
al_dict = make_dict(S,al)
#print(al_dict)
for i in range(q):
    quest_key, quest_left, quest_right = sys.stdin.readline().split()
    answer = count_num_of_alphabet(al_dict, quest_key, quest_left, quest_right)
    print(answer)