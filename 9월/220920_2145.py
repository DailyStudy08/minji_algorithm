# 숫자 놀이 
# 과제때문에 쉬운거 풉니다..
# 각자리수를 한자리수가 될때까지 반복
N  = input()
if N == '0':
    pass
else:
    while len(N) != 1 :
        num = 0
        for i in N:
            num += int(i)
        N = str(num)
    print(N)
### 잠와서 안보여유 