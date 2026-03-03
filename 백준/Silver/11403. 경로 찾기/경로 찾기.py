import sys

N = int(sys.stdin.readline())

graph = []
for _ in range(N):
    line = list(map(int, sys.stdin.readline().split()))
    graph.append(line)

for k in range(N): # 경유할 노드 
    for i in range(N): # 출발 노드 
        for j in range(N): # 도착 노드 
            # 만약 i -> k -> j로 갈 수 있다면 
            # 사이클 패턴이 있으면 대각선도 1이 될 수 있음 
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for row in graph:
    print(*(row))