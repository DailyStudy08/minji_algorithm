# 듣보잡
# N: 듣도 못한 사람
# M :보도 못한 사람
N,M = map(int,input().split())
not_hear =set()
for h in range(N):
    not_hear.add(input())
not_see = set()
for s in range(N):
    not_see.add(input())

no_see_hear = sorted(list(not_hear&not_see))
print(len(no_see_hear))
for i in no_see_hear:
    print(i)