import math
import copy
import heapq
#imoticon
discounts = {10:0.9, 20:0.8, 30:0.7, 40:0.6}
def dfs(users, emoticons, i, rates, answer):
    if i >= len(emoticons):
        ticket = 0
        amount = 0
        for user in users:
            userAmount = 0
            for i, rate in enumerate(rates):
                if rate >= user[0]:
                    userAmount += math.floor(discounts[rate] * emoticons[i])
            if userAmount >= user[1]:
                ticket += 1
            else:
                amount += userAmount
            #answer.append([ticket, amount])
            heapq.heappush(answer, [-ticket, -amount])
        return
    for d in discounts.keys():
        b = copy.deepcopy(rates)
        b.append(d)
        dfs(users, emoticons, i + 1, b, answer)
    
def solution(users, emoticons):
    answer = []
    dfs(users, emoticons, 0, [], answer)
    return list(map(lambda x: x * -1, heapq.heappop(answer)))
print(solution([[40, 10000], [25, 10000]], [7000, 9000]))




    












#print(solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]], [1300, 1500, 1600, 4900]))

'''
# [4, 13860]
입력값 〉	[[40, 10000], [25, 10000]], [7000, 9000]
기댓값 〉	[1, 5400]
'''