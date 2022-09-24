# 시험점수
minkook = list(map(int,input().split()))
manse = list(map(int,input().split()))
minkook_sum = sum(minkook)
manse_sum = sum(manse)
if minkook_sum >= manse_sum:
    print(minkook_sum)
else:
    print(manse_sum)