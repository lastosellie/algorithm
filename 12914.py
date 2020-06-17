'''
멀리 뛰기
https://programmers.co.kr/learn/courses/30/lessons/12914
'''

def dfs(a, n):
    s = sum(a)
    if s == n:
        print(a)
        a.pop()
        return 1
    elif s > n:
        a.pop()
        return 0
    a.append(1)
    sum1 = dfs(a, n)
    a.pop()
    a.append(2)
    sum2 = dfs(a, n)

def solution(n):
    answer = 0
    a = []
    a.append(1)
    dfs(a, n)
    return answer

print(solution(4))
print(solution(3))