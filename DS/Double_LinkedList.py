class Node:
    def __init__(self, data):
        self.data = data	
        self.next = None	
        self.prev = None	# 전 노드에 대한 레퍼런스 prev 추가

class LinkedList:
    """ __init__	find_node_at()	 find_node_with_data()	__str__ 
        이 4개의 메소드는 싱글 링크드 리스트랑 같다"""

    def __init__(self):
        self.head = None	
        self.tail = None

    def find_node_at(self, index):
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator

    def find_node_with_data(self, data):
    iterator = self.head  
    while iterator is not None:
        if iterator.data == data:
            return iterator
        iterator = iterator.next
    return None

    def __str__(self):
        res_str = ""
         iterator = self.head
        while iterator is not None:
            res_str += iterator.data + "  "
             iterator = iterator.next
        return res_str

    """여기서부터는 다름"""

    def append(self, data):
        new_node = Node(data)
        if self.head is None:	
            self.head = new_node
            self.tail = new_node
        else:	
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_after(self, previous_node, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)
        if previous_node is self.tail:
            previous_node.next = new_node
            new_node.prev = previous_node
            self.tail = new_node
        else:
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next = new_node
            previous_node.next.prev = new_node

    def prepend(self, data):
        """링크드 리스트 가장 앞에 데이터를 추가시켜주는 메소드"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def delete(self, node_to_delete):
        """더블 링크드 리스트 삭제 연산 메소드"""
        if node_to_delete == self.head and node_to_delete == self.tail:     # 노드가 하나일 때
            self.head = None
            self.tail = None
        elif node_to_delete == self.head:           # 맨 앞 노드를 삭제할 때
            self.head = node_to_delete.next
            self.head.prev = None
        elif node_to_delete == self.tail:           # 맨 뒤 노드를 삭제할 때
            self.tail = node_to_delete.prev
            self.tail.next = None
        else:                                       # 그 외 노드 사이에 있는 노드 삭제
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
        return node_to_delete.data