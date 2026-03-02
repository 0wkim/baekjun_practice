import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
S = sys.stdin.readline().rstrip()

answer = 0
count = 0 # 연속된 "OI"의 개수
i = 0

while i < (M - 2):
    if S[i:i+3] == "IOI":
        count += 1 
        i += 2

        if count == N:
            answer += 1
            count -= 1 # 겹치는 경우를 고려하기 위함 (중첩 허용)

    else:
        # 패턴이 끊기면 초기화
        count = 0
        i += 1 

print(answer)