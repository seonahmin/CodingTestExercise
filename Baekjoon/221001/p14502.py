import sys
from itertools import combinations
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())
board = []
ans = 0
max_val = 0
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
loc0 = []
loc2 = []
chk = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            loc0.append((i,j))
        elif board[i][j] == 2:
            loc2.append((i,j))
        else:
            chk[i][j] = True
all_case = list(combinations(loc0, 3))
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(loc2case):
    for sp in loc2case: 
        q = deque()
        r, c = sp
        q.append(sp)
        while q:
            now_r, now_c = q.popleft()
            cp_chk[now_r][now_c] = True
            for i in range(4):
                nr, nc = now_r + dr[i], now_c + dc[i]
                if 0<=nr<n and 0<=nc<m and cp_chk[nr][nc]==False and cp_board[nr][nc] == 0:
                    cp_board[nr][nc] = 2
                    q.append((nr, nc))

for case in all_case: # 64*63*62 / 6
    # 전염될 보드 초기화
    ans = 0
    cp_board = [i[:] for i in board]
    cp_chk = [i[:] for i in chk]
    # 벽 세울 수 있는 케이스 전체 탐색
    for cc in case:
        cp_board[cc[0]][cc[1]] = 1
    # 전염시키는 케이스
    bfs(loc2)
    # 전염된 지역 카운트
    for i in range(n):
        for j in range(m):
            if cp_board[i][j] == 0:
                ans += 1
    if max_val < ans:
        max_val = ans
    

print(max_val)