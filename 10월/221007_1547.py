M = int(input())
ball_num = 1
for _ in range(M):
    X ,Y = map(int,input().split())
    if X == ball_num:
        ball_num = Y
    elif Y == ball_num:
        ball_num = X
    else:
        pass
print(ball_num)