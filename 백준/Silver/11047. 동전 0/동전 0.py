import sys

# INPUT = list(map(int, sys.stdin.readline().split()))

# 그리디 알고리즘 
# 금액이 큰 동전부터 최대한 많이 사용할 것 

N, K = map(int, sys.stdin.readline().split())

coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline()))

count = 0
for coin in reversed(coins):
    if K == 0:
        break
    else:
        count += K // coin
        K = K % coin

print(count)    