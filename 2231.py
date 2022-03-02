def find_generator(n):
    count = 0
    for i in range(int(n)):
        check = i
        for j in str(i):
            check += int(j)
        if check == int(n):
            print(i)
            count += 1
            break
    if count == 0:
        print('0')
N = input()
find_generator(N)