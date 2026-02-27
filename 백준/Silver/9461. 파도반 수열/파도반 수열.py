import sys

T = int(sys.stdin.readline())

def solution(N):
    P = [0, 1, 1, 1]

    if N <= 3:
        print(1)
    else:
        for i in range(4, N+1):
            P.append(P[i-2] + P[i-3])
        print(P[N])

for _ in range(T):
    N = int(sys.stdin.readline())
    solution(N)