# 1010번 다리놓기
# N : 서쪽 사이트의 갯수
# M : 동쪽 사이트의 갯수
# 서쪽 사이트 (N) 만큼 다리를 지으려고 함 
# 다리끼리 서로 겹쳐 질 수 없을 때, 다리를 지을 수 있는 경우의 수?
def factorial(N):
    num = 1
    for i in range(N):
        num = num *(i+1)
    return num

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    result =factorial(M)//(factorial(N)*factorial(M-N))
    print(result)
#################################
# 내일은 dp로도 풀어보겠습니다.. 풀려고 시도했는데 이해를 못해서 
# 더 공부해야할꺼 같아용,,,
