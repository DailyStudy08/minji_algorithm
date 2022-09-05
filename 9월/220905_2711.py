# 오타맨 고창영
T = int(input())
for tc in range(1,T+1):
    num, st = input().split()
    print(st[0:int(num)-1]+st[int(num):])
    
