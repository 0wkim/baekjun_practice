import sys

T = int(sys.stdin.readline())


def solution(str):
    left = []
    is_correct = True

    for i in range(len(s)):
        if str[i] == "(":
            left.append(str[i])
        elif str[i] ==  ")":
            if left:
                left.pop()
            else: # 짝이 안맞는 경우
                is_correct = False
                break
    
    # 짝이 안맞는 경우
    if left:
        is_correct = False

    if is_correct:
        print("YES")
    else:
        print("NO")

for _ in range(T):
    s = sys.stdin.readline()
    solution(s)    