import sys
from collections import deque
sys.setrecursionlimit(10**6)

# N: 정점 개수, M: 간선 개수, V: 시작 정점 번호
N, M, V = map(int, sys.stdin.readline().split())

# DFS (깊이 우선 탐색)
# 한 방향으로 최대한 깊이 가다가, 
# 더이상 갈 곳이 없으면 가장 마지막에 만난 갈림길로 돌아가 다른 방향 탐색 
# 구현: 재귀 함수, 스택
# visited로 방문 처리 

# BFS (너비 우선 탐색)
# 시작 정점으로부터 가까운 정점을 먼저 방문하고, 멀리 떨어진 것을 나중에 방문
# 구현: 큐(collections.deque)
# 큐에서 노드를 하나씩 꺼내며 연결된 노드 중 방문하지 않은 곳을 큐에 넣어 방문 처리

graph = [[] for _ in range(N+1)]

# 그래프 간선 연결 (양방향)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    graph[u].append(v)
    graph[v].append(u)

# 번호가 낮은 순서대로 방문해야 하므로 정렬 
for i in range(1, N+1):
    graph[i].sort()
# ex) graph[1] = [2, 3, 4] -> 1번 노드가 2, 3, 4번과 연결

# ex) 1번 노드에 2, 3, 4번 연결
def dfs(v):
    # 1 출력 및 방문 처리 
    visited_dfs[v] = True
    print(v, end=' ')

    # 2 확인 
    for next_node in graph[v]:
        if not visited_dfs[next_node]:
            # 2번 노드에 방문하지 않았으므로 dfs(2) 호출 
            dfs(next_node)

def bfs(v):
    queue = deque([v])
    visited_bfs[v] = True

    # 큐가 빌 때까지 반복
    while queue:
        current = queue.popleft()
        print(current, end=' ')

        # 현재 노드와 연결된 노드들 확인 
        for next_node in graph[current]:
            if not visited_bfs[next_node]:
                # 큐에 넣고 방문 처리
                # 큐의 역할: 현재 노드에서 갈 수 있는 다음 후보들을 저장해두는 곳 (이후 순서대로 꺼내어 방문)
                queue.append(next_node)
                visited_bfs[next_node] = True


visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)
dfs(V)
print()
bfs(V)