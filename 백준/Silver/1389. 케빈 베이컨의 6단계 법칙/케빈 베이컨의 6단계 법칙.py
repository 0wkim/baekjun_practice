import sys

N, M = map(int, sys.stdin.readline().split())

graph = [[float('inf')] * (N+1) for _ in range(N+1)]

for i in range(1, N+1):
    # 자기 자신으로 가는 거리는 0으로 초기화
    graph[i][i] = 0

for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())

    # 친구 관계는 양방향
    graph[u][v] = 1
    graph[v][u] = 1

for k in range(1, N+1): # 경유할 노드 
    for i in range(1, N+1): # 출발 노드 
        for j in range(1, N+1): # 도착 노드 
            # i에서 j로 바로 가는 것보다 k를 거쳐 가는게 더 빠르면 갱신 
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

results = []
for i in range(1, N+1):
    # i번째 사람의 케빈 베이컨 수 
    kevin_sum = sum(graph[i][1:])
    results.append(kevin_sum)

print(results.index(min(results)) + 1)