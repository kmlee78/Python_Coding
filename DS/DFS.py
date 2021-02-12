from collections import deque

class Node:
    """그래프 노드 클래스"""
    def __init__(self, name):
        self.name = name
        self.adjacent = []
        self.visited = 0    # 접근 자체를 안했을 때 0, 스택에 있으면 1, 방문한 적이 있으면 2
    
    def add_connection(self, node):
        self.adjacent.append(node)
        node.adjacent.append(self)


def dfs(graph, start_node):
    """깊이 우선 탐색 알고리즘"""
    stack = deque()  # 빈 스택 생성
    # 모든 노드를 처음 보는 노드로 초기화
    for node in graph.values():
        node.visited = 0
    # 첫 노드를 스택 처리(1) 후 스택에 넣는다
    start_node.visited = 1
    stack.append(start_node)

    while stack:
        temp = stack.pop()
        print(temp.name)
        temp.visited = 2
        for neighbor in temp.adjacent_stations:
            if neighbor.visited == 0:
                neighbor.visited = 1
                stack.append(neighbor)


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
node_c,add_connection(node_f)
node_d.add_connection(node_b)
node_d.add_connection(node_e)
node_e.add_connection(node_d)
node_f.add_connection(node_c)
"""
A
| \
B  C
|   \
D-E  F
"""

bfs(passage, passage['A'])  # A B D E C F