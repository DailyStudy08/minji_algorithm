# 나는야 포켓몬 마스터 이다솜
N , M = map(int,input().split()) 
poketmon_strbook = []
poketmon_numbook = {}
for i in range(1,N+1):
    pk = input()
    poketmon_numbook[pk] = i
    poketmon_strbook.append(pk)
for _ in range(M):
    poketmon = input()
    if poketmon.isdigit():
       print(poketmon_strbook[(int(poketmon)-1)])
    else:
        print(poketmon_numbook[poketmon])