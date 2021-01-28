class Node:
    """노드 클래스"""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    def find_node_at(self, index):
        """접근 연산 메소드"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator

    def find_node_with_data(self, data):
        """링크드 리스트 탐색 연산 메소드. 해당 노드가 없으면 None을 리턴"""
        iterator = self.head
        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next
        return None

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)
        if self.head is None:       # 링크드 리스트가 비어있는 경우
            self.head = new_node
            self.tail = new_node
        else:                       # 비어있지 않는 경우
            self.tail.next = new_node
            self.tail = new_node

    def insert_after(self, previous_node, data):
        """링크드 리스트 삽입 연산 메소드"""
        new_node = Node(data)
        if previous_node is self.tail:      # 가장 마지막에 삽입하는 경우
            self.tail.next = new_node
            self.tail = new_node
        else:                               # 그렇지 않은 경우
            new_node.next = previous_node.next
            previous_node.next = new_node

    def prepend(self, data):
        """링크드 리스트의 가장 앞에 데이터 삽입"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def delete_after(self, previous_node):
        """링크드 리스트 삭제 연산 메소드"""
        if previous_node.next is self.tail:     # 지우려는 노드가 tail인 경우
            previous_node.next = None
            self.tail = previous_node
        else:
            previous_node.next = previous_node.next.next
    
    def pop_left(self):
        """링크드 리스트의 가장 앞 노드 삭제 메소드. 링크드 리스트에 항상 노드가 있다고 가정"""
        pop_data = self.head
        if self.head is self.tail:      # 노드가 하나만 있는 경우
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return pop_data.data

    def __str__(self):
        """링크드 리스트 안의 내용물 출력"""
        res_str = ""
         iterator = self.head
        while iterator is not None:
            res_str += iterator.data + "  "
             iterator = iterator.next
        return res_str


#링크드 리스트 만들고 데이터 추가
my_list = LinkedList()
my_list.append(2)
my_list.append(3)
my_list.append(5)
print(my_list)          # 2 3 5

node_1 = my_list.find_node_at(1)
print(node_1.data)     # 3

my_list.insert_after(node_1, 4)
my_list.prepend(1)

node_4 = my_list.find_node_with_data(4)
my_list.delete_after(node_4)
print(my_list)          # 1 2 3 4