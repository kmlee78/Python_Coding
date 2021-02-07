class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None

def print_inorder(node):
    """in-order 순회 함수. 이진 탐색 트리를 in-order 순회하면 저장된 데이터들을
       정렬된 순서대로 출력할 수 있다"""
    if node is not None:
        print_inorder(node.left_child)
        print(node.data)
        print_inorder(node.right_child)


class BinarySearchTree:
    """이진 탐색 트리 클래스"""
    def __init__(self):
        self.root = None
 

    def insert(self, data):
        """데이터 삽입 메소드"""
        new_node = Node(data) 

        if self.root is None:
            self.root = new_node
            return

        iterator = self.root
        while iterator is not None:
            if data > iterator.data:
                if iterator.right_child is None:
                    iterator.right_child = new_node
                    return
                iterator = iterator.right_child
            else:
                if iterator.left_child is None:
                    iterator.left_child = new_node
                    return
                iterator = iterator.left_child


    def search(self, data):
        """이진 탐색 트리 탐색 메소드. 해당 노드를 리턴"""
        iterator = self.root
        while iterator is not None:
            if data == iterator.data:
                return iterator
            if data > iterator.data:
                iterator = iterator.right_child
            else:
                iterator = iterator.left_child
        return None


    def delete(self, data):
        """이진 탐색 트리 삭제 메소드"""
        node_to_delete = self.search(data)  # 삭제할 노드를 가지고 온다
        parent_node = node_to_delete.parent  # 삭제할 노드의 부모 노드

        # 경우 1: 지우려는 노드가 leaf 노드일 때
        if node_to_delete.left_child is None and node_to_delete.right_child is None:
            if node_delete is self.root:
                self.root = None
            else:  
                if node_to_delete is parent_node.left_child: 
                    parent_node.left_child = None
                else:
                    parent_node.right_child = None

        # 경우 2: 지우려는 노드가 자식이 하나인 노드일 때:
        elif node_to_delete.left_child is None:  # 지우려는 노드가 오른쪽 자식만 있을 때
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
                self.root.parent = None
            # 지우려는 노드가 부모의 왼쪽 자식일 때
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node
            # 지우려는 노드가 부모의 오른쪽 자식일 때
            else:
                parent_node.right_child = node_to_delete.right_child
                node_to_delete.right_child.parent = parent_node

        elif node_to_delete.right_child is None:  # 지우려는 노드가 왼쪽 자식만 있을 때
            if node_to_delete is self.root:
                self.root = node_to_delete.left_child
                self.root.parent = None
            # 지우려는 노드가 부모의 왼쪽 자식일 때
            elif node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node
            # 지우려는 노드가 부모의 오른쪽 자식일 때
            else:
                parent_node.right_child = node_to_delete.left_child
                node_to_delete.left_child.parent = parent_node

        # 경우 3: 지우려는 노드가 2개의 자식이 있을 때
        else:
            successor = self.find_min(node_to_delete.right_child)
            temp = successor.data
            self.delete(successor.data)
            node_to_delete.data = temp


    @staticmethod
    def find_min(node):
        """(부분)이진 탐색 트리의 가장 작은 노드 리턴"""
        temp = node  
        while temp.left_child is not None:
            temp = temp.left_child      
        return temp
        