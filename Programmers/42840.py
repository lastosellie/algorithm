'''
모의고사
https://programmers.co.kr/learn/courses/30/lessons/42840
'''

def solution(answers):
    answer = {'1': 0, '2': 0, '3': 0}
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i, n in enumerate(answers):
        if a[i % len(a)] == n: answer['1'] += 1
        if b[i % len(b)] == n: answer['2'] += 1
        if c[i % len(c)] == n: answer['3'] += 1
    return [int(key) for key in answer if answer[key] == max(answer.values())]

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))