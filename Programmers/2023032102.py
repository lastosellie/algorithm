import heapq

def solution(n, k, enemy):
    answer = -1
    sumHeap = 0
    heap = []
    for i, e in enumerate(enemy):
        sumHeap += e
        heapq.heappush(heap, -e)
        if sumHeap > n:
            if k <= 0:
                answer = i
                break
            k = k - 1
            a = -heapq.heappop(heap)
            sumHeap -= aon
    return len(enemy) if answer == -1  else answer

#print(solution(2, 4, [3, 3, 3, 3]))
#print(solution(7, 3, [4, 2, 4, 6, 3, 3, 1]))
print(solution(5, 2, [2, 2, 4, 4, 1, 3, 1]))
