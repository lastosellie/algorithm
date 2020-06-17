'''
시저 암호
https://programmers.co.kr/learn/courses/30/lessons/12926
'''

def solution(s, n):
    answer = ''
    n = n % 26
    for i in s:
        if i.isalpha():
            o = ord(i) + n
            if i.isupper() and o > 90:
                o -= 26
            elif i.islower() and o > 122:
                o -= 26
            answer += chr(o)
        else:
            answer += i
    return answer

print(solution("ABZ", 1))
print(solution("a B z", 126))
print(solution("AaZz", 25))  #ZzYy
