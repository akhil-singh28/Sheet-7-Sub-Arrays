n= int(input())
arr = list(map(int, input().split()))
for i in range(n):
    total = 0
    for j in range(i, n):
        total += arr[j]
        print(total)
