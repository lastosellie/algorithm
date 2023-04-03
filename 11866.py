from collections import deque
import sys
input = sys.stdin.readline
n, step = list(map(int, input().split()))
step -= 1
queue = deque([i for i in range(1, n + 1)])
answer = []
while queue:
    queue.rotate(-step)
    answer.append(queue.popleft())

print("<", end='')
print(', '.join(map(str, answer)), end='')
print(">")
'''
7 3
<3, 6, 2, 7, 5, 1, 4>
'''