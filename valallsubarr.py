n = int(input())
arr = list(map(int, input().split()))
def subA(arr, n):
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j + 1):
                print(arr[k], end=' ')
            print()
subA(arr, n)


