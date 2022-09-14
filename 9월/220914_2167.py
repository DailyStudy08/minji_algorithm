# 2차원 배열이 주어졌을 때 (i,j)위치부터 (x,y) 위치까지에 저장되어 있는 수들의 합을 
# 구하는 프로그램을 작성하시오
# 배열의 (i,j) 위치는 i행 j 열을 나타낸다.
N, M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]

K = int(input())
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] = arr[i-1][j-1] +  dp[i-1][j] - dp[i-1][j-1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])