'''
완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42840/solution_groups?language=python3&type=my

hash(object)
객체의 해시값을 돌려준다(해시가 있는 경우)
해시값은 정수다
딕셔너리 조회 중에 딕셔너리 키를 빨리 비교하는 데 사용된다
같다고 비교되는 숫자 값은 같은 해시값을 갖는다
'''

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    return answer
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))