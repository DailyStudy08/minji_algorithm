import heapq
# A -> B
# 그리디 알고리즘으로 분류 되어있어서 도전 -!
# 가능한 연산 * 2 or 가장 오른쪽에 1을 추가 할 수 있음
A , B = map(int,input().split())
# 연산 해주는 함수를 만들자 ! 
# 1. 2로 만들어주는 함수
def make_2(A,cnt):
    return cnt+1 , A* 2

# 2. 1을 수에 가장 오른쪽에 추가해주는 함수 
def add_1(A,cnt):
    return cnt+1, int(str(A)+'1')

def solve(a,b):
    q = [(0,A)]
    while q:
        cnt, a =heapq.heappop(q)
        if a<b:
            heapq.heappush(q,make_2(a,cnt))
            heapq.heappush(q,add_1(a,cnt))
        elif a==b:
            return cnt+1
        else:
            continue
    return -1
print(solve(A,B))