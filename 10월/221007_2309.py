# 일곱 난쟁이
# 일곱난쟁이의 키의 합이 100이 됨
# 9명의 난쟁이 중 진짜 난쟁이 7명을 찾기
# 아홉 난쟁이의 키는 모드 다르다
# 오름차순으로 출력하기
# 부분 집합 만들기?
def powerset(idx,cnt,status):
    # 집합을 다 만든 경우
    if cnt == K:
        lst.append(status[::])
        return
    # 다 돌았지만 집합을 못만든 경우
    if idx == M:
        return
    # 선택한 경우
    status[idx] = 1
    powerset(idx+1,cnt+1,status)
    status[idx] = 0
    # 선택하지 않은 경우
    powerset(idx + 1,cnt,status)

cm = []
for _ in range(9):
    cm.append(int(input()))
sorted(cm)
M = 9
K = 7
status = [0] * 9
lst = []
powerset(0,0,status)
# print(lst)
for i in range(len(lst)):
    sum_cm = []
    for j in range(9):
        if lst[i][j] == 1:
            sum_cm.append(cm[j])
    # print(sum_cm)
    if sum(sum_cm) == 100:
        sum_cm.sort()
        for num in sum_cm:
            print(num)
        break
# 처음에 틀렸던 이유 : 문제 출력 조건이 아무거나 나오게 하라 하길래
# break를 넣지 않았는데 합이 100이 되는 조합을 발견하면
# 그 조합을 출력하고 반복문을 종료하여야 답으로 인정되는 문제였습니다..


# 9명 중에서 7명을 가지는 부분 집합을 만든다
# 그 집합의 합이 100이 되면 그 부분 집합 return

