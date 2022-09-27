import sys
import heapq
N = int(input())
dr = [-1, 1,0, 0]
dc = [0, 0, 1, -1]
pb_cnt = 1
INF = int(1e9)
while N != 0:
    board = []
    q = []
    for i in range(N):
        board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = board[0][0]
    start = (0,0,board[0][0])
    heapq.heappush(q, start)
    while q:
        r, c, cost = heapq.heappop(q)
        if cost < dist[r][c]:
            continue
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if cost + board[nr][nc] < dist[nr][nc]:
                    dist[nr][nc] = cost + board[nr][nc]
                    heapq.heappush(q, (nr, nc, cost + board[nr][nc]))
    print(f'Problem {pb_cnt}: {dist[N-1][N-1]}')
    pb_cnt += 1
    N = int(input())
