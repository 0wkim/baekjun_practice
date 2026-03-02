import sys
from collections import Counter

N, M = map(int, sys.stdin.readline().split())

trees = Counter(map(int, sys.stdin.readline().split()))

low = 1 
high = max(trees.keys()) 

now_len = 0

while low <= high:
    mid = (low + high) // 2 # 테스트용 길이 (이분 탐색의 기준점)
    total = 0 

    for height, cnt in trees.items():
        if height > mid: # 절단기보다 나무가 높다면 
            total += (height - mid) * cnt # (나무 높이 - 절단기 높이) * 해당 높이의 나무 개수 

    if total >= M:
        now_len = mid
        low = mid + 1
    elif total < M:
        high = mid - 1        

print(now_len)