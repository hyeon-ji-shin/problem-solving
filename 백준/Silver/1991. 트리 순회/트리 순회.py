# 전위 순회 : 루트 노드 / 왼쪽 자식 노드 / 오른쪽 자식 노드
def preorder(node, tree):
    if node != '.':
        print(node, end="")
        preorder(tree[node][0], tree)
        preorder(tree[node][1], tree)

# 중위 순회 : 왼쪽 자식 노드 / 루트 노드 / 오른쪽 자식 노드
def inorder(node, tree):
    if node != '.':
        inorder(tree[node][0], tree)
        print(node, end="")
        inorder(tree[node][1], tree)
    
# 후위 순회 : 왼쪽 자식 노드 / 오른쪽 자식 노드 / 루트 노드
def postorder(node, tree):
    if node != '.':
        postorder(tree[node][0], tree)
        postorder(tree[node][1], tree)
        print(node, end="")
        
N = int(input())
tree = {}

for _ in range(N):
    root, left, right = input().split()
    tree[root] = [left, right]

preorder('A', tree)
print()
inorder('A', tree)
print()
postorder('A', tree)