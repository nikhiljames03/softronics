def bubble(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1] :
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr = [6,4,89,65,32,92]
bubble(arr)
print(arr)