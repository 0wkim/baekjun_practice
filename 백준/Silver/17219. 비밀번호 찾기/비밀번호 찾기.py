import sys

# INPUT = list(map(int, sys.stdin.readline().split()))

# key: 주소, value: 비밀번호 

N, M = map(int, sys.stdin.readline().split())

pwd_list = []
addr_list = []

for _ in range(N):
    address, password = sys.stdin.readline().split()
    addr_list.append(address)
    pwd_list.append(password)

pwd_dict = dict(zip(addr_list, pwd_list))

for _ in range(M):
    find_addr = sys.stdin.readline().strip()
    print(pwd_dict[find_addr])

