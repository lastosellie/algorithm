'''
예산
https://programmers.co.kr/learn/courses/30/lessons/12982
'''

def solution(d, budget):
    d.sort()
    for i in range(len(d), -1, -1):
        if sum(d[:i]) <= budget:
            return i
    return 0

print(solution([1,3,2,5,4], 9))