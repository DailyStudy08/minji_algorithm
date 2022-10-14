arr = [list(map(int,input().split())) for _ in range(5)]
bingo = 0
cnt = 0
for k in range(5):
    check_lst = list(map(int,input().split()))
    if bingo != 3:
        for check in check_lst:
            for i in range(5):
                for j in range(5):
                    if arr[i][j] == check:
                        arr[i][j] = 0
                        cnt += 1
            if k >= 2:
                cross_cnt = 0
                reverse_cnt = 0
                for i in range(5):
                    row_cnt = 0
                    col_cnt = 0
                    for j in range(5):
                        if arr[i][j] == 0:
                            row_cnt += 1
                        if arr[j][i] == 0:
                            col_cnt += 1
                        if arr[i][i] == 0:
                            cross_cnt += 1
                        if arr[i][4-i] == 0:
                            reverse_cnt += 1
                    if row_cnt == 5 or col_cnt == 5 or cross_cnt == 5 or reverse_cnt == 5:
                        bingo += 1
    else:
        result = cnt
        print(result)
