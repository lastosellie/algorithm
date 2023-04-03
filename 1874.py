def solution(n, nl):
    answer = []
    stack = []
    current = 1
    for num in nl:
        while current <= num:
            answer.append('+')
            stack.append(current)
            current += 1
        if stack[-1] == num:
            stack.pop()
            answer.append('-')
        else:
            print('NO')
            return
    return answer

n = int(input())
nl = []
for _ in range(n):
    nl.append(int(input()))

answer = solution(n, nl)
if answer:
    print('\n'.join(answer))
'''
8
4
3
6
8
7
5
2
1
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-
'''
'''
5
1
2
5
3
4
'''