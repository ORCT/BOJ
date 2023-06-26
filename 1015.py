n = int(input())
tmp = list(map(int, input().split()))
a = [(tmp[i], i) for i in range(n)]
a_s = sorted(a, key=lambda x:x[0])
# for i in range(n):
#     for j in range(n):
#         if a[i][1] == a_s[j][1]:
#             print(j, end=' ')
#             break
for i in a:
    print(a_s.index(i), end=' ')
'''
3 : n
2 3 1 : a
0 1 2 : p
라고 생각하는 것이 맞다
수열 p를 길이가 n인 배열 a에 적용하면 길이가 n인 b가 된다.
적용하는 방법은 b[p[i]] = a[i]
이 때 p를 적용한 결과가 오름차순이 되는 수열을 찾는 프로그램을 작성하라
뭐 결국은 주어진 a를 오름차순으로 정렬한다면 원래 원소들의 인덱스가 어떻게 되어야 맞겠는가 라는게 핵심
n까지 비교하면서 인덱스를 출력하면 될듯
n이 50밖에 안되므로 그냥 sort를 key를 줘서 하면 된다.
1번 기준으로
(2, 0), (3, 1), (1, 2)로 리스트에 담고
첫번째를 기준으로 정렬시키면
(1,2) (2, 0) (3, 1)
그런 다음에 두번째 숫자들이 어디에 가있는지 인덱스를 출력하는거여'''