













n = 3
numList = [1, 2, 3]
visited = [0] * (n + 1)

def dfs(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if visited[i] == 1:
                print(i, end=" ")
        print()
    else:
        visited[v] = 1
        dfs(v + 1)
        visited[v] = 0
        dfs(v + 1)

if __name__ == "__main__":
    dfs(1)