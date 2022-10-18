# 1 = 스위치 켜짐 0 = 스위치 꺼짐
#  학생들은 성별과 받은 수에 따라 스위 치 조작
# 남학생은 스위치 번호가 자기가 받은 수의 배수이면 스위치 상태 변경
# 여학생은 받은 번호를 중심으로 좌우가 대칭이면서 가장많은 스위치 포함하는 구간
# 찾아서 상태 모두 바꿈
# 구간에 속한 스위치 개수는 항상 홀수
N = int(input()) # 스위치 갯수
arr = list(map(int,input().split())) # 스위치 상태
num = int(input()) # 학생 수
for _ in range(num):
    s, switch = map(int,input().split())
    if s == 1:  # 남학생인 경우
        switch
    else:       # 여학생인 경우
#  얘도 다시 생각하기
