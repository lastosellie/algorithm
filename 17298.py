import sys
input = sys.stdin.readline

testCase = int(input())
numbers = list(map(int, input().split()))
stack = []
answer = [-1 for _ in range(testCase)]

for i, number in enumerate(numbers):
    if len(stack) and stack[-1][0] >= number:
        stack.append((number, i))
    else:
        while stack:
            preNumber, preIndex = stack.pop()
            if preNumber >= number:
                stack.append((preNumber, preIndex))
                break
            else:
                answer[preIndex] = number
        stack.append((number, i))

print(*answer)

'''
4
3 5 2 7

4
9 5 4 8
'''