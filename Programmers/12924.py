'''
숫자의 표현
https://programmers.co.kr/learn/courses/30/lessons/12924
'''

def solution_sub(n):
    answer = []
    for i in range(1, n):
        sum = i
        list = [i]
        for j in range(i + 1, n):
            sum += j
            list.append(j)
            if sum == n:
                answer.append(list)
                break
            if sum >= n:
                break
    return answer

def solution(n):
    answer = 0
    for i in range(1, n):
        sum = i
        for j in range(i + 1, n):
            sum += j
            if sum == n:
                answer += 1
                break
            if sum >= n:
                break
    return answer + 1

print(solution(15))