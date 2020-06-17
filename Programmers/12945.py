'''
피보나치 수
https://programmers.co.kr/learn/courses/30/lessons/12945
'''

def solution(n):
    if n == 1 or n == 2:
        return 1
    a = b = 1
    answer = 0
    for i in range(3, n + 1):
        answer = a + b
        answer %= 1234567
        a = b
        b = answer
    return answer

print(solution(0))
print(solution(1))
print(solution(2))
print(solution(3))
print(solution(123456789))
print(dict)