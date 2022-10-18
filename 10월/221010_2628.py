# 가로 세로 리스트 만들어서
# 세로인 경우에는 가로 리스트에 자르는 구간 값 넣고
# 가로인 경우 세로 리스트에 구간 값넣음
# 오름차순으로 정렬해서
# 구간 간격 값 구해서 새로운 리스트에 배열
# 그 중 가장 큰 값 뽑아서 곱하면 넓이 나옴
N , M = map(int,input().split()) # 가로 세로
t = int(input())
row = [0,N]
col = [0,M]
for tc in range(t):
    path, num = map(int,input().split())
    if path == 1: # 세로인 경우
        row.append(num)
    else:
        col.append(num)
row.sort()
col.sort()
# print(row)
# print(col)
row_lst =[]
col_lst =[]
for i in range(len(row)-1):
    row_lst.append(row[i+1]-row[i])
for j in range(len(col)-1):
    col_lst.append(col[j+1]-col[j])
row_lst.sort()
col_lst.sort()
# print(row_lst)
# print(col_lst)
print(max(row_lst)*max(col_lst))

