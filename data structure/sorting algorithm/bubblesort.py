def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]> arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

x = int(input("enter a number: "))
y = []
for i in range(x):
    z=int(input("enter a number: "))
    y.append(z)

bubblesort(y)
print("sorted array: ",y)