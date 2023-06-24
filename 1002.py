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
    elif sorted(r_list)[2]<sorted(r_list)[0]+sorted(r_list)[1]:
        return 2

T = int(input())
for i in range(T):
    x1,y1,r1,x2,y2,r2 = map(int, sys.stdin.readline().split())
    print(find_number_of_circle_intersection_point(x1,y1,r1,x2,y2,r2))
    #test
    
'''
적 위치까지의 거리 r1, r2가 있고 관측자 2명의 각각 평면 좌표가 주어진다.
이 때 조건에 맞는 적의 위치는 총 몇개일 것인가
1명의 관측자의 좌표에서 적이 있을 수 있는 위치를 전부 체크하면 원의 형태가 나온다.
다른 한 명의 관측자에도 같은 원리를 적용하면 적의 예상위치가 두 개의 원으로 표시된다.
거기서 양 관측자의 조건을 다 만족한다는 뜻은 해당 원의 접점을 의미한다.
즉 두 개의 원의 방정식을 만족하는 해를 구하는게 이 문제의 목표이다.
가능한 경우는 외접하는 경우 2개의 교점, 1개의 교점, 0개의 교점
내접하는 경우 1개의 교점, 0개의 교점
두 방정식이 같을 때 무한대의 교점
총 6가지의 경우가 있을 수 있겠다.

첫번째 풀이는 왜 틀렸을까
함수부터 보자면
각 원의 중심까지의 거리를 구한다.
각 원의 반지름을 리스트로 만들고 정렬한다.
중심간거리도 리스트에 추가한다.
조건문을 통해 결과를 반환한다.
중심거리=0 & 반지름이 같을 경우 -1 반환(무한대)
아마 각 선을 기준으로 삼각형이 이뤄지는지를 조건에 따라 체크한 것으로 보인다
가장 긴 선이 다른 두 선의 합과 같으면 교점이 1개
더 크다면 교점이 0개
그 외의 경우는 2개
라고 체크한 것 같은데 아마 에러가 난다면
그 외의 경우는에 2개가 아닌 경우가 포함될 가능성이 있다는 것이다.
즉 작다면 2개로 고친다면 맞을 가능성이 있다.
틀렸다.

현재 여러 이의제기로 재채점 중이기 때문에 지금 틀린거로 신경 쓰지 말고 재채점 알림이 뜨면 그 때 다시 보는 걸로 하자

'''