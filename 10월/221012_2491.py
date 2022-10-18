# 또 수열,,
# 연속해서 커지거나 작아지는 수열 중 가장 길이가 긴 것을 찾아서 길이 출력
# 일단 첫번째 값고 두번째 값 비교해서
# 점점 커지는 수열인지 작아지는 수열인지 파악하고
# cnt 하는데 수열 흐름이 끊기면
# 그 카운트 값은 저장하고
# cnt 끝난지점을 start로 잡고 다시 cnt 해서
# 끝날때 까지한다 그 중 가장 큰 값을 출력!
N = int(input()) # 길이
lst = list(map(int,input().split()))
result = 0
flag = True  # 점점 작아지는 경우
count = 1

for i in range(len(lst)-1):
    if lst[i] == lst[i+1]:
        count += 1
    else:
        if lst[i] > lst[i+1]: # 점점 작아지는 경우
            
        else: # 점점 커지는 경우






# dp1, dp2 = [1]*N ,[1]*N
# for i in range(1,N):
#     if lst[i] <= lst[i-1]: # 점점 작아지는 경우
#         dp1[i] = max(dp1[i],dp1[i-1]+1)
#     if lst[i] >= lst[i-1]:  # 점점 커지는 경우
#         dp2[i] = max(dp2[i],dp2[i-1]+1)
# print(max(max(dp1),max(dp2)))
