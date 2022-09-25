# 미로 탈출하기
# 문자열 인식해서 문자열에 따라서 이동하기 
# 미로 탐색 함수 생성
def exit(r,c):
    d = dic[puzzle[r][c]]
    nr = r + d[0]
    nc = c + d[1]
    if nr < 0  and nc < 0 and nr >= N and nc >= N :      # 범위 밖으로 벗어나면 
        return 
    else :
        d = dic[puzzle[nr][nc]]




# 모든점을 출발점으로 시작해서 미로 탈출하는 경우의 수 
N, M = map(int,input().split())
puzzle = [list(input()) for _ in range(N)]
# 문자를 key 값 방향값 value
dic = {'U':[-1,0],'R':[0,1],'D':[1,0],'L':[0,-1]}
print(dic['U'][0])
visit = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        exit
