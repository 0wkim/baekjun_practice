import sys

# INPUT = list(map(int, sys.stdin.readline().split()))

N, M = map(int, sys.stdin.readline().split())

name_list = []
number = [i for i in range(1, N+1)]

for _ in range(N):
    name_list.append(sys.stdin.readline().strip())

poketmon_dict = dict(zip(name_list, number))

for _ in range(M):
    quest = sys.stdin.readline().strip()

    if quest.isdigit():
        print(name_list[int(quest)-1])
    else:
        print(poketmon_dict[quest])
