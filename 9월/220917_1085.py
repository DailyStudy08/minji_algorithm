# 직사각형에서 탈출
# (x, y) : 현수가 있는 곳
# (w , h) : 오른 쪽 위 꼭짓점
x,y,w,h = map(int,input().split())
# 직사각형의 경계선까지 가는 거리의 최솟값을 구하라
row_x = x
row_w = w-x
col_y = y
col_h = h - y
lst =[row_x,row_w,col_y,col_h]
print(min(lst))