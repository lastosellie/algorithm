from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
circle = list(map(int, input().split()))
queue = deque([i for i in range(1, n + 1)])
answer = []
while queue:
    first = queue.popleft()
    step = circle[first - 1]
    if step > 0:
        step -= 1
        queue.rotate(-step)
    else:
        #step += 1
        queue.rotate(-step)
    answer.append(first)
print(*answer)
'''
5
3 2 1 -3 -1
예제 출력 1 
1 4 5 3 2
'''
