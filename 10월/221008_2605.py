# 줄 세우기
# 줄을 선 순서를 출력하는 프로그램 작성
# 시작 1번은 0을 뽑고 그 뒤론 0 1 , 0 1 2, 0 1 2 3 ... 순으로 뽑기를 하게 됨
N = int(input())
arr = list(map(int,input().split()))
lst =[]
stack =[]
for i in range(N):
    if arr[i] == 0:
        lst.append(str(i+1))
    else:
        for _ in range(arr[i]):
            stack.append(lst.pop())
        lst.append(str(i+1))
        while stack:
            lst.append(stack.pop())
result = " ".join(lst)
print(result)

