def move(no : int,x : int,y : int) -> None:
    if no > 1:
        move(no - 1, x, 6 - x - y)
    move_list.append(f'{x} {y}')
    if no > 1 :
        move(no - 1, 6 - x - y, y)
    return move_list

n = int(input())
move_list = []
move_list = move(n,1,3)
print(len(move_list))
for i in move_list:
    print(i)