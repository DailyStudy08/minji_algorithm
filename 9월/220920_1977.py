# 완전제곱수
# M 이상 N 이하의 자연수 중 완전 제곱수인 것을 모두 골라 합을 구하고 
# 그 중 최솟값을 찾는 프로그램을 작성
M = int(input())
N = int(input())
lst = []
num = int(N**(1/2))
for i in range(num+1):
    if i**2 >= M : 
        lst.append(i**2)
if lst :
    sum = sum(lst)
    min_num = min(lst)
    print(sum)
    print(min_num)
else:
    print(-1)