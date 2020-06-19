'''
카펫
https://programmers.co.kr/learn/courses/30/lessons/42842
'''

def solution(brown, yellow):
    setxy = []
    for y in range(1, yellow + 1):
        q, r = divmod(yellow, y)
        if q > 0 and r == 0:
            x = q + 2
            y = y + 2
            if 2 * (x + y - 2) == brown:
                return [x, y]
    return None
        
print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))