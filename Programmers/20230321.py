from collections import deque

def solution(numbers):
    answer = 0
    '''
    123
    456
    789
    *0#
    '''
    n = [
        [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
        [6, 2, 1, 2, 3, 2, 3, 5, 4,ser 5],
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],
    ]
    currDict = {}
    currDict[(4, 6)] = 0
    for number in numbers:
        num = int(number)
        newDict = {}
        for pos, v in currDict.items():
            x, y = pos
            if not (num, y) in newDict.keys() or newDict[(num, y)] > v + n[x][num]:
                if num != y:
                    newDict[(num, y)] = v + n[x][num]
            if not (x, num) in newDict.keys() or newDict[(x, num)] > v + n[y][num]:
                if num != x:
                    newDict[(x, num)] = v + n[y][num]
        currDict = newDict
    return min(currDict.values())

print(solution("151506"))
# print(solution("5123"))