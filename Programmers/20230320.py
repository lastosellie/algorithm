import math
## 점찍기
def solution(k, d):
    answer = 0
    for x in range(0, d + 1, k):
        r = math.floor(math.sqrt(d**2 - x **2))
        answer += r//k + 1
    return answer

print(solution(2, 4))
print(solution(1, 5))