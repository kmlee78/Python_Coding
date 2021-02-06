def swap(tree, index_1, index_2):
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp

def heapify(tree, index, tree_size):
    left_child_index = 2 * index
    right_child_index = 2 * index + 1
    if right_child_index < tree_size:
        biggest = max(tree[index], tree[left_child_index], tree[right_child_index])
        if biggest == tree[left_child_index]:
            swap(tree, index, left_child_index)
            heapify(tree, left_child_index, tree_size)
        elif biggest == tree[right_child_index]:
            swap(tree, index, right_child_index)
            heapify(tree, right_child_index, tree_size)

def reverse_heapify(tree, index):
    """삽입된 노드를 힙 속성을 지키는 위치로 이동시키는 함수"""
    parent_index = index // 2
    if parent_index > 0 and tree[parent_index] < tree[index]:
        swap(tree, parent_index, index)
        reverse_heapify(tree, parent_index)


class PriorityQueue:
    """힙으로 구현한 우선순위 큐"""
    def __init__(self):
        self.heap = [None]  # 파이썬 리스트로 구현한 힙

    def insert(self, data):
        """삽입 메소드"""
        self.heap.append(data)      # 새로운 데이터를 힙의 가장 마지막 부분에 추가
        reverse_heapify(self.heap, len(self.heap)-1)

    def extract_max(self):
        """최우선순위 데이터 추출 메소드"""
        swap(self.heap, 1, len(self.heap) - 1)  # root 노드와 마지막 노드의 위치 바꿈
        max_value = self.heap.pop()  # 힙에서 마지막 노드 추출(삭제)해서 변수에 저장
        heapify(self.heap, 1, len(self.heap))  #  heapify 호출해서 힙 속성 유지
        return max_value  

    def __str__(self):
        return str(self.heap)

priority_queue = PriorityQueue()

priority_queue.insert(6)
priority_queue.insert(9)
priority_queue.insert(1)
print(priority_queue)       # [9, 6, 1]

print(priority_queue.extract_max())     # 9
