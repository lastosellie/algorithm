'''
소수 찾기
https://programmers.co.kr/learn/courses/30/lessons/12921
'''

import math
def isPrime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def solution(n):
    answer = 0
    for num in range(2, n+1):
        if isPrime(num):
            print(num)
            answer += 1
    return answer

print(solution(10))