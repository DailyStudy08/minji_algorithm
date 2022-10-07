# 방배정
# 1~ 6학년 까지 배정
# 성별끼리 , 같은 학년끼리 방 배정
# 한방에 배정할 수 있는 최대 인원 수 K
# 모든 학생을 배정하기 위해 필요한 최소 방의 개수
# 입력 : 첫째 줄 N:학생 수 , K:최대 인원 수
# 다음 N개의 줄 성별 (여자는 0 남자는 1 ) 과 학년

N , K = map(int,input().split())
Woman = [0] * 7
man = [0] * 7
for _ in range(N):
    s , c = map(int,input().split())
    if s == 1:  # 남학생인 경우
        man[c] += 1
    else:       # 여학생인 경우
        Woman[c] += 1

# print(Woman)
# print(man)
room = 0
for i in range(1,7):
    if Woman[i] % K == 0 :
        room += Woman[i] // K
    else:
        room += (Woman[i] // K) + 1

    if man[i] % K == 0 :
        room += man[i] // K
    else:
        room += (man[i] // K) + 1

print(room)