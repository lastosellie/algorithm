# 각 사원마다 근무 태도 점수, 동료 평가 점수
# 어떤 사원이 다른 임의의 사원보다 두 점수가 모두 낮은 경우 인센티브 못 받음
# 그렇지 않은 사원들은 두 점수의 합이 높은 순으로 석차 내어 석차에 따른 인센티브 차등 지급
# 두 점수 합 동일하면 동석차, 그만큼 다음 석차 건너 뜀
def solution(scores):
    target = scores[0]
    scores.sort(key=lambda x: (-x[0], x[1]))
    maxL, answer = 0, 1
    for s in scores:
        if target[0] < s[0] and target[1] < s[1]:
            return -1
        
        if maxL <= s[1]:
            if sum(target) < sum(s):
                answer += 1
            maxL = s[1]
    return answer
print(solution([[1, 9], [4, 8], [4, 7], [3, 9], [3, 8]]))
print(solution([[2, 9], [5, 9], [4, 8]]))












'''
print(solution([[4, 1], [4, 1], [4, 6], [3, 5], [0, 6], [3, 6]]))
print(solution([[2, 2], [2, 2], [2, 3], [3, 2]])) #3
print(solution([[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]])) #4
print(solution([[1, 1], [1, 1], [1, 1], [1, 1], [1, 1]])) # 1
print(solution([[3, 4], [4, 4],[4, 3], [3, 2], [3, 1]]))
'''
    # scores = list(filter(lambda x: sum(x) > sum(target), scores))
    # scores.append(target)
    # l = len(scores)
    # invalid = 0
    # for i in range(l):
    #     for j in range(i + 1, l):
    #         if scores[i][0] == -1 or scores[j][0] == -1 or scores[i][1] == -1 or scores[j][0] == -1:
    #             break
    #         if scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]:
    #             scores[i][0], scores[i][1] = -1, -1
    #             invalid += 1
    # if target in scores:
    #     return len(scores) - invalid
    # else:
    #     return -1

