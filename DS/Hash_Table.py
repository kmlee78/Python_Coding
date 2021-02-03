"""
Chaining을 이용한 해시 테이블 구현.
배열 인덱스에 링크드 리스트를 저장해서 같은 key값을 가지는 
다른 두 key-value쌍 간의 충돌을 해결 
"""
class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None  
        self.prev = None  

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  
        self.tail = None  
 
    def find_node_with_key(self, key):
        iterator = self.head 
        while iterator is not None:
            if iterator.key == key:
                return iterator
            iterator = iterator.next
        return None

    def append(self, key, value):
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node 
            new_node.prev = self.tail
            self.tail = new_node 

    def delete(self, node_to_delete):
        if node_to_delete is self.head and node_to_delete is self.tail:
            self.tail = None
            self.head = None
        elif node_to_delete is self.head:
            self.head = self.head.next
            self.head.prev = None
        elif node_to_delete is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev


class HashTable:
    """해시 테이블 클래스"""
    def __init__(self, capacity):
        self._capacity = capacity  # 파이썬 리스트 수용 크기 
        self._table = [LinkedList() for _ in range(self._capacity)]  # 파이썬 리스트 인덱스에 반 링크드 리스트 저장

    def _hash_function(self, key):
        """해시 함수"""
        return hash(key) % self._capacity

    def look_up_value(self, key):
        """
        주어진 key에 해당하는 데이터를 리턴하는 메소드
        """
        index = self._hash_function(key)
        Llist = self._table[index]
        iterator = Llist.head
        return Llist.find_node_with_key(key)
            
    def insert(self, key, value):
        """
        새로운 key-value 쌍을 삽입시켜주는 메소드
        이미 해당 key에 저장된 데이터가 있으면 해당 key에 해당하는 데이터를 바꿔줌
        """
        index = self._hash_function(key)
        Llist = self._table[index]
        check = Llist.find_node_with_key(key)
        if check is None:
            Llist.append(key, value)
        else:
            check.value = value

     def delete_by_key(self, key):
        """주어진 key에 해당하는 key-value 쌍을 삭제하는 메소드"""
        index = self._hash_function(key)
        Llist = self._table[index]
        del_node = Llist.find_node_with_key(key)
        if del_node is not None:
            Llist.delete(del_node)

    def __str__(self):
        """해시 테이블 문자열 메소드"""
        res_str = ""

        for linked_list in self._table:
            res_str += str(linked_list)

        return res_str[:-1]

 
test_scores = HashTable(50)  # 해시 테이블 인스턴스 생성

# 이름과 시험 점수 삽입
test_scores.insert("KM", 85)
test_scores.insert("SH", 90)
test_scores.insert("DH", 87)
test_scores.insert("JS", 99)

print(test_scores)

# key인 이름으로 특정 이름의 시험 점수 검색
print(test_scores.look_up_value("KM"))
print(test_scores.look_up_value("JS"))

# 시험 점수 수정 또는 추가
test_scores.insert("DH", 10)
test_scores.insert("HI", 20)

print(test_scores)

# 시험 정보 삭제
test_scores.delete_by_key("JH")
test_scores.delete_by_key("HI")

print(test_scores)