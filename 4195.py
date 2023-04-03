#from collections import defaultdict

testCases = int(input())

def find(relDict, x):
    if relDict[x] == x:
        return x
    else:
        p = find(relDict, relDict[x])
        relDict[x] = p
        return relDict[x]

def union(relDict, left, right, number):
    nleft = find(relDict, left)
    nright = find(relDict, right)
    if nleft != nright:
        relDict[nright] = nleft
        number[nleft] += number[nright]

for testCase in range(testCases):
    relDict = {}
    number = {}
    relations = int(input())
    for relation in range(relations):
        left, right = list(input().split())
        if not left in relDict:
            relDict[left] = left
            number[left] = 1
        if not right in relDict:
            relDict[right] = right
            number[right] = 1
        union(relDict, left, right, number)
    print(relDict)
    print(number[find(relDict, left)])

'''
1
4
Fred Barney
Betty Wilma
Barney Wilma
Barney Wilma


1
3
Fred Barney
Barney Betty
Betty Wilma

2
3
Fred Barney
Barney Betty
Betty Wilma
3
Fred Barney
Betty Wilma
Barney Betty

def bfs(realDict, start):
    visited, need_visit = list(), list()
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop(0)
        if not node in visited:
            visited.append(node)
            nodes = realDict[node]
            need_visit.extend(nodes)
    return len(visited)

def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    
    return visited
'''