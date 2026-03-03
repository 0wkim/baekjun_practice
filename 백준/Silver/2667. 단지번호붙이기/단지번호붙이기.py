import sys
from collections import deque
sys.setrecursionlimit(10**6)

# NxN 크기의 지도
N = int(sys.stdin.readline())

# DFS (깊이 우선 탐색)
# 한 방향으로 최대한 깊이 가다가, 
# 더이상 갈 곳이 없으면 가장 마지막에 만난 갈림길로 돌아가 다른 방향 탐색 
# 구현: 재귀 함수, 스택
# visited로 방문 처리 

# BFS (너비 우선 탐색)
# 시작 정점으로부터 가까운 정점을 먼저 방문하고, 멀리 떨어진 것을 나중에 방문
# 구현: 큐(collections.deque)
# 큐에서 노드를 하나씩 꺼내며 연결된 노드 중 방문하지 않은 곳을 큐에 넣어 방문 처리

all_map = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().strip()))
    all_map.append(line)

visited_bfs = [[False] * N for _ in range(N)]
# 단지별 집의 수를 저장할 리스트 
danji_homes = []

def bfs(r, c):
    queue = deque([(r, c)])
    visited_bfs[r][c] = True

    # 단지 개수 카운트
    count = 1

    # 상하 좌우 
    move_r = [-1, 1, 0, 0]
    move_c = [0, 0, -1, 1]

    while queue:
        # 이전 칸
        curr_r, curr_c = queue.popleft()

        for i in range(4):
            nr = curr_r + move_r[i]
            nc = curr_c + move_c[i]

            if 0 <= nr < N and 0 <= nc < N:
                if all_map[nr][nc] == 1 and not visited_bfs[nr][nc]:
                    visited_bfs[nr][nc] = True 
                    queue.append((nr, nc))
                    count += 1
    return count

# 지도를 순회하며 방문하지 않은 집을 찾으면 BFS 시작 
for i in range(N):
    for j in range(N):
        if all_map[i][j] == 1 and not visited_bfs[i][j]:
            # 새로운 단지 발견 시 BFS를 호출하고 결과를 리스트에 저장
            danji_homes.append(bfs(i, j))

# 총 단지 수
print(len(danji_homes))

# 각 단지 내 집의 개수 
danji_homes.sort()
for count in danji_homes:
    print(count)