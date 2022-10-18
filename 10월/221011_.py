# 개미
# 이차원 배열 만드는데
# 개미의 시작 움직임이 r += 1 c += 1
# 최댓값 일때 벽에 부딪히면 그 부딪힌 방향은 -1 됨
# 최소값 일때 벽에 부딪히면 부딪힌 방향은 +1 됨
# 출력값으로 t 시간 후 개미의 위치 좌표 출력
d =[1,-1]
w , h =map(int,input().split())
p ,q = map(int,input().split())
t = 8
cnt = 0
path1 = 0
path2 = 0
# cnt 만들어서 while 문을 돌려서 개미의 위치 좌표를 구하자!
while cnt != t:
    if p == w or p == 0:
        path1 = (path1 + 1) % 2
    if q == h or q == 0:
        path2 = (path2 + 1) % 2
    p += d[path1]
    q += d[path2]
    cnt += 1
print(f'{p} {q}')