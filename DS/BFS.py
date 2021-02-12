class Node:
    """그래프 노드 클래스"""
    def __init__(self, name):
        self.name = name
        self.adjacent = []
        self.visited = False
    
    def add_connection(self, node):
        self.adjacent.append(node)
        node.adjacent.append(self)


def bfs(graph, start_node):
    """너비 우선 탐색 알고리즘"""
    queue = deque()  # 빈 큐 생성
    # 일단 모든 노드를 방문하지 않은 노드로 표시
    for node in graph.values():
        node.visited = False   
    queue.append(start_node)
    while queue:
        temp = queue.popleft()
        print(temp.name)
        for neighbor in temp.adjacent:
            if neighbor.visited == False:
                neighbor.visited = True
                queue.append(neighbor)


# 노드들을 만들고 서로를 연결하는 그래프를 만드는 작업
passage = {}
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')
passage['A'] = node_a
passage['B'] = node_b
passage['C'] = node_c
passage['D'] = node_d
passage['E'] = node_e
passage['F'] = node_f
node_a.add_connection(node_b)
node_a.add_connection(node_c)
node_b.add_connection(node_a)
node_b.add_connection(node_d)
node_c.add_connection(node_a)
node_c.add_connection(node_e)
node_c,add_connection(node_f)
node_d.add_connection(node_b)
node_d.add_connection(node_e)
node_e.add_connection(node_c)
node_e.add_connection(node_d)
node_f.add_connection(node_c)
"""
A
| \
B  C
|  | \
D--E  F
"""

bfs(passage, passage['A'])  # A B C D E F