# 가장 큰 금민수
# 금민수는  4 와 7로만 이루어진 수 
# N : 주어지는 수
# N 보다 작거나 같은 금민수 중 가장 큰 것을 출력
N = input()
result = 0
# 일단 N을 문자열로 받아서 0번째 자리부터 비교해서 
# 0번째 자리가 4보다 작은경우,4이거나 7보다 작은경우, 7이거나 7보다 큰 경우 만들기 
# 4보다 작은 경우에는 한칸 작게 7 출력?
for i in range(len(N)):
        if i == 0 and int(N[i]) < 4 :
            result += 7*10**(len(N)-i-2)
        elif i > 1 and i != len(N)-1 and int(N[i]) < 4 :
            result += 7*10**(len(N)-i-2)
        elif i > 1 and 4 <= int(N[i]) < 7:
            result += 4*10**(len(N)-i-1)
        elif i > 1 and 7 <= int(N[i]):
            result += 7*10**(len(N)-i-1) 

        if i == 0 and int(N[i]) > 4:
            if 4 <= int(N[i]) < 7:
                result += 4*10**(len(N)-i-1)
            elif  7 <= int(N[i]):
                result += 7*10**(len(N)-i-1)
            if i+1 == 1 and int(N[i+1]) > 4:
print(result)

###############################
# 반례 하나를 못찾겠습니다 ㅠ
