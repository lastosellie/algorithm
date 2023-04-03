import sys
from collections import deque 
input = sys.stdin.readline

n, m = list(map(int, input().split()))
numbers = list(map(int, input().split()))
queue = deque([i for i in range(1, n + 1)])
answer = 0

for number in numbers:
    diff = queue.index(number) - 0
    if diff != 0:
        reverseDiff = len(queue)  - diff
        if reverseDiff >= diff:
            queue.rotate(-diff)
            answer += diff
        elif reverseDiff < diff:
            queue.rotate(reverseDiff)
            answer += reverseDiff
    if queue[0] == number:
        queue.popleft()
    
print(answer)
'''
10 3
1 2 3
0

10 3
2 9 5
8

32 6
27 16 30 11 6 23
59

10 10
1 6 3 2 7 9 8 4 10 5
14
'''