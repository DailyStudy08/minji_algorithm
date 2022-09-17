# 미로 탈출
# N*M 크기의 배열로 표현되는 미로가 있다.
# 1은 이동 할 수 있는 칸
# 0은 이동 할 수 없는 칸
# (1,1) 에서 출발하여 (N,M) 위치로 이동하는 미로 
##### 0917에 못풀어서 0918에 재도전 하겠습니당 ㅠ ####
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
puzzle=[]
for _ in range(N):
    puzzle.append(list(map(int,input().rstrip()))) # readline이 맨 뒤에 \n 까지 입력 받아서 rstrip을 제거해줌

dr = [-1,1,0,0] # 상 하 좌 우
dc = [0,0,-1,1]
cnt = 1
visit=[[0]*M for _ in range(N)]
a, b = 0, 0
min_cnt = sys.maxsize
visit[a][b] = 1
while True:
    for k in range(4): # 탐색 구문
        nr = a+dr[k]
        nc = b+dc[k]
        if nr < 0 or nc <0 or nr >= N or nc >= N or puzzle[nr][nc] == 0:
            pass
        elif puzzle[nr][nc] == 1:
            cnt += 1
            visit[nr][nc] = cnt
            a , b = nr, nc
            continue
    else:
        if cnt <= min_cnt:
            min_cnt = cnt

