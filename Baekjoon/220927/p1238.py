import sys
import heapq
INF = int(1e9)
N, M, X = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(N)]
for i in range(M):
    s, e, w = map(int, sys.stdin.readline().rstrip().split())
    graph[s-1].append((e-1, w))
answer = []
def dijkstra(start, end):
    heap = []
    dist = [INF for _ in range(N)]
    dist[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        weight, node = heapq.heappop(heap)
        if weight < dist[node]:
            continue

        for e, w in graph[node]:
            if w + weight < dist[e]:
                dist[e] = w + weight
                heapq.heappush(heap, (w + weight, e))
    return dist[end]

for i in range(N):
    answer.append(dijkstra(i, X-1) + dijkstra(X-1, i))

print(max(answer))