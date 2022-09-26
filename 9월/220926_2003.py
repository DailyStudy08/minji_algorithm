# pypy3으로 냈어용
N , M =map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
result = 0
start = 0
end = len(A)
while start != end:
    for i in range(start,end):
        cnt += A[i]
        if cnt < M:
            if i == end-1:
                cnt = 0
                start += 1
                break
            else:
                pass
        elif  cnt == M:
            cnt = 0
            result += 1
            start += 1
            break
        elif cnt > M:
            cnt = 0
            start += 1
            break
print(result)         
