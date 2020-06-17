'''
2016년
https://programmers.co.kr/learn/courses/30/lessons/12901
'''

import datetime
def solution(a, b):
    answers = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    return answers[datetime.date(2016,a,b).weekday()]

print(solution(5, 24))