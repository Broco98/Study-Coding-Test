
# https://www.acmicpc.net/problem/11047

from collections import deque

# n, k 입력
n, k = map(int, input().split())

data = deque()

result = 0

for i in range(n):
    data.appendleft(int(input()))

for i in data:
    if k < i or k == 0:
        continue

    result += k // i
    k -= i * (k // i)

print(result)