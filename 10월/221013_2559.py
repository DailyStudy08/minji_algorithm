# 수열
# 매일 측정한 온도가 정수의 수열로 주어졌을때, 연속적인 며칠 동안의
# 온도의 합이 가장 큰 값을 계산하는 프로그램을 작성하시오
L,N = map(int,input().split())
arr = list(map(int,input().split()))
max_num = -101
for i in range(L-N+1):
    num = 0
    for j in range(i,i+N):
        num += arr[j]
    if max_num < num:
        max_num = num
print(max_num)
# 시간 초과
# 시간 복잡도가 N^2 되기 때문에 이중 반복문을 피하는게 중요하다!
#