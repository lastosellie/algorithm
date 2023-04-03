def dfs(cards, i, g1, visited):
    if visited[i]:
        return
    num = cards[i]
    g1.append(num)
    visited[i] = True
    dfs(cards, num -1, g1, visited)

def solution(cards):
    answer = 0
    l = len(cards)
    for i in range(l):
        visited = [False for _ in range(l)]
        g1 = []
        dfs(cards, i, g1, visited)
        for j in range(l):
            g2 = []
            dfs(cards, j, g2, visited)
            answer = max(len(g1) * len(g2), answer)
    return answer

print(solution([8, 6, 3, 7, 2, 5, 1, 4]))