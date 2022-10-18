# 색종이
# 각 색종이가 보이는 부분의 면적을 구하는 프로그램을 작성하라
# 가로 최대 1001 칸 세로 최대 1001 칸
# ex) 1 4 3 2 이면 (1,4) 가장 왼쪽 아래  너비 3 높이 2
# 경계 밖으로 나가는 경우는 없음
N = int(input())
arr =[[0]*1002 for _ in range(1002)]
x_lst =[]
y_lst =[]
for k in range(1,N+1):
    x,y,w,h=map(int,input().split())
    for i in range(y,y+h):
        for j in range(x,x+w):
            arr[i][j] = k
    x_lst.append(x)
    x_lst.append(x+w)
    y_lst.append(y)
    y_lst.append(y+h)


min_x = min(x_lst)
max_x = max(x_lst)
min_y = min(y_lst)
max_y = max(y_lst)
for k in range(1,N+1):
    cnt = 0
    for i in range(min_y,max_y+1):
        for j in range(min_x,max_x):
            if arr[i][j] == k:
                cnt += 1
    print(cnt)

#### 42점 맞는데 고쳐 볼것,,,
