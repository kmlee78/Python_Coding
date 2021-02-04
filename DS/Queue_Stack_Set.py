from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.qppend(3)
# 큐 출력
print(queue)	# deque([1, 2, 3])
# 맨 앞 데이터 접근
print(queue[0])	# 1
# 맨 앞 데이터 삭제, 리턴
print(queue.popleft())	# 1

stack = deque()
stack.append(2)
stack.append(3)
# 스택 출력
print(stack)
# 맨 끝 데이터 접근
print(stack[-1])	# 3
# 맨 끝 데이터 삭제, 리턴
print(stack.pop())	# 3

classes = set()
classes.add('A')
classes.add('B')
classes.add('B')
print(classes)  	# {'B', 'A'}		순서 상관, 중복 X
# 데이터 탐색
print('A' in classes)		# True
# 데이터 삭제
classes.remove('B')
