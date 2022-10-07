# 직사각형 네개의 합집합의 면적 구하기
# 평면에 4개의 직사각형 모두 가로축에 평행
# 떨어져 있거나 겹쳐있거나 포함하거나 할 수 있음!
# 직사각형들이 차지 하는 면적 구하기

# 모든 x 좌표와 y좌표는 1이상 100이하 정수!

# 100*100 이차원 배열 만들어 주기
arr = [[0]*101 for _ in range(101)]
x_lst = []
y_lst = []
for tc in range(4):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(y1,y2):
        for j in range(x1,x2):
            arr[i][j] = 1
    x_lst.append(x1)
    x_lst.append(x2)
    y_lst.append(y1)
    y_lst.append(y2)
#
# print(x_lst)
# print(y_lst)
    # print(f'#{tc}')
    # for num in arr:
    #     print(num)
cnt = 0
min_x = min(x_lst)
max_x = max(x_lst)
min_y = min(y_lst)
max_y = max(y_lst)
for i in range(min_y,max_y+1):
    for j in range(min_x,max_x+1):
        if arr[i][j] == 1:
            cnt += 1
print(cnt)

# 22분 걸림
# 처음에는 1이상 100 이하라고 해서 이라고 101*101 이차원 배열을
# 만들어서 전체 탐색을 할려고 했으나 런타임 에러가 뜨는 바람에
# 입력으로 들어오는 x값과 y값을 각 리스트에 저장해서 최대 최솟값을 사용하여
# 2차원 배열을 탐색하고 나니 런타임 에러가 뜨지 않았습니다.