import sys

K, N = map(int, sys.stdin.readline().split())

lines = []
for _ in range(K):
    lines.append(int(sys.stdin.readline()))

low = 1 # 랜선을 자를 수 있는 가장 짧은 길이(최솟값)
high = max(lines) # 랜선의 길이의 최댓값

now_len = 0

while low <= high:
    mid = (low + high) // 2 # 테스트용 길이 (이분 탐색의 기준점)
    total = 0 # mid 길이로 랜선을 잘랐을때의 총 조각 수

    for line in lines:
        total += (line // mid)

    if total >= N:
        now_len = mid
        low = mid + 1
    elif total < N:
        high = mid - 1        

print(now_len)