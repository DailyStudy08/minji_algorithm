
N = int(input())
room = [list(map(str,input().rstrip())) for _ in range(N)]
row_cnt = 0
col_cnt = 0
for i in range(N):
    for j in range(N-1):
        if room[i][j] == '.' and room[i][j+1] == '.':
            row_cnt += 1
            break
for i in range(N):
    for j in range(N-1):
        if room[j][i] == '.' and room[j+1][i] == '.':
            col_cnt += 1
            break
print(row_cnt,col_cnt)
# 반례를 모르겠어요 ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ


'''
6
.....X
..X..X
.X.X.X
......
......
XXXXXX
일 때, 
output: 4 6
answer: 5 8
인 것 같아서 적어보았어요!
'''
