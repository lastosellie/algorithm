'''
N개의 최소공배수
https://programmers.co.kr/learn/courses/30/lessons/12953
'''

def getGcd(a, b):
    tmp = 0
    while b != 0:
        tmp = b
        b = a % b
        a = tmp
    return a

def getLcm(a, b):
    return a * b // getGcd(a, b)

def solution(arr):
    lcm = arr[0]
    for i in range(1, len(arr)):
        lcm = getLcm(lcm, arr[i])
    return lcm

print(solution([7, 14, 39]))
print(solution([12, 18, 144]))
print(solution([16, 14, 12])) # 672
print(solution([16,14])) # 112
print(solution([2,6,8,14])) # 168
print(solution([1,2,3]))
print(solution([18, 24, 12]))
print(solution([1,2,3]))