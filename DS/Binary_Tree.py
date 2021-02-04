class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def traverse_preorder(node):
        """pre-order 순회 함수"""
        if node is not None:
            print(node.data)
            traverse_preorder(node.left_child)
            traverse_preorder(node.right_child)

    def traverse_inorder(node):
        """in-order 순회 함수"""
        if node is not None:
            traverse_inorder(node.left_child)
            print(node.data)
            traverse_inorder(node.right_child)

    def traverse_postorder(node):
        """post-order 순회 함수"""
        if node is not None:
            traverse_postorder(node.left_child)
            traverse_postorder(node.right_child)
            print(node.data)
        
# 노드 인스턴스 생성
node_A = Node("A")
node_B = Node("B")
node_C = Node("C")
node_D = Node("D")
node_E = Node("E")
node_F = Node("F")
node_G = Node("G")
node_H = Node("H")
node_I = Node("I")

# 노드 인스턴스들 연결
node_F.left_child = node_B
node_F.right_child = node_G
node_B.left_child = node_A
node_B.right_child = node_D
node_D.left_child = node_C
node_D.right_child = node_E
node_G.right_child = node_I
node_I.left_child = node_H
"""
                F
               / \
              B   G     이런 모양의 트리가 만들어짐
             /\    \
            A  D    I
              /\   /
             C E  H
"""
# 만들어 놓은 트리를 root 노드인 node_F 부터 순회한다
traverse_preorder(node_F)       # F B A D C E G I H
traverse_inorder(node_F)        # A B C D E F G H I
traverse_postorder(node_F)      # A C E D B H I G F
