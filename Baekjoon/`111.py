from collections import deque
import sys
input = sys.stdin.readline
n = int(input())

arr = deque([])
for i in range(n) :
    s = input().split()

    if s[0] == 'push':
        arr.append(int(s[-1]))
    elif s == 'pop':
        if arr:
            print(arr.popleft())
        else:
            print(-1)
    elif s == 'size':
        print(len(arr))
    elif s == 'empty':
        if arr:
            print(0)
        else:
            print(1)
    elif s == 'front':
        if arr:
            print(arr[0])
        else:
            print(-1)
    elif s == 'back':
        if arr:
            print(arr[-1])
        else:
            print(-1)
