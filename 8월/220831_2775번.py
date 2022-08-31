# 부녀회장이 될테야
# a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지
# 사람들의 수의 합만큼 사람들을 데려와 살아야한다.
# K: 층 , N : 호수
# 이차원 배열 리스트를 만들어야하나?
T = int(input())

for tc in range(1,T+1):
    k = int(input())
    n = int(input())
    k0 = [x for x in range(1,n+1)]
    for k in range(k):
        for i in range(1,n):
            k0[i] += k0[i-1]
    print(k0[-1])



    