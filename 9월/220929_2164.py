N = int(input())
arr = [x for x in range(1,N+1)]
while len(arr) != 1:
    arr.remove(arr[0])
    save = arr[0]
    for i in range(len(arr)-1):
        arr[i] =arr[i+1]
    arr[len(arr)-1] = save
print(*arr)