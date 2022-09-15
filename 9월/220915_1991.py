# 트리순회 
# 이진 트리를 입력 받아 전위순회, 중위순회 ,후위 순회 한 결과를 출력하는 프로그램 작성
N  = int(input())
tree = {}  # 문자열이라 딕셔너리 생성
for _ in range(N):
    node,left,right = map(str,input().split())
    tree[node] = left ,right 

# 전위 순회
def preorder(node):
    if node != '.':  # 자식이 있다면 
        print(node,end = '') # 루트 노드 출력
        if tree[node][0] != '.':
            preorder(tree[node][0]) # 왼쪽 노드 탐색
        if tree[node][1] != '.':
            preorder(tree[node][1]) # 오른쪽 노드 탐색
# 중위 순회
def inorder(node):
    if node != '.':  # 자식이 있다면 
        if tree[node][0] != '.':
            preorder(tree[node][0]) # 왼쪽 노드 탐색
        print(node,end = '')  # 루트 노드 출력
        if tree[node][1] != '.':
            preorder(tree[node][1]) # 오른쪽 노드 탐색
# 후위 순회
def postorder(node):
    if node != '.':  # 자식이 있다면 
        if tree[node][0] != '.':
            preorder(tree[node][0]) # 왼쪽 노드 탐색
        if tree[node][1] != '.':
            preorder(tree[node][1]) # 오른쪽 노드 탐색
        print(node,end = '') # 루트 노드 출력


preorder('A')
print()
inorder('A')
print()
postorder('A')


### 중위 순회랑  후위 순회가 이상하게 나와서 다시 해보겠습니다 ㅠ