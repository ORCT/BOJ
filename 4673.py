#The main logic is int(n)+n[i]... = m and m is not the self number
#You have to find self number
def sum_digits(n:int):
    sum_of_digits=0
    for i in range(len(str(n))):
        digit=str(n)[i]
        sum_of_digits += int(digit)
    return sum_of_digits

def make_num_sequence(n:int):
    d = n+sum_digits(n)
    return d

num_list = []
for i in range(1, 10001):
    num_list.append(i)
for i in range(1, 10001):
    remove_num = make_num_sequence(i)
    try:
        num_list.remove(remove_num)
    except ValueError:
        pass
for i in range(len(num_list)):
    print(num_list[i])
