from collections import defaultdict

graph = defaultdict(list)

def bfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)
    depth = 0
    leaf = []
    graph_info = defaultdict(list)
    graph_info[0].append(start_node)
    while need_visit:
        new_visit = []
        while need_visit:
            node = need_visit.pop(0)
            #if node not in visited:
            visited.append(node)
            if len(graph[node]) == 1:
                leaf.append(node)
            for next_node in graph[node]:
                if next_node not in visited:
                    new_visit.append(next_node)
                    graph_info[depth + 1].append(next_node)
        if len(new_visit) > 0:
            depth += 1
            need_visit = new_visit
    answer = []
    for key in graph_info.keys():
        if depth % 2 == 0: #짝수
            depth -= 1
            while depth >= 0:
                if depth % 2 == 1 or depth == 0:
                    answer.extend(graph_info[depth])
                depth -= 1
        else:
            while depth >= 0:
                if depth % 2 == 0 or depth == 0:
                    answer.extend(graph_info[depth])
                depth -= 1
    return (len([x for x in answer if x not in leaf]))
        #if key == 0 or key % 2 == 0:
        #print(key, graph_info[key], len(graph_info[key]))

    # print(visited, leaf)
    # print(graph_info)
    # print(graph)

def solution(n, lighthouse):
    for l, r in lighthouse:
        graph[l].append(r)
        graph[r].append(l)
    return bfs(graph, 1)

print(solution(8, [[1, 2], [1, 3], [1, 4], [1, 5], [5, 6], [5, 7], [5, 8]]))
#solution(10, [[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]])

'''
		2
10	[[4, 1], [5, 1], [5, 6], [7, 6], [1, 2], [1, 3], [6, 8], [2, 9], [9, 10]]	3
'''