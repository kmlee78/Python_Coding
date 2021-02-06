def swap(tree, index_1, index_2):
    """완전 이진 트리의 노드 index_1과 노드 index_2의 위치를 바꿔준다"""
    temp = tree[index_1]
    tree[index_1] = tree[index_2]
    tree[index_2] = temp

def heapify(tree, index, tree_size):
    """heapify 함수"""
    # 자식 노드 인덱스 계산
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

def heapsort(tree):
    """힙 정렬 함수"""
    tree_size = len(tree)
    # 일단 힙을 만들고
    for index in range(tree_size, 0, -1):
        heapify(tree, index, tree_size)
    # root와 마지막 노드의 위치를 바꾸고 바뀐 마지막 노드를 제외한 힙을 다시 heapify
    for count in range(tree_size-1, 0, -1):
        swap(tree, 1, count)
        heapify(tree, 1, count)

data_to_sort = [None, 6, 1, 4, 7, 10, 3, 8, 5, 1, 5, 7, 4, 2, 1]
heapsort(data_to_sort)
print(data_to_sort)
