'''
나누어 떨어지는 숫자 배열
https://programmers.co.kr/learn/courses/30/lessons/12910
'''

def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]

print(solution([5, 9, 7, 10], 5))
