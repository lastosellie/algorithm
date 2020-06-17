'''
체육복
https://programmers.co.kr/learn/courses/30/lessons/42862
'''

def solution(n, lost, reserve):
    sreserve = set(reserve)
    for i in range(len(lost) - 1):
        if lost[i] - 1 in sreserve:
            lost = lost[i:]
            sreserve.remove(lost[i] - 1)
        elif lost[i] + 1 in sreserve:
            lost = lost[i:]
            sreserve.remove(lost[i] + 1)
    return n - len(lost)

print(solution(5, [2, 4], [1, 3, 5]))