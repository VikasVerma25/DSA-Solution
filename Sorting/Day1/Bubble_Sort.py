def bubble(arr,n):
    for i in range(n):
        isswap = 0
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                isswap = 1
        if isswap == 0:
            break

arr = [3,1,6,5,9,8]
bubble(arr,len(arr))
print(arr)
            