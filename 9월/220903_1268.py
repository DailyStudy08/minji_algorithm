# 임시반장 정하기 
N = int(input())
student= [list(map(int,input().split()))for _ in range(N)]
leaders = {}
for i in range(N): # 학생 수 
    cnt = 0
    same = [[0]*5 for _ in range(N)]  # 같은 경우를 표시하기 위한 이차원 배열 생성 
    for j in range(5): # 학년 수 
        for k in range(N): 
            if student[i][j] == student[k][j]:   # 같은반을 했을 경우
                same[k][j] = 1  # 1로 표시 해줌
    for s in range(N):           # same 배열을 탐색하기위한 반복문 생성
        for l in range(5):
            if same[s][l] == 1:   # 같은 반을 했을 경우에 
                cnt += 1          # cnt를 1 올려주고 
                break             # 한사람이랑 여러번 같은반을 했어도 중복할 수 없기때문에 반복문 탈출 
    leaders[i] = cnt -1   # 본인값 제외하고 겹치는 값 카운트 
leader = max(leaders,key = leaders.get)+1  # key값이 0부터 시작해서 + 1 해야함, 동일한 value값이 있는 경우에는 작은 숫자의 key값을 출력함
print(leader)
            
        
