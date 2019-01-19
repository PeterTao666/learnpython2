from collections import deque
q = deque(['a','b','c'])
print(q[0])

q.append('d')
print(q[-1])

q.appendleft('x')
print(q[0])
