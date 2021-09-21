import sys

def find_number_of_circle_intersection_point(x1,y1,r1,x2,y2,r2):
    center_to_center_distatnce = ((x2-x1)**2+(y2-y1)**2)**(1/2)
    r_list = [r1,r2]
    r_list = sorted(r_list)
    r_list.append(center_to_center_distatnce)
    if center_to_center_distatnce==0 and r_list[0]==r_list[1]:
        return -1
    elif sorted(r_list)[2]==sorted(r_list)[0]+sorted(r_list)[1]:
        return 1
    elif sorted(r_list)[2]>sorted(r_list)[0]+sorted(r_list)[1]:
        return 0
    else:
        return 2

T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())
    print(find_number_of_circle_intersection_point(x1,y1,r1,x2,y2,r2))