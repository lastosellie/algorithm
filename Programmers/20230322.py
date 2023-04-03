# def sumDp(cap, n, dp):
#     distance = 0
#     for i in range(n - 2, -1, -1):
#         if i > len(dp) - 2:
#             continue
#         nd = dp[i][0] + dp[i + 1][0]
#         np = dp[i][1] + dp[i + 1][1]
        
#         if nd == cap and np == cap:
#             distance += dp[i + 1][2] * 2
#             del dp[i + 1]
#             del dp[i]
#         elif nd <= cap and np <= cap:
#             dp[i][0], dp[i][1], dp[i][2] = nd, np, dp[i + 1][2]
#             del dp[i + 1]
#     return distance

def solution(cap, n, deliveries, pickups):
    answer = 0
    d = 0
    p = 0
    
    for i in range(n - 1, -1, -1):
        d -= deliveries[i]
        p -= pickups[i]
        count = 0
        while d < 0 or p < 0:
            d += cap
            p += cap
            count += 1
        answer += ((i + 1) * count * 2)
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))























