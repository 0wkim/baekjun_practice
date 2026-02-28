import sys

N = int(sys.stdin.readline())

# 제곱수 저장
squares = []
j = 1
while j*j <= N:
    squares.append(j*j)
    j += 1

# 답인 1인 경우(N 자체가 제곱수)
# **0.5 = 제곱근(루트)
if int(N**0.5)**2 == N:
    print(1)
    exit()

# 답이 2인 경우(제곱수 하나를 뺐을때 남은 수가 제곱수)
for square in squares:
    if square > N: # 뺴는 제곱수가 더 큰 경우 중단
        break

    if int((N-square)**0.5)**2 == (N-square):
        print(2)
        exit()

# 답이 3인 경우(제곱수 두개를 뺐을때 남은 수가 제곱수)
# 답이 3인 경우에는 N = a^2+b^2+c^2이므로, N-a^2-b^2 = c^2이 되는 것을 확인해야 함
for i in range(len(squares)):
    for j in range(i, len(squares)): # i제외 나머지 중 j
        if N-squares[i]-squares[j] < 0: # 제곱수를 모두 뺐을때 음수값이 나오면 중단
            break
        
        if int((N-squares[i]-squares[j])**0.5)**2 == N-squares[i]-squares[j]:
            print(3)
            exit()

# 남은 경우
print(4)
