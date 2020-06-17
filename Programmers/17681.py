'''
[1차] 비밀지도
https://programmers.co.kr/learn/courses/30/lessons/17681?language=python3
'''

def solution(n, arr1, arr2):
    answer = []
    #print(bin(6)[2:])
    fm = '{0:0' + str(n) + 'b}'
    for i in range(n):
        sarr1 = fm.format(arr1[i])
        sarr2 = fm.format(arr2[i])
        sarr = ''
        for j in range(n):
            if int(sarr1[j]) | int(sarr2[j]) == 0:
                sarr += " "
            else:
                sarr += "#"
        answer.append(sarr)
    return answer

n = 5
arr = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr, arr2))