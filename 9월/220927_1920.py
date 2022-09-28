def search(num):
    L = 0
    R = N - 1
    mid = (L+R) // 2
    while A[L] <= num <= A[R] :
        if num < A[mid]: # 찾는 수 보다 mid 값이 더 큰 경우
            R = mid - 1
            mid = (L + R)//2
        elif num > A[mid]: # mid 값이 더 작은 경우
            L = mid + 1
            mid = (L + R)//2
        else:
            return 1
    return 0
# 수 찾기 
N = int(input())
A = list(map(int,input().split()))
A.sort()
M = int(input())
B = list(map(int,input().split()))
for num in B:
    print(search(num))



# for i in B:
#     if i in A:
#         print(1)
#     else:
#         print(0)
