'''
최댓값과 최솟값
https://programmers.co.kr/learn/courses/30/lessons/12939
'''

def solution(s):
    answer = [int(i) for i in s.split(" ")]
    answer.sort()
    answer = answer[:1] + answer[-1:]
    return ' '.join(str(e) for e in answer)

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))
print(solution("-1 -1"))
