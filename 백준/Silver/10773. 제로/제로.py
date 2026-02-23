import sys

K = int(sys.stdin.readline())

num_list = []

for _ in range(K):
    num = int(sys.stdin.readline())

    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)

num_sum = sum(num_list)
print(num_sum)
